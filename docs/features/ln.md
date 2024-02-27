<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: ln 

Feature group | Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Semantic`](featuresbygroup.md#semantic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start)

## Feature description

Louw-Nida lexical classification of the semantic domain. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values:

ln (this feature) | Comment | Frequency
--- | --- | ---
xx.yy  | one or more entries for the Louw-Nida references | 126756
'' | Empty | 11023

## Interpreting the data

The Louw-Nida Lexical Classification, by Johannes P. Louw and Eugene A. Nida, is a system for organizing New Testament Greek vocabulary. It categorizes words into 93 semantic domains based on meaning and context, emphasizing the importance of context in understanding word nuances. Lookup of values for feature ln can be performed in [Louw-Nida Lexicon](https://www.laparola.net/greco/louwnida.php).

## Notes

See also related feature [domain](domain.md#readme) (Lexical Domain).

## Source description

Taken from XML attribute `domain` of tag `w` (word). The word sense data for this feature was compiled by the United Bible Societies MARBLE project. See [Macula-Greek Licence](https://github.com/Clear-Bible/macula-greek/blob/main/LICENSE.md).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
