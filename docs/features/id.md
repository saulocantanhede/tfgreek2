# Feature: id <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`relational`](featuresbygroup.md#relational-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) 

## Feature description

A uniqe identifier for each individual word in the corpus.

## Feature values

Id in the following format:

```
The letter 'n' followed by a 11-digit unique id in the format

    BBCCCVVVWWW
    BB          => zero-padded book, the first NT book (Matthew) starts at 40
      CCC       => zero-padded chapter
         VVV    => zero-padded verse
            WWW => zero-padded word index (instance within the verse)
```

## Source description
Taken from XML tag `xml:id` of `w` (word) node.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
