
# Feature: framespec <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Semantic`](featuresbygroup.md#semantic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Reference to the [id](id.md#start) of subject, object or idirect object. 

This feature is populated for most verbs (24690 out of 24767), with the addition of a small number of references for other wordtypes.  It's functional equivalent edge feature is [frame](frame.md#start).

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values

This feature contains one or more refernces to [`id`](id.md#start)'s,  like in following example:

```
A0:n63001005005;n63001001007 A1:n63001010014
```
The labels can be decoded using the following table.

Value | Description | Frequency
---|---|---
A0 | Agent or subject of the action | 25654
A1 | Direct object or the entity directly affected by the action | 15570
A2 | Indirect object or secondary entity affected by the action | 2577
AA2 | Adverbial roles in a sentence | 92

The values behind these identifires are in the following format:

```
An 'n' followed by a 11-digit unique id in the format
    BBCCCVVVWWW
    BB          => zero-padded book, NT starts at 40
      CCC       => zero-padded chapter
         VVV    => zero-padded verse
            WWW => zero-padded word index (instance within the verse)
```

## Notes

The following syntactical graphs from Matthew 1:2 and 1:20 serve as demonstration of this feature:

<img src="images/framespecA0A1.png" width="550">
<img src="images/framespecA0A2.png" width="550">

See also the following related features:
   * [frame](frame.md#start): Edge feature that links nodes that are part of the frame; labelled as A0, A1 etc.
   * [id](id.md#start): A uniqe identifier for each individual word in the corpus.
   * [referent](referent.md#start): referent.
   * [subjrefspec](subjrefspec.md#start): subjrefspec.

## Source description

Taken from (optional) XML attribute `frame` of tag `w` (word). Annotation data originates from [Clear Bible](https://github.com/Clear-Bible/macula-greek/tree/main/sources/Clear/annotations). Annotation data originates from [Clear Bible](https://github.com/Clear-Bible/macula-greek/tree/main/sources/Clear/annotations).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
