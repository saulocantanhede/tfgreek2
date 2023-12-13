# Feature: mood

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` |  [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Gramatical mood of a verb.

## Feature values 

mood | Comment | Frequency
--- | --- | ---
`imperative` | expresses a command | 1877
`indicative` | expresses an action being portrayed as real | 15617
`infinitive` | (pseudo mood) | 2285
`participle` | (pseudo mood) | 6653
`optative` | expresses something is possible | 69
`subjunctive` | expresses a probable or desired action | 1856
` ` | Any other wordtype | 109422

## Source description

Taken from (optional) XML attribute `mood` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
