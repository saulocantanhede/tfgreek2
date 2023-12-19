# Feature: subjref <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Edge`](featuresbyfeaturetype.md#edge-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Subject reference to one or more nodes.

## Feature values

`word` node values.

## Notes

The "Subject Reference" feature is implemented as an edge feature within the data structure. Its usage can be seen in the following example, where the feature is applied in a structured query. The following examples shows two nodes being reported:

<pre>
E.subjref.f(514)
  (524, 533)
</pre>

This snippet indicates that the node with identifier 514 has a subject reference connection to nodes 524 and 533.

To demonstrate the practical application of this feature, consider the following query example:

<pre>
SubQuery = '''
clause
  w1:word 
  w2:word 
  w1 -subjref> w2
'''
SubResults = PLAY.search(SubQuery)
  0.17s 7755 results
</pre>

This query illustrates how to retrieve relationships where one word (w1) has a subject reference to another word (w2).
One example syntactical tree:

<img src="images/subjref.png" width="600">

See also related feature [subjrefspec](subjrefspec.md#start).

## Source description

Based upon (optional) XML attribute `subjref` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
