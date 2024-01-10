# Features grouped by node type <a name="start"></a>
###### *(or browse by [feature type](featuresbyfeaturetype.md#start), [data type](featuresbydatatype.md#start), or [feature group](featuresbygroup.md#start))*

This Text-Fabric dataset contains the following node types:
* [137779 `word` nodes](#word-nodes): represents individual words in the text.
* [106868 `wg` (wordgroup) nodes](#wordgroup-nodes): collection or grouping of words that form a cohesive unit. It can be any of the following:
    * [72845 `subphrase` nodes](#subphrase-nodes)
    * [113750 `phrase` nodes](#phrase-nodes)
    * [30479 `clause` nodes](#clause-nodes)
    * [8964 `group` nodes](#group-nodes)
* [18609 `sentence` nodes](#sentence-nodes)
* [7944 `verse` nodes](#verse-nodes)
* [260 `chapter`nodes](#chapter-nodes)
* [27 `book` nodes](#book-nodes)

Below are all node features listed: 

## Word nodes 

<sup>Note: this node type is associated with both the [WordGroup view](wg-view.md#start) and the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | All material found after a word | `. ` `; ` ` `
[before](before.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Text-critical signs before word | `[` `(` `—`
[bol_lemma](bol_lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | lexical lemma provided by Bible Online Learner | `ὁ` `καί`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full) | `Matthew` `Mark` ... `Revelation`
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (abbreviated) | `MAT` `MAR` ... `REV`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical case | `nominative` `genitive` `vocative`
[chapter](chapter.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Chapter number inside book |
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features)  | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word class: Part of Speech | `noun` `verb`
[criticalsign](criticalsign.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | text-critical signs | `(` `[` `)` `]`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an comparative or superlative adjective |
[discontinuous](discontinuous.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Discontinuous information
[domain](domain.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG |
[gender](gender.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss |
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexeme (lemma) | 
[ln](ln.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | 
[morph](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Morphological tag (Sandborg-Petersen morphology) |
[monad](monad.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | {possibly to be added: monad} | 
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative`
[nodeId](nodeId.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Node Id | 
[normalized](normalized.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations
[note](note.md#start) | ? | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Annotation of linguistic nature | `discontinuous discourse`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sequence number (here: word in verse)
[number](number.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number of the verb
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[parent](parent.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Edge`](featuresbyfeaturetype.md#edge-features) | `link` | Link to parent node
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person of the verb (first, second, third)
[punctuation](punctuation.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Punctuation | ` ` `.`
[ref](ref.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes)  [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Unique identity of a word | `1CO 10:1!1`
[strong](strong.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Strong's number
[unicode](unicode.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Unicode text |
[sibling](sibling.md#start) | [`Relational`](featuresbygroup.md#relational-features) |  [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Sibling relationship between words | 
[subjrefspec](subjrefspec.md#start) | [`Relational`](featuresbygroup.md#relational-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Subject reference (to nodeID in XML source data) |
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[text](text.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word as it appears in the text |
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word in unicode format | `Λόγος` `Θεόν,`
[variant](variant.md#start) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical variant | `1` `2`
[verse](verse.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Verse number inside chapter |
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb |

## Wordgroup nodes 

<sup>Note: this node type is only associated with the [WordGroup view](wg-view.md#start).</sup> 

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[appositioncontainer](appositioncontainer.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  appositioncontainer |
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Indicates if wordgroup contains an article | `1`
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (abbreviated) | `MAT` `MAR` ... `REV`
[clausetype](clausetype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Clause type information | `normalized`)
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | WordGroup class | `np` `cl`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction |  `coordinate` `subordinate`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[parent](parent.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Edge`](featuresbyfeaturetype.md#edge-features) | `link` | Link to parent node |
[rela](rela.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Appostion information | `Appo` 
[role](role.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Role wordgroup | `s` `o` `apposition`
[rule](rule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic rule | `ClCl` `ClCl2`
[type](type.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |Clause type | `Verbless` `VerbElided`

## Subphrase nodes

<sup>Note: this node typs is only associated with the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | All material found after a word | `. ` `; ` ` `
[before](before.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Text-critical signs before word | `[` `(` `—`
[bol_lemma](bol_lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | lexical lemma provided by Bible Online Learner | `ὁ` `καί`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical case | `nominative` `genitive` `vocative`
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Class of the subphrase  | `np` `cl`
[criticalsign](criticalsign.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | text-critical signs | `(` `[` `)` `]`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an comparative or superlative adjective |
[discontinuous](discontinuous.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Discontinuous information
[domain](domain.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG |
[framespec](framespec.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | this is XML attribute framespec | `A0:n00000000000` `A1:n00000000000`
[function](function.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | this is XML attribute function | `Pred` `Subj`
[gender](gender.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss |
[id](id.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | xml id | `n40001001001`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) |  [`string`](featuresbydatatype.md#string-datatype) | Junction |  `coordinate` `subordinate`
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexeme (lemma) | 
[ln](ln.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | 
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative`
[morph](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | morphological code | `CONJ` `PREP`
[normalized](normalized.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations
[note](note.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Annotation of linguistic nature | `discontinuous discourse`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Phrase number inside book | `1` `2`
[number](number.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number of the verb | 
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person of the verb (first, second, third)
[punctuation](punctuation.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Punctuation | ` ` `.`
[ref](ref.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes)  [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Unique identity of a word | `1CO 10:1!1`
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[text](text.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word as it appears in the text |
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word in unicode format | `Λόγος` `Θεόν,`
[variant](variant.md#start) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical variant | `1` `2`
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb |

## Phrase nodes

<sup>Note: thes node type is only associated with the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | All material found after a word | `. ` `; ` ` `
[appositioncontainer](appositioncontainer.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  appositioncontainer |
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Indicates if wordgroup contains an article | `1`
[before](before.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Text-critical signs before word | `[` `(` `—`
[bol_lemma](bol_lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | lexical lemma provided by Bible Online Learner | `ὁ` `καί`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical case | `nominative` `genitive` `vocative`
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Class of the phrase  | `np` `cl`
[criticalsign](criticalsign.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | text-critical signs | `(` `[` `)` `]`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an comparative or superlative adjective |
[discontinuous](discontinuous.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Discontinuous information
[domain](domain.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG |
[framespec](framespec.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | this is XML attribute framespec | `A0:n00000000000` `A1:n00000000000`
[function](function.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | this is XML attribute function | `Pred` `Subj`
[gender](gender.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss |
[id](id.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | xml id | `n40001001001`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) |  [`string`](featuresbydatatype.md#string-datatype) | Junction |  `coordinate` `subordinate`
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexeme (lemma) | 
[ln](ln.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | 
[note](note.md#start) | ? | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Annotation of linguistic nature | `discontinuous discourse`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative`
[morph](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | morphological code | `CONJ` `PREP`
[normalized](normalized.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations
[note](note.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Annotation of linguistic nature | `discontinuous discourse`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Phrase number inside book | `1` `2`
[number](number.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number of the verb | 
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person of the verb (first, second, third)
[punctuation](punctuation.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Punctuation | ` ` `.`
[ref](ref.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes)  [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Unique identity of a word | `1CO 10:1!1`
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[text](text.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word as it appears in the text |
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Word in unicode format | `Λόγος` `Θεόν,`
[variant](variant.md#start) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical variant | `1` `2`
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb |

## Clause nodes

<sup>Note: thes node type is only associated with the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Indicates if wordgroup contains an article | `1`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full) | 
[clausetype](clausetype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Clause type information | `normalized`)
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Class of the clause  | `np` `cl`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction |  `coordinate` `subordinate`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Clause number inside book |
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[role](role.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Role wordgroup | `s` `o` `apposition`
[rule](rule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic rule | `ClCl` `ClCl2`
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`

## Group nodes

<sup>Note: thes node type is only associated with the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Indicates if wordgroup contains an article | `1`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full) | 
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (abbreviated) | `MAT` `MAR` ... `REV`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Clause number inside book |
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of group | `conjuncted`
[role](role.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Role wordgroup | `s` `o` `apposition`
[rule](rule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic rule | `ClCl` `ClCl2`
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`

## Sentence nodes 

<sup>Note: this node type is associated with both the [WordGroup view](wg-view.md#start) and the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Indicates if wordgroup contains an article | `1`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full)
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (abbreviated) | `MAT` `MAR` ... `REV`
[clausetype](clausetype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Clause type information | `normalized`)
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | WordGroup class | `np` `cl`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction |  `coordinate` `subordinate`
[nodeId](nodeId.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Node Id | `400010200010490`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sentence number inside book | `1` `2`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 
[parent](parent.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Edge`](featuresbyfeaturetype.md#edge-features)  | `link` | Link to parent node
[role](role.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Role wordgroup | `s` `o` `apposition`
[rule](rule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic rule | `ClCl` `ClCl2`
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`

## Verse nodes 

<sup>Note: this node type is associated with both the [WordGroup view](wg-view.md#start) and the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full) | `Luke` `Matthew`
[chapter](chapter.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Chapter number inside book | `1` `2`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features)) | mapping between node number and associated objecttype | 
[verse](verse.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Verse number inside chapter | 

## Chapter nodes 

<sup>Note: this node type is associated with both the [WordGroup view](wg-view.md#start) and the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  Book name (full) | `Luke` `Matthew`
[chapter](chapter.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Chapter | `1` `2`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 

## Book nodes 

<sup>Note: this node type is associated with both the [WordGroup view](wg-view.md#start) and the [Syntactic view](syntactic-view.md#start).</sup>

Feature | Feature group | Feature type | Data type | Short description | Examples
--- | --- | --- | --- | --- | ---
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (full) | `Luke` `Matthew`
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (abbreviated) | `LUK` `ACT`
[lang](lang.md#start) |  [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | Language of the corpus | `el`
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sequence number (here: book number) | `1` `2`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | [`Node`](featuresbyfeaturetype.md#node-features) | mapping between node number and associated objecttype | 







