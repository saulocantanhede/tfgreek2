<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: ref

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes)  [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start)

## Feature description

Unique identifier of a word inside the New Testament corpus.

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values

A compound string indicating book (following the format of feature [bookshort](bookshort.md#start)), chapter, verse and sequence number of the word *inside the verse* according to following format:

<pre>
  MAT 1:2!11
</pre>

From this feature value the word sequence number inside the verse can be easily obtained by means of following Python code:
<pre>
ref = "MAT 1:2!11"
print ('word sequence number: ', ref.split("!")[1])
word sequence number:  11
</pre>

## Notes

This first three characters of this feature value are identical to feature [book_short](book_short.md#start).

## Source description

Based upon XML attribute `ref` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
