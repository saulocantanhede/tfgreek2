# Text-Fabric features Nestle 1904 (sorted by feature group)
###### *(or browse by [node type](featuresbynodetype.md#readme) or [feature type](featuresbyfeaturetype.md#readme))*

This is the key to the meaning of the features in this TextFabric dataset. The available features can be taken together in the following groups: 

* [Grid features](#grid-features)
* [Sectional features](#sectional-features)
* [Lexical features](#lexical-features)
* [Orthograpic features](#orthograpic-features)
* [Morphological features](#morphological-features)
* [Syntactic features](#syntactic-features)
* [Relational features](#relational-features)

## Grid features

Name |  Feature type | Available on nodes | Description| Examples
---|---| ---|--- | ---
[oslots](oslots.md#readme) | [`Config`](featuresbyfeaturetype.md#config-features) |   | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md#readme) |  [`Config`](featuresbyfeaturetype.md#config-features) | | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md#readme)| [`Node`](featuresbyfeaturetype.md#node-features) | | node type | `book` `verse` `clause` `phrase` `word`

## Sectional features

Name | Data type | Feature type | Available on nodes | Description | Examples
---|---|---|---|---|---
[book](book.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes)  [`book`](featuresbynodetype.md#book-notes) | Full book name | `Matthew` `Mark` ... `Revelation`
[book_short](book_short.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes)  [`book`](featuresbynodetype.md#book-notes) | Short book name | `MAT` `MAR` ... `REV`
[chapter](chapter.md#readme) | `integer` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) | Chapter number inside book | `1` `2` ...
[id](id.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Unique identity of a word | `n40001003006`
[nodeId](nodeId.md#readme) | `integer` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Node Id as in XML | `400010200010490`
[num](num.md#readme) | `integer` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`book`](featuresbynodetype.md#book-nodes) | Sequence number  | `1` `2` ...   
[verse](verse.md#readme) | `integer` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`verse`](featuresbynodetype.md#verse-nodes) | Verse number inside chapter | `1` `2`

## Lexical features

Name |  Data type |Feature type | Available on nodes | Description | Examples
---|---|---|--- | ---| ---
[gloss](gloss.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | English gloss | 
[lemma](lemma.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Lexical lemma (cf. BDAG) |
[domain](domain.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Louw-Nida lexical classification | `93.169a`
[strong](strong.md#readme) | `string` |  [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Strong's number | `5547`

## Orthograpic features

Name |  Data type |Feature type | Available on nodes| Description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Space or punctuation after word | ` ` `. ` `; `
[before](before.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | text-critical characters before word | `(` `[`
[criticalsign](criticalsign.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | text-critical signs | `(` `[` `)` `]`
[normalized](normalized.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Surface word stripped of punctations | `πρὸς`
[punctuation](punctuation.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Punctations after the word | `.` `;`
[text](text.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Word as it appears in the text | `Λόγος` `Θεόν,`
[unicode](unicode.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Word in unicode format | `Λόγος` `Θεόν,`

## Morphological features

Name |  Data type | Feature type | Available on nodes |Description | Examples
--- | --- | --- | --- | --- | ---
[case](case.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gender](gender.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical gender | `masculine` `feminine` `neuter`
[mood](mood.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)| Morphological tag | `V-AAI-3S` `N-GSF`
[number](number.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical number | `singular` `plural`
[person](person.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical person | `first` `second` `third`
[tense](tense.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) | Gramatical type of noun or pronoun | `common` `personal`
[voice](voice.md#readme) | `string` | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical voice of the verb | `active` `passive`

## Syntactic features

Name | Feature type | Description | Examples
--- | --- | --- | ---
[appostioncontainer](appositioncontainer.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Appostioncontainer information | `1` 
[articular](articular.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Articular information | `1`
[clauseType](clauseType.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Clause type information | `normalized`
[cls](cls.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Word and WordGroup class (Part of Speech) | `noun` `verb` / `np` `cl`
[cltype](cltype.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Clause type | `Verbless` `VerbElided`
[crule](crule.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Clause rule | `ClCl` `ClCl2`
[discontinuous](discontinuous.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Discontinuous information | `1`
[junction](junction.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Junction information | `1`
[lang](lang.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | language the text is in | `el`
[rela](rela.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Appostion information | `Appo` 
[role](role.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Role of word or wordgroup | `s` `o` `apposition`
[type](type.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Syntactical type of wordgroup | `conjuncted-wg` `apposition-group`

## Relational features

Name | Feature type |Description | Example
--- | --- | --- | ---
[frame](frame.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Frame |
[framespec](framespec.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Framespec |
[note](note.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Notes |
[parent](parent.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Parent | 
[referent](referent.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Referent | `n40001011005`
[subjrefspec](subjrefspec.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Subject reference | `n46003022002`
[sibling](sibling.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Sibling | 
