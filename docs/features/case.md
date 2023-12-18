# Feature: case <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description
Gramatical case for wordtypes noun, pronoun, adjective, article, or participle. This feature is also populated for `phrase` or `subphrase` only in case these contain just one `word`.

## Feature values

case | explanation | Frequency
--- | --- | ---
accusative | Generaly indicating the direct object of a verb | 23031
dative | Generaly indicating indirect object of a verb | 12126
genitive | Generaly indicating possesion | 19515
nominative | Generaly indicating the subject | 24197
vocative | Adressee of speech | 649
'' | empty for any other word type | 58261

## Source description

Taken from XML attribute `case` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

