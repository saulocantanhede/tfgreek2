# Feature: discontinuous <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

Set to 1 if the word is out of sequence in the XML source data in relation to the running text.  

## Feature values 

value | description | Frequency
---  | --- | --- 
` ` | no discontinuation | 
`1` |  discontinuation | 12068

## Source description

Taken from (optional) XML attribute `discontinuous` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
