<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Views`](../views.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) |[`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: voice

Feature group |Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) 
 
## Feature description

Gramatical voice of a verb. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values

Value | Description | Frequency<sup>1</sup>
--- | --- | ---
active | Sentences subject is agent of the verb's action | 20742
middle | Sentences subject is both agent and affected by the verb's action | 2408
middlePassive | | 1714
passive | The subject of the verb is being acted upon | 3493
'' | Empty for wordtypes other than verbs | 109422

<sup>1</sup> Frequency figures are listed for word nodes only. 

## Notes

The BOL dataset contians additional details.

## Source description

Taken from XML attribute `voice` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
