# Features sorted by feature type
###### *(or browse by [node type](featuresbynodetype.md#readme) or [feature group](featuresbygroup.md#readme))*

The features of this Text-Fabric dataset:

* [Node features](#node-features):
* [Edge features](#edge-features):
* [Config features](#config-features):

## Node features

Name | Feature group | Data type | Description | Examples
---|---|---|---|---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) |[`string`](featuresbydatatype.md#string-datatype) | Space or punctuation after word | ` ` `.`
[appostioncontainer](appositioncontainer.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Appostioncontainer information | `1` 
[articular](articular.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Articular information | `1`
[before](before.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) |text-critical characters before word | `(` `[`
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Full book name | `Matthew` `Mark` ... `Revelation`
[book_short](book_short.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) |[`string`](featuresbydatatype.md#string-datatype) | Short book name | `MAT` `MAR` ... `REV`
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical case | `nominative` `genitive` `dative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) |[`integer`](featuresbydatatype.md#integer-datatype) | Chapter number inside book | `1` `2` ...
[clauseType](clauseType.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Clause type information | `normalized`
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Word and WordGroup class (Part of Speech) | `noun` `verb` / `np` `cl`
[cltype](cltype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) |[`string`](featuresbydatatype.md#string-datatype) | Clause type | `Verbless` `VerbElided`
[criticalsign](criticalsign.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) |[`string`](featuresbydatatype.md#string-datatype) | text-critical signs | `(` `[` `)` `]`
[crule](crule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Clause rule | `ClCl` `ClCl2`
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[discontinuous](discontinuous.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Discontinuous information | `1`
[domain](domain.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) |Lexical domain according to SDBG | `092004`
[frame](frame.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Frame |
[framespec](framespec.md#readme) | [`Relational`](featuresbygroup.md#relational-features) |[`string`](featuresbydatatype.md#string-datatype) | Framespec |
[gender](gender.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) |  [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss | 
[id](id.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) |[`string`](featuresbydatatype.md#string-datatype) | Unique identity of a word | `n40001003006`
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction information | `1`
[lang](lang.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Language (ISO code) | `el`
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical lemma (cf. BDAG) |
[ln](ln.md#readme) |  [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | `93.169a`
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features)| [`integer`](featuresbydatatype.md#integer-datatype) | Monad | *to be added?*
[mood](mood.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative `
[morhp](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Morphological tag | `V-AAI-3S` `N-GSF`
[nodeId](nodeId.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Node Id | `n56001015007`
[normalized](normalized.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations |
[note](note.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Linguistic annotation |
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sequence number  | `1` `2` ...   
[number](number.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number| `singular` `plural`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | [`string`](featuresbydatatype.md#string-datatype) | node type data | 
[person](person.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person | `first` `second` `third`
[punctuation](punctuation.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Punctations after the word | `.` `;`
[referent](referent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Referent | `n40001011005`
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Syntactic role | 
[strong](strong.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Strong's number | `5547`
[subjrefspec](subjrefspec.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Subject reference | `n46003022002`
[text](text.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Word as it appears in the text | `Λόγος` `καὶ`
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`string`](featuresbydatatype.md#string-datatype) | Unicode presentation of the surface text |  `Λόγος` `καὶ`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Verse number inside chapter | `1` `2`
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb | `active` `passive`


## Edge features

Name | Feature group | Data type | Description | Example
---|---|---|---|---
[frame](frame.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Frame |
[framespec](framespec.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Framespec |
[parent](parent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Parent | 
[referent](referent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Referent | `n40001011005`
[subj_ref](subj_ref.md#readme) |  [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Subject reference |
[sibling](sibling.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | Sibling | 

## Config features

Name | Feature group |Data type| Description| Examples
---|---|---|---|---
[oslots](oslots.md) | [`Grid`](featuresbygroup.md#grid-features) | | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Grid`](featuresbygroup.md#grid-features) | | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  


