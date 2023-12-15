# Feature: num <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | ---  | --- | --- 
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`book`](featuresbynodetype.md#book-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

Sequential number for node type.

## Feature values

For node type:
  * [`book`](featuresbynodetype.md#book-nodes): Sequence within the Greek New Testament corpus (Matthew=1, Mark=2, ..., Revelation=27)
  * [`chapter`](featuresbynodetype.md#chapter-nodes): Chapter number in book
  * [`phrase`](featuresbynodetype.md#phrase-nodes):
  * [`sentence`](featuresbynodetype.md#sentence-nodes): Sentence number within chapter
  * [`subphrase`](featuresbynodetype.md#subphrase-nodes):
  * [`word`](featuresbynodetype.md#word-nodes): Word numbered inside verse (?)

## Source description

Calculated.

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
