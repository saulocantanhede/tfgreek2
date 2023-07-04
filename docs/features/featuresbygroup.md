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

Name | Description| Examples
---|---|---
[oslots](oslots.md) | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md) | node type | `book` `verse` `clause` `phrase` `word`

## Sectional features

Name | Description | Examples
---|---|---
[book](book.md#readme) | Short book name | `MAT` `MAR` ... `REV`
[chapter](chapter.md#readme) | Chapter number inside book | `1` `2` ...
[id](id.md#readme) | Unique identity of a word | `n40001003006`
[monad](monad.md#readme) | Monad | *to be added?*
[nodeId](nodeId.md#readme) | Node Id  | `n56001015007`
[num](num.md#readme) | Sequence number  | `1` `2` ...   
[verse](verse.md#readme) | Verse number inside chapter | `1` `2`

## Lexical features

Name| Description| Examples
---|---|---
[gloss](gloss.md#readme) | English gloss | 
[lemma](lemma.md#readme) | Lexical lemma (cf. BDAG) |
[domain](domain.md#readme) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | Louw-Nida lexical classification | `93.169a`
[strongs](strongs.md#readme) | Strongs number | `5547`

## Orthograpic features

Name | Description | Examples
--- | --- | ---
[after](after.md#readme) | Space or punctuation after word | ` ` `.`
[normalized](normalized.md#readme) | Surface word stripped of punctations |
[text](text.md#readme) | Word as it appears in the text | 

## Morphological features

Name | Description | Examples
--- | --- | ---
[case](case.md#readme) | Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#readme) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gender](gender.md#readme) | Gramatical gender | `masculine` `feminine` `neuter`
[mood](mood.md#readme) | Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#readme) | Morphological tag | `V-AAI-3S` `N-GSF`
[number](number.md#readme) | Gramatical number | `singular` `plural`
[person](person.md#readme) | Gramatical person | `first` `second` `third`
[tense](tense.md#readme) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | Gramatical type of noun or pronoun | `common` `personal`
[voice](voice.md#readme) | Gramatical voice of the verb | `active` `passive`

## Syntactic features

Name | Description | Examples
--- | --- | ---
[appostioncontainer](appositioncontainer.md#readme) | Appostioncontainer information | `1` 
[articular](articular.md#readme) | Articular information | `1`
[clauseType](clauseType.md#readme) | Clause type information | `normalized`
[cls](cls.md#readme) | Word and WordGroup class (Part of Speech) | `noun` `verb` / `np` `cl`
[cltype](cltype.md#readme) | Clause type | `Verbless` `VerbElided`
[crule](crule.md#readme) | Clause rule | `ClCl` `ClCl2`
[discontinuous](discontinuous.md#readme) | Discontinuous information | `1`
[junction](junction.md#readme) | Junction information | `1`
[role](role.md#readme) | Role of word or wordgroup | `s` `o` `apposition`
[type](type.md#readme) | Syntactical type of wordgroup | `conjuncted-wg` `apposition-group`

## Relational features

Name | Description | Example
--- | --- | ---
[frame](frame.md#readme) | Frame |
[framespec](framespec.md#readme) | Framespec |
[note](note.md#readme) | Notes |
[parent](parent.md#readme) | Parent | 
[referent](referent.md#readme) | Referent | `n40001011005`
[subj_ref](subj_ref.md#readme) | Subject reference |
[sibling](sibling.md#readme) | Sibling | 
