# Feature: type

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`w`](featuresbynodetype.md#word-nodes)
[`Syntactical`](featuresbygroup.md#syntactical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`wg`](featuresbynodetype.md#wordgroup-nodes)

## Feature description

For `w` (word) nodes: Gramatical type of noun or pronoun. For `wg`(wordgroup) nodes: syntactical type.

## Feature values

For `w` (word) nodes:

Value | Description | Frequency
---- | ---- | ---
adverbial |  | 3
common | objects | 23644
demonstrative | Indicate a specific object ([examples](https://ugg.readthedocs.io/en/latest/determiner_demonstrative.html)) | 1722
indefinite | | 552
interrogative |  Introduces a question ([examples](https://ugg.readthedocs.io/en/latest/determiner_interrogative.html)) | 633
personal | Pronoun designating a person (e.g. εγώ, εσύ, etc.) | 11521
possessive | | 70
proper | Name of a person, place, thing, etc. | 4639
relative |  | 1674
'' | Empty for wordtypes other than noun or pronoun | 93321

For `wg` (wordgroup) nodes:

Value | Description | Frequency
---- | ---- | ---
apposition-group | | 891
conjuncted-wg | | 8075
group | | 4957 
modifier-clause-scope | | 1712
modifier-scope | | 29645x 
wrapper-clause-scope | | 12166 
wrapper-scope	| | 11264 

## Source description

Taken from XML attribute `type` of tag `w` (word) and tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
