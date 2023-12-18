# Feature: appositioncontainer <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature indicates if a wordgroup or phrase contains an apposition.

## Feature values 

Value | Description | Frequency
---  | --- | --- 
` ` | this entity has no appositioncontainer | -
`1` | this entity has an appositioncontainer | 3816

## Note

The following image presents a nested apposition demonstrating this feature and the related feature [rela](rela.md#readme).

<img src="images/appositioncontainer.png" width="600">

## Source description

Taken from (optional) XML attribute `appositioncontainer` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
