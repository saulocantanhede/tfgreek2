# Feature: gloss <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

English gloss based upon the [Berean Interlinear Bible](https://berean.bible/) offering a word-for-word translation of the Greek text, focusing on a direct correspondence between Greek and English words, while also making adjustments for English grammar and punctuation to enhance readability. It prioritizes literal accuracy over idiomatic or contextual fluency. This feature is also populated for `phrase` or `subphrase` only in case these contain just one `word`.

## Source description

Taken from XML attribute `gloss` of tag `w` (word). The source of this data is the [Berean Interlinear Bible](https://interlinearbible.com/). The Berean Bible and Majority Bible texts are officially placed into the public domain as of April 30, 2023.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
