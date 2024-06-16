<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: crule

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) 

## Feature description

clause rule (from xml attribute rule). This can be assigned to a `wg`, `clause` or `sentence` node.

## Feature values

Frequency for nodetype `sentence`:

value | explanation | Frequency
--- | --- | ---
ClCl | subordinate clause follows the main clause | 619
‎ClCl2 | subordinate clause precedes the main clause | 219

Frequency for nodetype `clause`:

value | explanation | Frequency
--- | --- | ---
ClCl | subordinate clause follows the main clause | 3689
‎ClCl2 | subordinate clause precedes the main clause | 1031

Frequency for nodetype `wg`:

value | explanation | Frequency
--- | --- | ---
ClCl | subordinate clause follows the main clause | 4308
‎ClCl2 | subordinate clause precedes the main clause | 1250

## Note

See also the related feature [junction](junction.md#readme).

## Source description

Taken from (optional) XML attribute `rule` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
