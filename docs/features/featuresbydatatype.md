# Features by data type  <a name="start"></a>
###### *(or browse by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), or [feature type](featuresbyfeaturetype.md#start))*

This is the key to the meaning of the features in this TextFabric dataset. The available features can be taken together in the following groups: 

* [String datatype features](#string-datatype)
* [Integer datatype features](#integer-datatype)
* [Link datatype features](#link-datatype)
* [Configuration data](featuresbydatatype.md#configuration-data)

## String datatype

Name | Feature group | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)| All material after a word | ` ` `.` `,— ` `.]] `
[before](before.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | All material before a word | `—`  `[[`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`group`](featuresbynodetype.md#group-nodes) [`wg`](featuresbynodetype.md#wg-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes)  [`book`](featuresbynodetype.md#book-notes) | Full book name | `Matthew` ... `Revelation`
[book_short](book_short.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Short book name | `MAT` `MAR` ... `REV`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[domain](domain.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Lexical domain according to SDBG | `092004`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)| English gloss | `faith`
[gender](gender.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)  | Gramatical gender | `masculine` `feminine` `neuter`
[nodeId](nodeId.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) | Node ID | `n56001015007`
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Lexical lemma (cf. BDAG) |
[ln](ln.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Louw-Nida lexical classification | `93.169a`
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) |Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [domain](domain.md#start) | Morphological tag | `V-AAI-3S` `N-GSF`
[normalized](normalized.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)  | Surface word stripped of punctations |
[number](number.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical number | `singular` `plural`
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features)| [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical person | `first` `second` `third`
[punctuation](punctuation.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) |[`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | Punctuation after a word | ` ` `.`
[junction](junction.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) |Junction information | `coordinate` `subordinate`
[roleclausedistance](roleclausedistance.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | distance to wg describing word function | `1` `3`
[sp](sp.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech | `det` `adv` `prep`
[sp_full](sp_full.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech (full) | `conjunction` `pronoun`
[strongs](strongs.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Strongs number | `5547`
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features)| [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical tense of the verb | `present` `aorist`
[text](text.md#start) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[type](type.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text (in unicode) | `λόγος`
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features)| [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical voice of the verb | `active` `passive`
[wgrolelong](wgrolelong.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role (full)| 
[wgrule](wgrule.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup rule | 
[wgtype](wgtype.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup type | `Verbless` `VerbElided`
[wordrole](wordrole.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Synctactic role of word | `s` `o` `adv` `aux` 
[wordtranslit](wordtranslit.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word without accents| `λογος`
[wgclass](wgclass.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup class | 
[wgrole](wgrole.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role | `ClCl` `DetNP` `Conj-CL` `S-V-O`

## Integer datatype

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[booknumber](booknumber.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | NT book number (Matthew=1, ... , Revelation=27) | `3` `8`
[chapter](chapter.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) | Chapter number inside book | `1` `2` ...
[monad](monad.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Monad (word order in corpus) | `1` .. `137779`
[orig_order](orig_order.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[verse](verse.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`verse`](featuresbynodetype.md#verse-nodes)| Verse number inside chapter | `1` `2`
[wgnum](wgnum.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup number | `1` `2`

## Link datatype

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[subj_ref](subj_ref.md#start) | [`Edge`](featuresbyfeaturetype.md#edge-features) | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |


## Configuration data

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[oslots](oslots.md) | [`Config`](featuresbyfeaturetype.md#config-features) | - | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Config`](featuresbyfeaturetype.md#config-features) |  - |  configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md) | [`Node`](featuresbyfeaturetype.md#node-features) |  | node type | `book` `verse` `clause` `phrase` `word`

