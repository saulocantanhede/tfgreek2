# Text-Fabric features Nestle 1904 (sorted per node type)
###### *(or browse by [feature type](featuresbyfeaturetype.md#readme) or [feature group](featuresbygroup.md#readme))*

This Text-Fabric dataset contains the following node types:
* [`w` (word) nodes](#word-nodes)
* [`wg` (wordgroup) nodes](#wordgroup-nodes)
* [`phrase` nodes](#phrase-nodes)
* [`clause` nodes](#clause-nodes)
* [`sentence` nodes](#sentence-nodes)
* [`verse` nodes](#verse-nodes)
* [`chapter`nodes](#chapter-nodes)
* [`book` nodes](#book-nodes)

Below are all node features listed: 

## Word nodes 

Feature | Feature group |Data type | Description
--- | --- | --- | ---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | space or punctuation after word
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated)
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical case (nominative, genitive, ..., vocative)
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features)  | `String` | Word class: Part of Speech (`noun` `verb`)
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Degree of an comparative or superlative adjective
[discontinuous](discontinuous.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) |`String` | Discontinuous information
[domain](domain.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG
[gender](gender.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical gender (masculine, feminine, neuter)
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | English gloss
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexeme (lemma)
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Louw-Nida lexical classification 
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Morphological tag (Sandborg-Petersen morphology)
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | {possibly to be added: monad}
[mood](mood.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical mood of a verb (indicative, optative, etc.)
[nodeId](nodeId.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Node Id
[normalized](normalized.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Surface word stripped of punctations
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sequence number (here: word in verse)
[number](number.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number of the verb
[person](person.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical person of the verb (first, second, third)
[strongs](strongs.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Strongs number
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | `String` | Subject reference (to nodeID in XML source data)
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical tense of the verb (e.g. present, aorist)
[text](text.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Word as it appears in the text
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun (e.g. common, personal)
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Verse number inside chapter
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical voice of the verb

## Wordgroup nodes 

Feature | Feature group |  Data type | Description
--- | --- | --- | --- 
[appositioncontainer](appositioncontainer.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  appositioncontainer
[articular](articular.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `Integer` | Indicates if wordgroup contains an article
[clauseType](clauseType.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause type information (`normalized`)
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | WordGroup class (e.g. `np` `cl`)
[cltype](cltype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Clause type (`Verbless` `VerbElided`)
[crule](crule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause rule (`ClCl` `ClCl2`)
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Role wordgroup (`s` `o` `apposition`)
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun (e.g. common, personal)

## Phrase nodes
Feature | Feature group | Data type | Short description
--- | --- | --- | ---


## Clause nodes
Feature | Feature group | Data type | Short description
--- | --- | --- | ---

## Sentence nodes 
Feature | Feature group | Data type | Short description
--- | --- | --- | ---

## Verse nodes 
Feature | Feature group | Data type | Short description
--- | --- | --- | ---
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Verse

## Chapter nodes 

Feature | Feature group | Data type | Description
--- | --- | --- | --- 
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Chapter
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book

## Book nodes 

Feature | Feature group | Data type | Description
--- | --- | --- | --- 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated)
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sequence number (here: book number)







