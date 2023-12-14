# Feature: after

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature includes either a regular space character or a punctuation mark followed by a regular space character, occurring after a word.

## Feature values 

Value | Description | Unicode codepoint | Frequency
---  |  --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  119272
`, ` | Comma |  [`&#44`](https://www.codetable.net/decimal/44)   | 9441
`. ` | Full Stop | [`&#46`](https://www.codetable.net/decimal/46) | 5712
`· ` | Midle Dot | [`&#183`](https://www.codetable.net/decimal/183) | 2355
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) | 969
`— ` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 30

## Notes

See also the following related features:
   * [before](before.md#start): critical signs before word
   * [criticalsign](criticalsign.md#start): text-critical signs
   * [punctuation](punctuation.md#start): punctuations

The following image shows the relation between these features.

<img src="images/details_surface_features.png" width="400" >

## Source description

Taken from XML attribute `after` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*

