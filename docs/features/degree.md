# Feature: degree

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description
Grammatical degree of an comparative or superlative adjective.

## Feature values

Value | Description | Frequency
--- | --- | ---
comparitative | Comparitative adjective | 626
superlative | Superlative adjective | 400
'' | Empty for any other adjectives or other wordtypes | -

## Source description

Taken from (optional) XML attribute `degree` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
