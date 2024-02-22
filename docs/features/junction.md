<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: junction

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`phrase`] | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) (featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature indicates details coordinating and subordinating clauses.

## Feature values 

value | description | Frequency<sup>1</sup>
---  | --- | --- 
`coordinate` | coordinate | 18734
`subordinate` |  subordinate | 17108
` `  | empty | 

<sup>1</sup> Frequency figures are listed for `wg` nodes only. 

## Note
See also the related feature [crule](crule.md).

## Source description

Taken from (optional) XML attribute `junction` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
