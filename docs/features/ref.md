# Feature: ref <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes)  [`phrase`](featuresbynodetype.md#phrase-notes)

## Feature description

Unique identifier of a word inside the New Testament corpus.
This feature is populated for `phrase` and `subphrase` only in case these contain only one `word`.

## Feature values

A compound string indicating book (following the format of feature [book-short](book_short.md#start)), chapter, verse and sequence number of the word *inside the verse* according to following format:

<pre>
  MAT 1:2!11
</pre>

From this feature value the word sequence number inside the verse can be easily obtained by means of following Python code:
<pre>
ref = "MAT 1:2!11"
print ('word sequence number: ', ref.split("!")[1])
word sequence number:  11
</pre>


## Source description

Based upon XML attribute `ref` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
