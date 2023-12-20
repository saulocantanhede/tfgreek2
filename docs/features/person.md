# Feature: person <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Gramatical person of a verb.

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values

Value | Description | Frequency
--- | --- | ---
first | First person (either singular or plural) | 2943
second | Second person (either singular or plural) | 3729
third | Third person (either singular or plural) | 12747
'' | Empty for any wordtypes other than verb | 118360

## Note

See also related feature [number](number.md).

## Source description

Taken from XML attribute `person` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

