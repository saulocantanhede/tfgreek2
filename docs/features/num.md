<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: num

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | ---  | --- | --- | ---
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`book`](featuresbynodetype.md#book-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`wg`](featuresbynodetype.md#wordgroup-nodes) [`clause`](featuresbynodetype.md#clause-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start)

## Feature description 

Sequential number for node type.

## Feature values

For node type:
  * [`book`](featuresbynodetype.md#book-nodes): Sequence within the Greek New Testament corpus (Matthew=1, Mark=2, ..., Revelation=27)
  * [`chapter`](featuresbynodetype.md#chapter-nodes): Chapter number in book.
  * [`phrase`](featuresbynodetype.md#phrase-nodes):
  * [`sentence`](featuresbynodetype.md#sentence-nodes): Sentence number within chapter.
  * [`subphrase`](featuresbynodetype.md#subphrase-nodes):
  * [`word`](featuresbynodetype.md#word-nodes): Word numbered inside verse.

## Source description

Calculated (not in source xml).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

