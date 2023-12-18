# Features grouped by feature type <a name="start"></a>
###### *(or browse by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), or [feature group](featuresbygroup.md#start))*

The features of this Text-Fabric dataset:

* [Node features](#node-features): the fundamental units or entities in the data model.
* [Edge features](#edge-features): relationships or links, establishing connections between nodes in the data model.
* [Config features](#config-features): contains the configuration or settings that define the behavior and parameters of the data processing or analysis.

## Node features

Name | Feature group | Data type | Available on node | Description | Examples
---|---|---|---|---|---
[after](after.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) |[`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) |  Space or punctuation after word | ` ` `.`
[appostioncontainer](appositioncontainer.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) |Appostioncontainer information | `1` 
[articular](articular.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`sentence`](featuresbynodetype.md#sentence-nodes) [`group`](featuresbynodetype.md#group-nodes)  [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)| Articular information | `1`
[before](before.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) |Text-critical signs before word | `(` `[`
[bol_lemma](bol_lemma.md#start) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Lexical lemma provided by Bible Online Learner | `ὁ` `καί`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes)  [`book`](featuresbynodetype.md#book-notes) | Full book name | `Matthew` `Mark` ... `Revelation`
[book_short](book_short.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes)  [`book`](featuresbynodetype.md#book-notes)| Short book name | `MAT` `MAR` ... `REV`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical case | `nominative` `genitive` `dative`
[chapter](chapter.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) |[`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`verse`](featuresbynodetype.md#verse-nodes) | Chapter number inside book | `1` `2` ...
[clauseType](clauseType.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |  [`clause`](featuresbynodetype.md#clause-nodes) [`wg`](featuresbynodetype.md#wordgroup-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes)
 | Clause type information | `normalized`
[cls](cls.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`clause`](featuresbynodetype.md#clause-nodes)  [`wg`](featuresbynodetype.md#wordgroup-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)
 | Word and WordGroup class (Part of Speech) | `noun` `verb` / `np` `cl`
[cltype](cltype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) |[`string`](featuresbydatatype.md#string-datatype) | [`clause`](featuresbynodetype.md#clause-nodes)  [`wg`](featuresbynodetype.md#wordgroup-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) | Clause type | `Verbless` `VerbElided`
[criticalsign](criticalsign.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) |[`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Text-critical signs | `(` `[` `)` `]`
[crule](crule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Clause rule | `ClCl` `ClCl2`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[discontinuous](discontinuous.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Discontinuous information | `1`
[domain](domain.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) |Lexical domain according to SDBG | `092004`
[frame](frame.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Frame |
[framespec](framespec.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) |[`string`](featuresbydatatype.md#string-datatype) | Framespec |
[gender](gender.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) |  [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss | 
[id](id.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) |[`string`](featuresbydatatype.md#string-datatype) | Unique identity of a word | `n40001003006`
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction information | `1`
[lang](lang.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Language (ISO code) | `el`
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical lemma (cf. BDAG) |
[ln](ln.md#start) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | `93.169a`
[monad](monad.md#start) | [`Sectional`](featuresbygroup.md#sectional-features)| [`integer`](featuresbydatatype.md#integer-datatype) | Monad | *to be added?*
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative `
[morhp](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Morphological tag | `V-AAI-3S` `N-GSF`
[nodeId](nodeId.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Node Id | `n56001015007`
[normalized](normalized.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations |
[note](note.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Linguistic annotation |
[num](num.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sequence number  | `1` `2` ...   
[number](number.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number| `singular` `plural`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | node type data | 
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person | `first` `second` `third`
[punctuation](punctuation.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Punctations after the word | `.` `;`
[ref](ref.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)  [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Unique identity of a word | `1CO 10:1!1`
[referent](referent.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Referent | `n40001011005`
[role](role.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic role | 
[strong](strong.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Strong's number | `5547`
[subjrefspec](subjrefspec.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Subject reference | `n46003022002`
[text](text.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Word as it appears in the text | `Λόγος` `καὶ`
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Unicode presentation of the surface text |  `Λόγος` `καὶ`
[verse](verse.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Verse number inside chapter | `1` `2`
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb | `active` `passive`


## Edge features

Name | Feature group | Data type | Description | Example
---|---|---|---|---
[frame](frame.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Frame |
[parent](parent.md#start) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | parent relationship between words | 
[subjref](subjref.md#start) |  [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Node number of subject reference |
[sibling](sibling.md#start) | [`Relational`](featuresbygroup.md#relational-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sibling | 

## Config features

Name | Feature group |Data type| Description| Examples
---|---|---|---|---
[oslots](oslots.md) | [`Grid`](featuresbygroup.md#grid-features) | | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Grid`](featuresbygroup.md#grid-features) | | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  


