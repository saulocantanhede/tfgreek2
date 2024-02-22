<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: normalized

Feature group | Feature type | Data type | Available for node types | Used in viewtypes
---  | --- | --- | --- | ---
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start)

## Feature description

Normalized Greek text (changed accents and diacritics to their standard forms). Also trailing punctuations are removed.

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Notes

See also the following related features:

   * [text](text.md#start): Word without punctuations and text-critical signs.
   * [unicode](unicode.md#start): Word as it appears in the text (in unicode)


## Source description

Taken from XML attribute `normalized` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

