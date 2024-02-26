<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: typ

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Syntactical`](featuresbygroup.md#syntactical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`group`](featuresbynodetype.md#group-nodes)  | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) 

## Feature description

This is XML attribute typ.

## Feature values

Frequency for nodetype `group`:

Value | Description | Frequency
---- | ---- | ---
conjuncted | |	8075
apposition | |	889

Frequency for nodetype `wg`:

Value | Description | Frequency
---- | ---- | ---
NP	|| 30911
PP	|| 11169
conjuncted	|| 8075
apposition	|| 889
VP	|| 207
AdjP ||	168
AdvP ||	166

Frequency for nodetype `phrase`:

Value | Description | Frequency
---- | ---- | ---
NP	|| 10935
PP	|| 9609
AdvP ||	154
AdjP ||	60
VP	|| 10

Frequency for nodetype `subphrase`:

Value | Description | Frequency
---- | ---- | ---
NP	|| 30911
PP	|| 11169
VP	|| 207
AdjP ||	168
AdvP || 166

## Source description

Taken from XML attribute `typ` of tag `w` (word) and tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

