<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Views`](../views.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) |[`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: lemma

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Lexical lemma according to Bible Dictionary of Ancient Greek (BDAG) and/or ANLEX by Friberg, Friberg, and Miller. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Notes

When using the [Bible Online Learner](http://www.dadel.org/) as an aid in exploring text and creating Text-Fabric queries, it is advisable to use the [bol_lemma](bol_lemma.md#start) feature instead of this one to circumvent potential issues arising from a slightly different handling of Unicode codepoints.

## Source description

Taken from XML attribute `lemma` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
