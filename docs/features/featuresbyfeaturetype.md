# Text-Fabric features Nestle 1904 (sorted by feature type)
###### *(or browse by [node type](featuresbynodetype.md#readme) or [feature group](featuresbygroup.md#readme))*

The features of this Text-Fabric dataset:

* [Node features](#node-features):
* [Edge features](#edge-features):
* [Config features](#config-features):

## Node features

Name | Feature group | Description | Examples
---|---|---| ---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) |Space or punctuation after word | ` ` `.`
[appostioncontainer](appositioncontainer.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Appostioncontainer information | `1` 
[articular](articular.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Articular information | `1`
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Short book name | `MAT` `MAR` ... `REV`
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) |  Gramatical case | `nominative` `genitive` `dative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Chapter number inside book | `1` `2` ...
[clauseType](clauseType.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Clause type information | `normalized`
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Word and WordGroup class (Part of Speech) | `noun` `verb` / `np` `cl`
[cltype](cltype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Clause type | `Verbless` `VerbElided`
[crule](crule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Clause rule | `ClCl` `ClCl2`
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[discontinuous](discontinuous.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Discontinuous information | `1`
[domain](domain.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | Lexical domain according to SDBG | `092004`
[frame](frame.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Frame |
[framespec](framespec.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Framespec |
[gender](gender.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | English gloss | 
[id](id.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Unique identity of a word | `n40001003006`
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Junction information | `1`
[lang](lang.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | Language (ISO code) | `el`
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | Lexical lemma (cf. BDAG) |
[ln](ln.md#readme) |  [`Lexical`](featuresbygroup.md#lexical-features) | Louw-Nida lexical classification | `93.169a`
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features)| Monad | *to be added?*
[mood](mood.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Gramatical mood of a verb | `indicative` `optative `
[morhp](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) |  Morphological tag | `V-AAI-3S` `N-GSF`
[nodeId](nodeId.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Node Id | `n56001015007`
[normalized](normalized.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | Surface word stripped of punctations |
[note](note.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) |Linguistic annotation |
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) |  Sequence number  | `1` `2` ...   
[number](number.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Gramatical number| `singular` `plural`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | node type data | 
[person](person.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Gramatical person | `first` `second` `third`
[referent](referent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Referent | `n40001011005`
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | Syntactic role | 
[strongs](strongs.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | Strongs number | `5547`
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Subject reference |
[text](text.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | Word as it appears in the text | 
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) |  Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) [`Syntactic`](featuresbygroup.md#syntactic-features) | Gramatical type of noun or pronoun | `common` `personal`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Sequence number  | `1` `2` ...   Verse number inside chapter | `1` `2`
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | Gramatical voice of the verb | `active` `passive`


## Edge features

Name | Feature group |Description | Example
--- | --- | --- | ---
[frame](frame.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Frame |
[framespec](framespec.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Framespec |
[parent](parent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Parent | 
[referent](referent.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Referent | `n40001011005`
[subj_ref](subj_ref.md#readme) |  [`Relational`](featuresbygroup.md#relational-features) |Subject reference |
[sibling](sibling.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | Sibling | 

## Config features

Name | Feature group | Description| Examples
---|---|---| ---
[oslots](oslots.md) | [`Grid`](featuresbygroup.md#grid-features) | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Grid`](featuresbygroup.md#grid-features) | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  


