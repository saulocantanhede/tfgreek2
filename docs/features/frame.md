# Feature: frame  <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Relational`](featuresbygroup.md#relational-features) | [`Edge`](featuresbyfeaturetype.md#edge-features) | [`string`](featuresbydatatype.md#string-datatype)  |  [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Edge feature that links nodes that are part of the frame; labelled as A0, A1 or A2. 

## Feature values:

In this:

   * A0 = reference(s) to a subject.
   * A1 = reference(s) to an object.
   * A2 = reference(s) to the indirect object

## Note

The following image shows the query that will return the node ids of the verb and the its indirect object.

<img src="images/indirectobjectquery.png" width="600">

The following image shows the first returned clause (from Matthew 1:18):

<img src="images/indirectobjecttree.png" width="600">

See also related node feature [framespec](framespec.md#start).

## Source description

Based on (optional) XML attribute `frame` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
