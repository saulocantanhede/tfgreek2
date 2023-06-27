import re
from lxml import etree
from io import BytesIO

from tf.core.helpers import console
from tf.core.files import initTree, unexpanduser as ux

from tf.convert.helpers import XNEST, TNEST, TSIB

# set this to true if you want to create demo data on the oldest
# xml version with the first sentence of Jude twice:
# once without and once with slot reordering
demoMode = False

book_name = {'MAT': 'Matthew', 'MRK': 'Mark', 'LUK': 'Luke', 'JHN': 'John', 'ACT': 'Acts', 'ROM': 'Romans', '1CO': '1Corinthians',
            '2CO': '2Corinthians', 'GAL': 'Galatians', 'EPH': 'Ephesians', 'PHP': 'Philippians', 'COL': 'Colossians',
            '1TH': '1Thessalonians', '2TH': '2Thessalonians', '1TI': '1Timothy', '2TI': '2Timothy', 'TIT': 'Titus', 'PHM': 'Philemon',
            'HEB': 'Hebrews', 'JAS': 'James', '1PE': '1Peter','2PE': '2Peter', '1JN': '1John', '2JN': '2John', '3JN': '3John',
            'JUD': 'Jude', 'REV': 'Revelation'}

type_features = {"adjp": "AdjP",
                 "advp": "AdvP",
                 "np": "NP",
                 "pp": "PP",
                 "vp": "VP"}

role_features = {"io": "Cmpl",
                 "o": "Objc",
                 "o2": "Objc",
                 "p": "Pred",
                 "s": "Subj"}

def convertTaskCustom(self):
    """Implementation of the "convert" task.

    It sets up the `tf.convert.walker` machinery and runs it.

    ### Important details

    *   **parents/siblings**
        We only compute parents and siblings for de `wg` elements and their
        descendant elements (only `wg` and `w`).

        If we would do siblings between sentences, the sibling feature would grow
        enormously and take up 40% of the dataset.

    *   The `subjref` attribute contains essentially a link to another node,
        identified by the `id` attribute. We move this attribute to feature
        `subjrefspec`, but we also create an edge feature `subjref` with the
        corresponding information.

    *   The `frame` attribute contains essentially labelled links to other nodes,
        identified by the `id` attribute. We move this attribute to feature
        `framespec`, but we also create an edge feature `frame` with the
        corresponding information.

    *   Clause and phrase nodes have been added, they duplicate some of the `wg`
        nodes. Only for wg-s with an attribute `class`.

        * clauses are `wg` with `class="cl"`
        * phrases are `wg` with `class` something else, but not empty


    Returns
    -------
    boolean
        Whether the conversion was successful.
    """
    if not self.good:
        return

    verbose = self.verbose
    tfPath = self.tfPath
    xmlPath = self.xmlPath

    if verbose == 1:
        console(f"XML to TF converting: {ux(xmlPath)} => {ux(tfPath)}")

    slotType = "word"
    otext = {
        "fmt:text-orig-full": "{text}{after}",
        "sectionTypes": "book,chapter,verse",
        "sectionFeatures": "book,chapter,verse",
    }
    monoAtts = {"appositioncontainer", "articular", "discontinuous"}

    self.monoAtts = monoAtts

    #information about the authors and the version of the datasource
    tfVersion = self.tfVersion
    xmlVersion = self.xmlVersion
    generic = self.generic
    generic["author"] = "Evangelists and apostles"
    generic["title"] = "Greek New Testament"
    generic["institute"] = "ETCBC (Eep Talstra Centre for Bible and Computer)"
    generic["converters"] = "Saulo de Oliveira Cantanhêde, Tony Jorg, Dirk Roorda"
    generic["sourceFormat"] = "XML lowfat"
    generic["version"] = tfVersion
    generic["xmlVersion"] = xmlVersion
    intFeatures = self.intFeatures
    featureMeta = self.featureMeta

    initTree(tfPath, fresh=True, gentle=True)

    cv = self.getConverter()

    self.good = cv.walk(
        getDirector(self),
        slotType,
        otext=otext,
        generic=generic,
        intFeatures=intFeatures,
        featureMeta=featureMeta,
        generateTf=True,
    )


def getDirector(self):
    """Factory for the director function.

    The `tf.convert.walker` relies on a corpus dependent `director` function
    that walks through the source data and spits out actions that
    produces the TF dataset.

    We collect all needed data, store it, and define a local director function
    that has access to this data.

    You can also include a copy of this file in the script that constructs the
    object. If you then tweak it, you can pass it to the XML() object constructor.

    Returns
    -------
    function
        The local director function that has been constructed.
    """

    SPLIT_REF = re.compile(r"[ :!]")

    PASS_THROUGH = set(
        """
        xml
        p
        milestone
        """.strip().split()
    )

    # CHECKING

    verbose = self.verbose
    xmlPath = self.xmlPath
    featureMeta = self.featureMeta
    transform = self.transform
    renameAtts = self.renameAtts
    monoAtts = self.monoAtts

    transformFunc = (
        (lambda x: BytesIO(x.encode("utf-8")))
        if transform is None
        else (lambda x: BytesIO(transform(x).encode("utf-8")))
    )

    parser = self.getParser()

    # WALKERS

    def walkNode(cv, cur, xnode):
        """Internal function to deal with a single element.

        Will be called recursively.

        Parameters
        ----------
        cv: object
            The convertor object, needed to issue actions.
        cur: dict
            Various pieces of data collected during walking
            and relevant for some next steps in the walk.
        xnode: object
            An lxml element node.
        """
        tag = etree.QName(xnode.tag).localname

        if tag == "w":
            tag = "word"

        nestable = tag in {"word", "wg"}

        cur[XNEST].append(tag)

        (curNode, extraNode) = beforeChildren(cv, cur, xnode, tag)

        if curNode is not None:
            if len(cur[TNEST]):
                if nestable:
                    parentNode = cur[TNEST][-1]
                    cv.edge(curNode, parentNode, parent=None)

            cur[TNEST].append(curNode)

            if len(cur[TSIB]):
                if nestable:
                    siblings = cur[TSIB][-1]

                    nSiblings = len(siblings)
                    for (i, sib) in enumerate(siblings):
                        cv.edge(sib, curNode, sibling=nSiblings - i)
                    siblings.append(curNode)

            cur[TSIB].append([])

        for child in xnode.iterchildren(tag=etree.Element):
            walkNode(cv, cur, child)

        afterChildren(cv, cur, xnode, tag)

        if extraNode is not None:
            cv.terminate(extraNode)

        if curNode is not None:
            if len(cur[TNEST]):
                cur[TNEST].pop()
            if len(cur[TSIB]):
                cur[TSIB].pop()

        cur[XNEST].pop()
        afterTag(cv, cur, xnode, tag)

    def beforeChildren(cv, cur, xnode, tag):
        """Actions before dealing with the element's children.

        Parameters
        ----------
        cv: object
            The convertor object, needed to issue actions.
        cur: dict
            Various pieces of data collected during walking
            and relevant for some next steps in the walk.
        xnode: object
            An lxml element node.
        tag: string
            The tag of the lxml node.

        Returns
        -------
        tuple | void
            The resulting TF node, if any, else None
        """
        if tag in PASS_THROUGH:
            return (None, None)

        atts = {etree.QName(k).localname: v for (k, v) in xnode.attrib.items()}
        atts = {renameAtts.get(k, k): v for (k, v) in atts.items()}
        for m in monoAtts:
            if atts.get(m, None) == "true":
                atts[m] = 1

        if tag == "error":
            tag = "wg"
        
        if tag == "w":
            tag = "word"

        (curNode, extraNode) = (None, None)

        extraType = None

        if tag == "word":
            atts["text"] = xnode.text

            #atts_phrase={} #saving only specific features in the features of the phrase
            atts_phrase=atts #saving all features of the words in the features of the phrase

            #obtaining class and role of word attributes for the phrase container
            cls = atts.get("cls", None)
            role = atts.get("role", None)

            #generate phrase and subphrase containers for the words as an extra node
            if role is not None:
                extraType = "phrase"

                cur["phraseNum"] += 1 #counting the number of the phrases
                atts_phrase["num"] = cur["phraseNum"]
            
            elif cls == "conj":
                extraType = "phrase"
            
                cur["phraseNum"] += 1 #counting the number of the phrases
                atts_phrase["num"] = cur["phraseNum"]
            
            else:
                extraType = "subphrase"
            
                cur["subphraseNum"] += 1 #counting the number of the subphrases
                atts_phrase["num"] = cur["subphraseNum"]
            
            if cls in type_features:
                atts_phrase["typ"] = type_features[cls]
            
            if role in role_features:
                atts_phrase["function"] = role_features[role]
            
            if role == "apposition":
                atts_phrase["rela"] = "Appo"
            
            #save word attributes as features for the extra nodes
            extraNode = cv.node(extraType)
            if len(atts):
                cv.feature(extraNode, **atts_phrase)     

            ref = atts["ref"]
            (bRef, chRef, vRef, wRef) = SPLIT_REF.split(ref)
            if bRef in book_name:
                atts["book_short"]=bRef
                thisBook = book_name[bRef]
                atts["book"] = thisBook
            atts["chapter"] = chRef
            atts["verse"] = vRef
            atts["num"] = wRef
            thisChapterNum = atts["chapter"]
            thisVerseNum = atts["verse"]
            if thisChapterNum != cv.get("chapter", cur["chapter"]):
                if cur.get("verse", None) is not None:
                    cv.terminate(cur["verse"])
                if cur.get("chapter", None) is not None:
                    cv.terminate(cur["chapter"])

                curChapter = cv.node("chapter")
                cur["chapter"] = curChapter
                cv.feature(curChapter, chapter=thisChapterNum)

                curVerse = cv.node("verse")
                cur["verse"] = curVerse
                cv.feature(curVerse, verse=thisVerseNum, chapter=thisChapterNum, book=thisBook) #chapter and book features added to the verse node

            elif thisVerseNum != cv.get("verse", cur["verse"]):
                if cur.get("verse", None) is not None:
                    cv.terminate(cur["verse"])

                curVerse = cv.node("verse")
                cur["verse"] = curVerse
                cv.feature(curVerse, verse=thisVerseNum, chapter=thisChapterNum, book=thisBook) #chapter and book features added to the verse node

            key = f"B{cur['bookNum']:>03}-C{chRef:>03}-V{vRef:>03}-W{wRef:>04}"

            if demoMode:
                if cur["sentNum"] == 1:
                    key = None

            curNode = cv.slot(key=key)
            cv.feature(curNode, **atts)

            xId = atts.get("id", None)
            if xId is not None:
                cur["xIdIndex"][xId] = curNode

            subjrefSpec = atts.get("subjrefspec", None)
            if subjrefSpec is not None:
                parts = subjrefSpec.split()
                for xIds in parts:
                    cur["subjrefEdges"].append((curNode, xIds))

            frameSpec = atts.get("framespec", None)
            if frameSpec is not None:
                parts = frameSpec.split()
                for part in parts:
                    (label, xIds) = part.split(":")
                    cur["frameEdges"].append((curNode, xIds, label))

        else:

            if tag == "book":
                cur["bookNum"] += 1
                atts["num"] = cur["bookNum"]
                atts["book_short"] = atts["id"] #defining the attribute book_short
                if atts["id"] in book_name: #including the attribute book for the whole name of the book
                    atts["book"] = book_name[atts["id"]]
                del atts["id"]

            elif tag == "sentence":
                cur["sentNum"] += 1
                atts["num"] = cur["sentNum"]
                
            elif tag == "wg":
                cls = atts.get("cls", None)
                role = atts.get("role")
                cltype = atts.get("cltype")
                clauseType = atts.get("clauseType")
                rule = atts.get("rule")
                if cls is not None:
                    if cls == "cl":
                        extraType = "clause" #generate clause container from the wg tag

                        cur["clNum"] += 1 #counting the number of the clauses
                        atts["num"] = cur["clNum"]
                        
                        #atts["typ"] = cltype
                        #atts["typ"] = clauseType
                        #atts["typ"] = rule
                        
                    else:
                        extraType = "phrase" #generate phrase container for the words within the wg tag

                        cur["phraseNum"] += 1 #counting the number of the phrases
                        atts["num"] = cur["phraseNum"]
                        
                        if cls in type_features:
                            atts["typ"] = type_features[cls]
                        
                        if role in role_features:
                            atts["function"] = role_features[role]
                        
                        if role == "apposition":
                            atts["rela"] = "Appo"

            curNode = cv.node(tag)
            if len(atts):
                cv.feature(curNode, **atts)

            if extraType is not None:
                extraNode = cv.node(extraType)
                if len(atts):
                    cv.feature(extraNode, **atts)

        return (curNode, extraNode)

    def afterChildren(cv, cur, xnode, tag):
        """Node actions after dealing with the children, but before the end tag.

        Here we make sure that the newline elements will get their last slot
        having a newline at the end of their `after` feature.

        Parameters
        ----------
        cv: object
            The convertor object, needed to issue actions.
        cur: dict
            Various pieces of data collected during walking
            and relevant for some next steps in the walk.
        xnode: object
            An lxml element node.
        tag: string
            The tag of the lxml node.
        """
        if tag == "error":
            tag = "wg"
        
        if tag == "w":
            tag == "word"

        if tag not in PASS_THROUGH:
            if tag == "book":
                cv.terminate(cur["verse"])
                cv.terminate(cur["chapter"])

            if len(cur[TNEST]):
                curNode = cur[TNEST][-1]
                cv.terminate(curNode)

    def afterTag(cv, cur, xnode, tag):
        """Node actions after dealing with the children and after the end tag.

        This is the place where we proces the `tail` of an lxml node: the
        text material after the element and before the next open/close
        tag of any element.

        Parameters
        ----------
        cv: object
            The convertor object, needed to issue actions.
        cur: dict
            Various pieces of data collected during walking
            and relevant for some next steps in the walk.
        xnode: object
            An lxml element node.
        tag: string
            The tag of the lxml node.
        """
        pass

    def director(cv):
        """Director function.

        Here we program a walk through the XML sources.
        At every step of the walk we fire some actions that build TF nodes
        and assign features for them.

        Because everything is rather dynamic, we generate fairly standard
        metadata for the features.

        Parameters
        ----------
        cv: object
            The convertor object, needed to issue actions.
        """
        cur = {}

        i = 0
        cur["bookNum"] = 0

        brokenRefs = {}

        for (xmlFolder, xmlFiles) in self.getXML():
            for xmlFile in xmlFiles:
                i += 1
                console(f"\r{i:>4} {xmlFile:<50}", newline=False)

                with open(f"{xmlPath}/{xmlFolder}/{xmlFile}", encoding="utf8") as fh:
                    text = fh.read()
                    text = transformFunc(text)
                    tree = etree.parse(text, parser)
                    root = tree.getroot()
                    cur[XNEST] = []
                    cur[TNEST] = []
                    cur[TSIB] = []
                    cur["chapter"] = None
                    cur["verse"] = None
                    cur["sentNum"] = 0
                    cur["clNum"] = 0 #define number of the clause
                    cur["phraseNum"] = 0 #define number of the phrase
                    cur["subphraseNum"] = 0 #define number of the subphrase
                    cur["xIdIndex"] = {}
                    cur["subjrefEdges"] = []
                    cur["frameEdges"] = []
                    walkNode(cv, cur, root)

                xIdIndex = cur["xIdIndex"]
                noXId = "n00000000000"

                for (fromNode, xIds) in cur["subjrefEdges"]:
                    for xId in xIds.split(";"):
                        toNode = fromNode if xId == noXId else xIdIndex.get(xId, None)
                        if toNode is None:
                            brokenRefs.setdefault("subjref", {}).setdefault(
                                f"{xmlFolder}/{xmlFile}", set()
                            ).add(xId)
                        else:
                            cv.edge(fromNode, toNode, subjref=None)

                for (fromNode, xIds, label) in cur["frameEdges"]:
                    for xId in xIds.split(";"):
                        toNode = fromNode if xId == noXId else xIdIndex.get(xId, None)
                        if toNode is None:
                            brokenRefs.setdefault("frame", {}).setdefault(
                                f"{xmlFolder}/{xmlFile}", set()
                            ).add(xId)
                        else:
                            cv.edge(fromNode, toNode, frame=label)

            console("")
            if len(brokenRefs):
                for kind in ("subjref", "frame"):
                    if kind in brokenRefs:
                        brokenLinks = brokenRefs[kind]
                        nBroken = sum(len(x) for x in brokenLinks.values())
                        console(f"There are {nBroken} broken {kind} references.")
                        if verbose >= 0:
                            for loc in sorted(brokenLinks):
                                refs = sorted(brokenLinks[loc])
                                nRefs = len(refs)
                                refStr = ", ".join(refs[0:3])
                                if nRefs > 3:
                                    refStr += f" ... ({nRefs - 3} more)"
                                console(f"{loc:<30}: {refStr}")
                    else:
                        console(f"There are no broken {kind} references.")
            else:
                console("There are no broken references.")

        for fName in featureMeta:
            if not cv.occurs(fName):
                cv.meta(fName)
        for fName in cv.features():
            if fName not in featureMeta:
                cv.meta(
                    fName,
                    description=f"this is XML attribute {fName}",
                    valueType="str",
                )

        if verbose == 1:
            console("source reading done")
        return True

    return director
