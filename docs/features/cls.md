# Feature: cls <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`clause`](featuresbynodetype.md#clause-nodes)  [`wg`](featuresbynodetype.md#wordgroup-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

For `word` nodes: Part of Speech (PoS). For `wg` (wordgroup) nodes: phrase catagory.

## Feature values

For word nodes:

value | Part of Speech | frequency
--- | --- | ---
adj | adjective | 8452
adv | adverb | 6147
conj | conjunction | 18227
det | determiner | 19786
intj | interjection | 15
noun | noun | 28455
num | numeral | 476
prep | preposition | 10914
ptcl | particle | 773
pron | pronoun | 16177
verb | verb | 28357

For WordGroup nodes:

Value | Phrase Category | frequency
--- | --- | ---
adjp | adjectival phrase | 168
advp | adverbial phrase | 166
np | noun phrase | 30911
nump | numeral phrase | 7
pp | prepositional phrase | 11169
vp | verbal phrase | 207
adv | ?  | 7
cl | ? | 30152
conj | ? | 1


## Note
See also the description in [MACULA Greek Treebank for the Nestle 1904 Greek New Testament.pdf](https://nbviewer.org/github/biblicalhumanities/greek-new-testament/blob/master/syntax-trees/nestle1904/doc/Nestle%201904%20Treebank%20Documentation.pdf) on page 4 and 5 (section 2.2. Syntactic Categories at Word Level: Part of Speech Labels).

## Source description

For word nodes: taken from XML attribute `class` of tag `w` (word).

For wg nodes: taken from XML attribute `class` of tag `wg` (wordgroup)

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
