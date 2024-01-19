from multiprocessing.resource_sharer import stop
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

book_name = {'MAT': 'Matthew', 'MRK': 'Mark', 'LUK': 'Luke', 'JHN': 'John', 'ACT': 'Acts', 'ROM': 'Romans', '1CO': 'I_Corinthians',
            '2CO': 'II_Corinthians', 'GAL': 'Galatians', 'EPH': 'Ephesians', 'PHP': 'Philippians', 'COL': 'Colossians',
            '1TH': 'I_Thessalonians', '2TH': 'II_Thessalonians', '1TI': 'I_Timothy', '2TI': 'II_Timothy', 'TIT': 'Titus', 'PHM': 'Philemon',
            'HEB': 'Hebrews', 'JAS': 'James', '1PE': 'I_Peter','2PE': 'II_Peter', '1JN': 'I_John', '2JN': 'II_John', '3JN': 'III_John',
            'JUD': 'Jude', 'REV': 'Revelation'}

type_features = {"adjp": "AdjP",
                 "advp": "AdvP",
                 "np": "NP",
                 "pp": "PP",
                 "vp": "VP"}

role_features_wg = {"io": "Cmpl",
                 "o": "Objc",
                 "o2": "Objc",
                 "p": "PreC",
                 "s": "Subj",
                 "vc": "PreC",
                 "adv": "Cmpl"}

role_features_word = {"io": "Cmpl",
                 "o": "Objc",
                 "o2": "Objc",
                 "v": "Pred",
                 "s": "Subj",
                 "p": "PreC",
                 "adv": "Cmpl"}

clause_features = {"ADV": "Cmpl",
                   "IO": "Cmpl",
                   "O": "Obj",
                   "O2": "Obj",
                   "P": "PreC",
                   "S": "Subj",
                   "V": "Pred",
                   "VC": "PreC"}

character_substitution = {'ά': 'ά',
                          'έ': 'έ',
                          'ή': 'ή',
                          'ί': 'ί',
                          'ΐ': 'ΐ',
                          'ό': 'ό',
                          'ύ': 'ύ',
                          'ΰ': 'ΰ',
                          'ώ': 'ώ'}

punctuation_signs = r"[ ,.;·]"
criticalsign_signs = r"[—()]"

cl_dictionary = ["CLaCL", "CLa2CL", "CLandCL2", "CLandClClandClandClandCl",
                 "ClCl", "ClClCl", "ClClClCl", "ClClClClCl", "ClClClClClCl", 
                "ClClClClClClCl", "ClClClClClClClCl", "ClClClClClClClClCl",
                "ClClClClClClClClCl", "ClClClClClClClClClCl", "ClClClClClClClClClClClCl", "ClCl2"]

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
        "fmt:text-orig-full": "{before}{text}{after}",
        "fmt:text-orig-plain": "{text}{punctuation}",
        "fmt:lex-orig-plain": "{lemma}{punctuation}",
        "sectionTypes": "book,chapter,verse",
        "sectionFeatures": "book,chapter,verse",
        "levelConstraints": "clause < group",
    }
    monoAtts = {"appositioncontainer", "articular", "discontinuous"}

    intFeatures = {
        "appositioncontainer",
        "articular",
        "chapter",
        "discontinuous",
        "nodeid",
        "num",
        "strong",
        "verse",
        "sibling",
    }
    featureMeta = (
        ("after", "material after the end of the word"),
        ("appositioncontainer", "1 if it is an apposition container"),
        ("articular", "1 if the sentence, group, clause, phrase or wg has an article"),
        ("book", "book name (full name)"),
        ("bookshort", "book name (abbreviated) from ref attribute in xml"),
        ("case", "grammatical case"),
        ("chapter", "chapter number, from ref attribute in xml"),
        ("class", "morphological class (on word); syntactical class (on sentence, group, clause, phrase or wg)"),
        ("clausetype", "clause type"),
        ("cltype", "clause type"),
        ("crule", "clause rule (from xml attribute Rule)"),
        ("degree", "grammatical degree"),
        ("discontinuous", "1 if the word is out of sequence in the xml"),
        ("domain", "domain"),
        ("frame", "frame"),
        ("gender", "grammatical gender"),
        ("gloss", "short translation"),
        ("id", "xml id"),
        ("junction", "type of junction"),
        ("lang", "language the text is in"),
        ("lemma", "lexical lemma"),
        ("ln", "ln"),
        ("mood", "verbal mood"),
        ("morph", "morphological code"),
        ("nodeid", "node id (as in the XML source data"),
        ("normalized", "lemma normalized"),
        (
            "num",
            (
                "generated number (not in xml): "
                "book: (Matthew=1, Mark=2, ..., Revelation=27); "
                "sentence: numbered per chapter; "
                "word: numbered per verse."
            ),
        ),
        ("number", "grammatical number"),
        ("note", "annotation of linguistic nature"),
        ("parent", "parent relationship between words"),
        ("person", "grammatical person"),
        ("ref", "biblical reference with word counting"),
        ("referent", "number of referent"),
        ("sibling", "simbling relationship between words"),
        ("strong", "strong number"),
        ("subjref", "number of subject referent"),
        ("role", "role"),
        ("rule", "syntactical rule"),
        ("text", "the text of a word"),
        ("tense", "verbal tense"),
        ("type", "morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)"),
        ("unicode", "word in unicode characters plus material after it"),
        ("verse", "verse number, from ref attribute in xml"),
        ("voice", "verbal voice")
    )
    featureMeta = {k: dict(description=v) for (k, v) in featureMeta}

    self.monoAtts = monoAtts
    self.intFeatures = intFeatures
    self.featureMeta = featureMeta

    tfVersion = self.tfVersion
    xmlVersion = self.xmlVersion
    generic = self.generic
    generic["author"] = "Evangelists and apostles" #information about the authors and the version of the datasource
    generic["title"] = "Greek New Testament"
    generic["institute"] = "ETCBC (Eep Talstra Centre for Bible and Computer), Andrews University"
    generic["converters"] = "Saulo de Oliveira Cantanhêde, Tony Jorg, Dirk Roorda"
    generic["sourceFormat"] = "XML lowfat"
    generic["version"] = tfVersion
    generic["xmlVersion"] = xmlVersion
    
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
        sentence
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
            if extraNode is not None:
                if curNode[0] == 'wg': #classification for word groups
                    superNode = extraNode
                else:
                    superNode = curNode
            else:
                superNode = curNode
        else:
            superNode = curNode

        if superNode is not None:
            nest = superNode[0] in {"phrase", "clause", "word", "sentence", "group"}
        else:
            nest = False

        #condition for nesting extraNode phrase and clause
        if extraNode is not None:
            nestablePhraseClause = extraNode[0] in {"phrase", "clause"}
        else:
            nestablePhraseClause = False

        if curNode is not None:
            #parent features for curNode word and wg
            if len(cur[TNEST]):
                if nestable:
                    parentNode = cur[TNEST][-1]
                    cv.edge(curNode, parentNode, parent=None)
            
            #parent features for extraNode phrase and clause
            if len(cur['extraParent']):
                if nestablePhraseClause:
                    parentNode = cur['extraParent'][-1]
                    cv.edge(extraNode, parentNode, parent=None)

            #parent features for superNode phrase, clause, word, sentence and group
            if len(cur['superParentNode']):
                if nest:
                    parentNode = cur['superParentNode'][-1]
                    cv.edge(superNode, parentNode, parent=None)

            cur[TNEST].append(curNode) #gleaning all the previous curNodes

            #gleaning all the previous extraNode
            if curNode[0] == 'wg':
                Node = extraNode
            else:
                Node = curNode

            cur['extraParent'].append(Node)

            cur['superParentNode'].append(superNode) #gleaning all the previous superNodes
            
            if len(cur[TSIB]):
                if nestable:
                    siblings = cur[TSIB][-1]
                    nSiblings = len(siblings)
                    for (i, sib) in enumerate(siblings):
                        cv.edge(sib, curNode, sibling=nSiblings - i)
                    siblings.append(curNode)

            if len(cur['extraSib']):
                if nestablePhraseClause:
                    siblings = cur['extraSib'][-1]
                    nSiblings = len(siblings)
                    for (i, sib) in enumerate(siblings):
                        if curNode[0] == 'wg':
                            Node = extraNode
                        else:
                            Node = curNode
                        cv.edge(sib, Node, sibling=nSiblings - i)
                    siblings.append(Node)

            if len(cur['superSib']):
                if nest:
                    siblings = cur['superSib'][-1]
                    nSiblings = len(siblings)
                    for (i, sib) in enumerate(siblings):
                        cv.edge(sib, superNode, sibling=nSiblings - i)
                    siblings.append(superNode)

            cur['superSib'].append([])        
            
            cur['extraSib'].append([])

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
        
        if extraNode is not None:
            if len(cur['extraParent']):
                cur['extraParent'].pop()
            if len(cur['extraSib']):
                cur['extraSib'].pop()

        if superNode is not None:
            if len(cur['superParentNode']):
                cur['superParentNode'].pop()
            if len(cur['superSib']):
                cur['superSib'].pop()
        
        if cur[TNEST] == []:
            cv.terminate(curNode)

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
            atts["text"] = xnode.text #text shown in the conversor is provided by the text of the XML element
            
            unicode = atts.get('unicode')
            after = atts.get('after')
            
            #Definition of punctuation feature
            punctuation_matches = re.findall(punctuation_signs, after)
            atts['punctuation'] = punctuation_matches[0] if punctuation_matches else None

            # Definition of before feature
            if unicode[0] in {"—", "(", "["}:  # words that start with "—", "(", or "["
                atts['before'] = unicode[0]
                if unicode[0] == "—":
                    atts['after'] = atts['punctuation'] = " "  # solving bug with letters in the after feature
                    atts['text'] = re.sub(r"[—]", "", unicode)
                elif unicode[0] in {"(", "["}:
                    atts['criticalsign'] = unicode[0]
                    atts['text'] = re.sub(r"[(\[]", "", unicode)
            else:
                atts['before'] = None

            if unicode[:2] == "[[":  # words that start with "[["
                atts['criticalsign'] = atts['before'] = "[["
                atts['text'] = re.sub(r"[\[\[]", "", unicode)

            # Definition of after feature
            if unicode[-1] == "—":  # words that end with "—"
                if len(unicode) >= 2 and unicode[-2] in {" ", ",", ".", ";", "·", "—", "(", ")"}:
                    atts.update({'after': unicode[-2:], 'text': re.sub(r"[ ,.;·—()]", "", unicode)})
                    punctuation_matches = re.findall(punctuation_signs, unicode)
                    criticalsign_matches = re.findall(criticalsign_signs, unicode)
                    atts['punctuation'] = punctuation_matches[0] if punctuation_matches else None
                    atts['criticalsign'] = criticalsign_matches[0] if criticalsign_matches else None
                else:
                    atts.update({'after': unicode[-1], 'punctuation': " "})

            # words that end with two punctuation signs
            if len(unicode) >= 2 and unicode[-2] in {" ", ",", ".", ";", "·", "—", "(", ")"} and unicode[-1] not in {"ὁ", "ὃ", "ὅ"}:
                atts.update({'after': unicode[-2:], 'text': re.sub(r"[ ,.;·—()]", "", unicode)})
                punctuation_matches = re.findall(punctuation_signs, unicode)
                criticalsign_matches = re.findall(criticalsign_signs, unicode)
                atts['punctuation'] = punctuation_matches[0] if punctuation_matches else None
                atts['criticalsign'] = criticalsign_matches[0] if criticalsign_matches else None

            # words "ὁ", "ὃ", "ὅ"
            if len(unicode) >= 2 and unicode[-2] in {" ", ",", ".", ";", "·", "—", "(", ")"} and unicode[-1] in {"ὁ", "ὃ", "ὅ"}:
                atts['before'] = unicode[0]
                punctuation_matches = re.findall(punctuation_signs, unicode)
                criticalsign_matches = re.findall(criticalsign_signs, unicode)
                atts['punctuation'] = punctuation_matches[0] if punctuation_matches else None
                atts['criticalsign'] = criticalsign_matches[0] if criticalsign_matches else None

            # words that end with "]]"
            if len(unicode) >= 3 and unicode[-2] in {"]"} and unicode[-3] not in {"ν"}:
                atts.update({'after': unicode[-3:], 'criticalsign': "]]", 'punctuation': "."})

            if len(unicode) >= 3 and unicode[-2] in {"]"} and unicode[-3] in {"ν"}:
                atts.update({'after': unicode[-2:], 'criticalsign': "]]"})

            # word that ends with "]"
            if unicode == "Ἐφέσῳ]":
                atts.update({'after': "]", 'criticalsign': "]"})
            
            #updating lemma
            lemma = atts.get('lemma')
            txt = atts.get('text')
            normalized = atts.get('normalized')

            for character, replacement in character_substitution.items():
                if character in lemma:
                    lemma = lemma.replace(character, replacement)
                    atts.update({'lemma': lemma})
                if character in txt:
                    txt = txt.replace(character, replacement)
                    atts.update({'text': txt})
                if character in unicode:
                    unicode = unicode.replace(character, replacement)
                    atts.update({'unicode': unicode})
                if character in normalized:
                    normalized = normalized.replace(character, replacement)
                    atts.update({'normalized': normalized})

            #dealing with variants in lemma
            if "(I)" in lemma:
                atts["variant"] = "1"
                atts.update({'lemma': lemma[:-4]})
            elif "(II)" in lemma:
                atts["variant"] = "2"
                atts.update({'lemma': lemma[:-5]})
            
            #definition of attributes for the phrases and subphrases
            
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
            
            if role in role_features_word:
                atts_phrase["function"] = role_features_word[role]
            else: #when a phrase does not contain a function element it is classified as subphrase
                extraType = "subphrase"

                cur["subphraseNum"] += 1 #counting the number of the subphrases
                atts_phrase["num"] = cur["subphraseNum"]
            
            if role == "apposition":
                atts_phrase["rela"] = "Appo"
            
            #save word attributes as features for the extra nodes
            extraNode = cv.node(extraType)
            if len(atts):
                cv.feature(extraNode, **atts_phrase)     

            ref = atts["ref"]
            (bRef, chRef, vRef, wRef) = SPLIT_REF.split(ref)
            if bRef in book_name:
                cur["bookshort"] = bRef
                thisBook = book_name[bRef]
                atts["book"] = thisBook
            atts["bookshort"] = cur["bookshort"]
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
                cv.feature(curChapter, chapter=thisChapterNum, book=thisBook) #book feature added to the chapter node

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
                atts["bookshort"] = atts["id"] #defining the attribute bookshort
                cur["bookshort"] = atts["id"]
                if atts["id"] in book_name: #including the attribute book for the whole name of the book
                    atts["book"] = book_name[atts["id"]]
                    cur['book'] = atts['book']
                del atts["id"]

            elif tag == "sentence":
                cur["sentNum"] += 1
                atts["num"] = cur["sentNum"]
                atts['book'] = cur['book']
                atts["bookshort"] = cur["bookshort"]
                
            elif tag == "wg" and len(atts): #consider only wg tag with attributes
                cls = atts.get("cls", None)
                role = atts.get("role", None)
                type = atts.get("type", None)
                rule = atts.get("rule", None)
                cltype = atts.get("cltype", None)
                crule = atts.get("crule", None)
                clausetype = atts.get("clauseType", None)
                
                #fixing features with capital letters in the middle of the word
                atts["clauseType"] = atts.get("clauseType")
                if atts["clauseType"] is not None:
                    atts["clausetype"] = atts["clauseType"]
                    del atts["clauseType"]
                atts["nodeId"] = atts.get("nodeId")
                if atts["nodeId"] is not None:
                    atts["nodeid"] = atts["nodeId"]
                    del atts["nodeId"]

                if cls is not None:
                    if cls == "cl":
                        extraType = "clause" #generate clause container from the wg tag

                        if rule is not None:
                            std= "|".join(r'\b' + re.escape(keey) + r'\b' for keey in clause_features.keys())
                            subs = lambda match: clause_features[match.group(0)]
                            atts["function"] = re.sub(std, subs, rule)
                        
                        cur["clNum"] += 1 #counting the number of the clauses
                        atts["num"] = cur["clNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]
                            
                    else:
                        extraType = "phrase" #generate phrase container for the words within the wg tag
                        
                        cur["phraseNum"] += 1 #counting the number of the phrases
                        atts["num"] = cur["phraseNum"]
                        
                        if cls in type_features:
                            atts["typ"] = type_features[cls]
                        
                        if role in role_features_wg:
                            atts["function"] = role_features_wg[role]
                        else: #when a phrase does not contain a function element it is classified as subphrase
                            extraType = "subphrase"

                            cur["subphraseNum"] += 1 #counting the number of the subphrases
                            atts["num"] = cur["subphraseNum"]
                        
                        if role == "apposition":
                            atts["rela"] = "Appo"

                else:
                    if rule == "NPofNP":
                        extraType = "phrase"

                        cur["phraseNum"] += 1 #counting the number of the phrases
                        atts["num"] = cur["phraseNum"]
                    
                    #generate clause container for specific attributes
                    elif clausetype == "nominalized" or cltype is not None or crule is not None:
                        extraType = "clause"

                        if rule is not None:
                            std= "|".join(r'\b' + re.escape(keey) + r'\b' for keey in clause_features.keys())
                            subs = lambda match: clause_features[match.group(0)]
                            atts["function"] = re.sub(std, subs, rule)
                                                                        
                        cur["clNum"] += 1
                        atts["num"] = cur["clNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]
                    
                    #generate sentence container for specific attributes
                    elif type == "wrapper-clause-scope" or type == "modifier-clause-scope":
                        extraType = "sentence"

                        cur["sentNum"] += 1 
                        atts["num"] = cur["sentNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]
                    
                    elif rule in cl_dictionary:
                        extraType = "sentence"

                        cur["sentNum"] += 1 
                        atts["num"] = cur["sentNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]

                    elif rule is not None and len(atts) == 1:
                        extraType = "sentence"

                        cur["sentNum"] += 1
                        atts["num"] = cur["sentNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]

                    #generate group container for specific attributes
                    elif type == "conjuncted-wg":
                        extraType = "group"
                        atts["typ"] = "conjuncted"

                        cur["groupNum"] += 1
                        atts["num"] = cur["groupNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]

                    elif type == "apposition-group":
                        extraType = "group"
                        atts["typ"] = "apposition"

                        cur["groupNum"] += 1
                        atts["num"] = cur["groupNum"]
                        atts['book'] = cur['book']
                        atts["bookshort"] = cur["bookshort"]
                    
                    else:
                        extraType = "phrase" #generate phrase container for the words that the clause feature is None
                        
                        cur["phraseNum"] += 1 #counting the number of the phrases
                        atts["num"] = cur["phraseNum"]

                        if role in role_features_wg:
                            atts["function"] = role_features_wg[role]
                        else: #when a phrase does not contain a function element it is classified as subphrase
                            extraType = "subphrase"

                            cur["subphraseNum"] += 1 #counting the number of the subphrases
                            atts["num"] = cur["subphraseNum"]
                        
                        if role == "apposition":
                            atts["rela"] = "Appo"
            
            else:
                return (None, None) #consider only wg tag with attributes
            
            if len(atts):
                curNode = cv.node(tag)
                cv.feature(curNode, **atts)

            if len(cur['superParentNode']) == 1 and extraType != "sentence": #defining the sentence container at the beginning of the root
                extraType = "sentence"

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
                if curNode[0] != 'book':
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
                    cur[TNEST] = [] #define dictionary that carries all the previous curNodes
                    cur[TSIB] = [] #define dictionary that carries all the siblings with curNodes
                    cur['book'] = None
                    cur["chapter"] = None
                    cur["verse"] = None
                    cur["bookshort"] = None
                    cur["sentNum"] = 0 #define number of the sentence
                    cur["groupNum"] = 0 #define number of the group
                    cur["clNum"] = 0 #define number of the clause
                    cur["phraseNum"] = 0 #define number of the phrase
                    cur["subphraseNum"] = 0 #define number of the subphrase
                    cur["xIdIndex"] = {}
                    cur["subjrefEdges"] = []
                    cur["frameEdges"] = []
                    cur["extraParent"] = [] #define dictionary that carries all the previous extraNodes
                    cur["extraSib"] = [] #define dictionary that carries all the siblings with extraNodes
                    cur["superParentNode"] = [] #define dictionary that carries all the previous superNodes
                    cur['superSib'] = [] #define dictionary that carries all the siblings with superNodes
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
            if fName == "sibling":
               cv.meta(
                    fName,
                    description=f"this is XML attribute {fName}",
                    valueType="int",
                )

        if verbose == 1:
            console("source reading done")
        return True

    return director
