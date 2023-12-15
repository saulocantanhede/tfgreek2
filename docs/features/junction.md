# Feature: junction

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) clause [`sentence`](featuresbynodetype.md#sentence-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

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
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
