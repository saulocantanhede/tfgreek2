<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: gender

Feature group |Feature type | Data type | Available for node types | Used by viewtypes
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) 

## Feature description

Gramatical gender for wordtypes nouns, adjectives, pronouns, participles, and definite articles.

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values

Value | Description | Frequency<sup>1</sup>
--- | --- | --- 
feminine | grammatical gender is feminine | 18736
masculine | grammatical gender is masculine | 41486
neuter | grammatical gender is neuter | 13753
 '' | empty for any other wordtype | 63804
 
<sup>1</sup> Frequency figures are listed for `word` nodes only. 

## Source description

Taken from XML attribute `gender` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
