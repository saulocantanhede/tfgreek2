<a name="start"></a>
[<small>`Transcription`</small>](../transcription.md#start) | [<small>`Features`</small>](../features.md#start) | [<small>`Views`</small>](../views.md#start) | [<small>`Syntaxtrees`</small>](../syntaxtrees.md#start) | [<small>`Tutorial`</small>](../../tutorial/README.md#start) | [<small>`Usecases`</small>](../usecases/README.md#start) |[<small>`About`</small>](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT -  Feature: appositioncontainer

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes)

## Feature description 

This feature indicates if a wordgroup or phrase contains an apposition.

## Feature values 

For [`wg`](featuresbynodetype.md#wordgroup-nodes) nodes:
Value | Description | Frequency
---  | --- | --- 
` ` | this entity has no appositioncontainer | -
`1` | this entity has an appositioncontainer | 1908

For [`phrase`](featuresbynodetype.md#phrase-nodes) nodes:
Value | Description | Frequency
---  | --- | --- 
` ` | this entity has no appositioncontainer | -
`1` | this entity has an appositioncontainer | 715

For [`subphrase`](featuresbynodetype.md#subphrase-nodes) nodes:
Value | Description | Frequency
---  | --- | --- 
` ` | this entity has no appositioncontainer | -
`1` | this entity has an appositioncontainer | 1908


## Note

The following image presents a nested apposition demonstrating this feature and the related feature [rela](rela.md#readme).

<img src="images/appositioncontainer.png" width="600">

## Source description

Taken from (optional) XML attribute `appositioncontainer` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
