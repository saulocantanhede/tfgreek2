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

Name | Feature type | Description| Examples
---|---|---| ---
[oslots](oslots.md) | [`Config`](featuresbyfeaturetype.md#config-features)  | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Config`](featuresbyfeaturetype.md#config-features) | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md) | [`Node`](featuresbyfeaturetype.md#node-features) | node type | `book` `verse` `clause` `phrase` `word`

## Sectional features

Name | Feature type | Description | Examples
---|---|---|---
[book](book.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Short book name | `MAT` `MAR` ... `REV`
[chapter](chapter.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Chapter number inside book | `1` `2` ...
[id](id.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Unique identity of a word | `n40001003006`
[monad](monad.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Monad | *to be added?*
[nodeId](nodeId.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Node Id  | `n56001015007`
[num](num.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Sequence number  | `1` `2` ...   
[verse](verse.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Verse number inside chapter | `1` `2`

## Lexical features

Name| Feature type | Description | Examples
---|---|---|---
[gloss](gloss.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | English gloss | 
[lemma](lemma.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Lexical lemma (cf. BDAG) |
[domain](domain.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Louw-Nida lexical classification | `93.169a`
[strongs](strongs.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Strongs number | `5547`

## Orthograpic features

Name | Feature type | Description | Examples
--- | --- | --- | ---
[after](after.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Space or punctuation after word | ` ` `.`
[normalized](normalized.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Surface word stripped of punctations |
[text](text.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Word as it appears in the text | 

## Morphological features

Name | Feature type |Description | Examples
--- | --- | --- | ---
[case](case.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gender](gender.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical gender | `masculine` `feminine` `neuter`
[mood](mood.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Morphological tag | `V-AAI-3S` `N-GSF`
[number](number.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical number | `singular` `plural`
[person](person.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical person | `first` `second` `third`
[tense](tense.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical type of noun or pronoun | `common` `personal`
[voice](voice.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical voice of the verb | `active` `passive`

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
[subj_ref](subj_ref.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Subject reference |
[sibling](sibling.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Sibling | 
