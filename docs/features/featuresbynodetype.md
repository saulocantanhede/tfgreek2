# Text-Fabric features Nestle 1904 (sorted per node type)
###### *(or browse by [feature type](featuresbyfeaturetype.md#readme) or [feature group](featuresbygroup.md#readme))*

This Text-Fabric dataset contains the following node types:
* [`w` (word) nodes](#word-nodes)
* [`wg` (wordgroup) nodes](#wordgroup-nodes)
* [`phrase` nodes](#phrase-nodes)
* [`subphrase` nodes](#subphrase-nodes)
* [`clause` nodes](#clause-nodes)
* [`sentence` nodes](#sentence-nodes)
* [`verse` nodes](#verse-nodes)
* [`chapter`nodes](#chapter-nodes)
* [`book` nodes](#book-nodes)

Below are all node features listed: 

## Word nodes 

Feature | Feature group |Data type | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | space or punctuation after word
[before](before.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | text-critical characters before word
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated)
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical case | `nominative` `genitive` `vocative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book |
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features)  | `String` | Word class: Part of Speech | `noun` `verb`
[criticalsign](criticalsign.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | text-critical signs | `(` `[` `)` `]`
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Degree of an comparative or superlative adjective |
[discontinuous](discontinuous.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) |`String` | Discontinuous information
[domain](domain.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG |
[gender](gender.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | English gloss |
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexeme (lemma) | 
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Louw-Nida lexical classification | 
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Morphological tag (Sandborg-Petersen morphology) |
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | {possibly to be added: monad} | 
[mood](mood.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical mood of a verb | `indicative` `optative`
[nodeId](nodeId.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Node Id | 
[normalized](normalized.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Surface word stripped of punctations
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sequence number (here: word in verse)
[number](number.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number of the verb
[parent](parent.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `link` | Link to parent node
[person](person.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical person of the verb (first, second, third)
[punctuation](punctuation.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Punctuation | ` ` `.`
[strongs](strongs.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Strongs number
[unicode](unicode.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Unicode text |
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | `String` | Subject reference (to nodeID in XML source data) |
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical tense of the verb | `present` `aorist`
[text](text.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | Word as it appears in the text |
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun | `common` `personal`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Verse number inside chapter |
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical voice of the verb |

## Wordgroup nodes 

Feature | Feature group |  Data type | Description | Examples
--- | --- | --- | --- | ---
[appositioncontainer](appositioncontainer.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  appositioncontainer |
[articular](articular.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `Integer` | Indicates if wordgroup contains an article | `1`
[clauseType](clauseType.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause type information | `normalized`)
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | WordGroup class | `np` `cl`
[type](type.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Clause type | `Verbless` `VerbElided`
[parent](parent.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `link` | Link to parent node |
[rela](rela.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Appostion information | `Appo` 
[rule](rule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Syntactic rule | `ClCl` `ClCl2`
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Role wordgroup | `s` `o` `apposition`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun | `common` `personal`

## Clause nodes
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated) | 
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  Class of the clause  | `np` `cl`
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Junction |
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Clause number inside book |
[rule](rule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Syntactic rule | `ClCl` `ClCl2`

## Group nodes
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated) | 
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Clause number inside book |
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of group | `conjuncted`

## Phrase nodes
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Phrase number inside book

## Subhrase nodes
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Subphrase number inside book

## Sentence nodes 
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated)
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number inside book
[parent](parent.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `link` | Link to parent node
[rule](rule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Sentence rule

## Verse nodes 
Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Verse number inside chapter
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book

## Chapter nodes 

Feature | Feature group | Data type | Description
--- | --- | --- | --- 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (abbriviated)
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Chapter
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book

## Book nodes 

Feature | Feature group | Data type | Description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated)
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sequence number (here: book number)







