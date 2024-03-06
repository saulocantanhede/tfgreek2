<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: trans

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) 

## Feature description

English translation based upon the [Berean Interlinear Bible](https://berean.bible/) offering a word-for-word translation of the Greek text, focusing on a direct correspondence between Greek and English words, while also making adjustments for English grammar and punctuation to enhance readability. It prioritizes literal accuracy over idiomatic or contextual fluency. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.
## Notes

See also the related feature [gloss](gloss.md#start) which contains the Enlgish translation of the lexeme.

## Source description

Taken from XML attribute `gloss` of tag `w` (word). 

The source of this data is the [Berean Interlinear Bible](https://interlinearbible.com/). The Berean Bible and Majority Bible texts are officially placed into the public domain as of April 30, 2023.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
