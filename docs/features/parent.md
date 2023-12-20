# Feature: parent <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Relational`](featuresbygroup.md#relational-features) | [`Edge`](featuresbyfeaturetype.md#edge-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes)
 
## Feature description

Edge between a node and its parent node.

## Feature value

A node value.

## Notes

The following query demonstrates a typical use of this feature. Here the parent feature is used twice in order to make sure wg2 is child of wg1 and w1 is child of wg1:

<pre>
Query2 = '''
wg1:wg type=modifier-scope
  w1:word lemma=ἐλπίς
  wg2:wg rule=DetNP
wg2 -parent> wg1
w1 -parent> wg1
'''
Results = A.search(Query)
 0.24s 6 results</pre>

Part of the results is shown in the following image:

<img src="images/parent_query.png" width="650">






## Source description

Calculated.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

