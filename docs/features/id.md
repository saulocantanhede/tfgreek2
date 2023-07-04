# Feature: id

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`relational`](featuresbygroup.md#relational-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`w`](wordnodefeatures.md#readme)

## Feature description

```
The letter 'n' followe by a 11-digit unique id in the format

    BBCCCVVVWWW
    BB          => zero-padded book, NT starts at 40
      CCC       => zero-padded chapter
         VVV    => zero-padded verse
            WWW => zero-padded word index (instance within the verse)
```

## Source description
Taken from XML tag `xml:id` of `w` (word) node.

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
