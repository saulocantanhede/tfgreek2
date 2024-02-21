<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Views`](../views.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) |[`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: role

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Syntactical`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`wg`](featuresbynodetype.md#wordgroup-nodes)  [`group`](featuresbynodetype.md#group-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`clause`](featuresbynodetype.md#clause-nodes)  [`phrase`](featuresbynodetype.md#phrase-nodes) 

## Feature description

Syntactic role of word or wordgroup.

## Feature values

For `word` or `wg` (wordgroup) nodes:

Value | Description | Frequency
--- | --- | ---
o | Object | 26988
s | Subject | 22336
adv | Adverbial | 43154
v | Verb | 50344
p | Predicate | 7348
io | Indirect object | 5316
vc | Verbal Copula  | 5186
apposition | Apposition | 4878
aux | Auxiliar | 2112
o2 | Second object | 718

## Mapping between role and function feature

feature `role` ([`wg-view`](../wg-view.md#start)) | feature [`function`](function.md#start) [`syntax-view`](../syntax-view.md#start)
---|---
io | Cmpl
o | Objc
o2 | Objc
p | PreD
s | Subj
vc (wg nodes) | Pred
v (word nodes) | Pred
apposition | Appo

## Note
See also the description in [MACULA Greek Treebank for the Nestle 1904 Greek New Testament.pdf](https://nbviewer.org/github/biblicalhumanities/greek-new-testament/blob/master/syntax-trees/nestle1904/doc/Nestle%201904%20Treebank%20Documentation.pdf) on page 4 and 5 (section 2.2. Syntactic Categories at Word Level: Part of Speech Labels).

## Source description

From the XML ...

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
