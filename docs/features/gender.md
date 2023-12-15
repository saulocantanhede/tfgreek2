# Feature: gender <a name="start"></a>

Feature group |Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Gramatical gender for wordtypes nouns, adjectives, pronouns, participles, and definite articles.

## Feature values

Value | Description | Frequency
--- | --- | --- 
feminine | grammatical gender is feminine | 18736
masculine | grammatical gender is masculine | 41486
neuter | grammatical gender is neuter | 13753
 '' | empty for any other wordtype | 63804

## Source description

Taken from XML attribute `gender` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
