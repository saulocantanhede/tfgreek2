# Feature: criticalsign

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

This feature provides the text-critical marks pressent before or after a word.

## Feature values 

Value | Description | Unicode codepoint | Frequency
--- |  --- | --- | ---
`—` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 50
`(` |	Left Parenthesis | [`&#40`](https://www.codetable.net/decimal/40)| 22
`)` |	Right Parenthesis | [`&#41`](https://www.codetable.net/decimal/41)| 22
`[[` | Left Square Bracket (2x) | [`&#91`](https://www.codetable.net/decimal/91) (2x) | 14
`]]` | Right Square Bracket (2x) | [`&#93`](https://www.codetable.net/decimal/91) (2x) | 14
`[` |	Left Square Bracket | [`&#91`](https://www.codetable.net/decimal/91) | 2
`]` |	Right Square Bracket | [`&#93`](https://www.codetable.net/decimal/93) | 2

## Notes

See also the following related features:
   * [after](after.md#start): spaces and punctuation after word
   * [before](before.md#start): critical signs before word
   * [punctuation](punctuation.md#start): punctuations

The following image shows the relation between these features.

<img src="images/details_surface_features.png" width="400" >

## Source description

Taken from XML of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
