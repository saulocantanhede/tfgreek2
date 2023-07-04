# Feature: voice

Feature group |Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`w`](featuresbynodetype.md#word-nodes)

## Feature description

Verbal voice of the verb.

## Feature values

Value | Description | Frequency
--- | --- | ---
active | Sentences subject is agent of the verb's action | 20742
middle | Sentences subject is both agent and affected by the verb's action | 2408
middlePassive | | 1714
passive | The subject of the verb is being acted upon | 3493
'' | Empty for wordtypes other than verbs | 109422

## Notes

Planned for future version? active, middle, passive, middle_or_passive, middle_deponent, passive_deponent, middle_or_passive_deponent, impersonal_active, and no_voice. Possibly by just adding a feature 'deponent'?

## Source description

Taken from XML attribute `voice` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
