# Feature: nodeId

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`w`](featuresbynodetype.md#word-nodes)

## Feature description 
Node ID in the format like `n56001015007`.

```
The letter 'n' followe by a 11-digit unique id in the format

    BBCCCVVVWWW
    BB          => zero-padded book, NT starts at 40
      CCC       => zero-padded chapter
         VVV    => zero-padded verse
            WWW => zero-padded word index (instance within the verse)
```

## Source description

Taken from XML attribute `xml:id` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
