# Feature: after

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature includes all material found after a word: regular space character,  punctuation marks followed by a regular space character, and text-critical markers. 

## Feature values 

Value | Description | Unicode codepoint | Frequency
---  |  --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  238522
`, ` | Comma | [`&#44`](https://www.codetable.net/decimal/44) & [`&#32`](https://www.codetable.net/decimal/32)   | 18878
`. ` | Full Stop | [`&#46`](https://www.codetable.net/decimal/46) & [`&#32`](https://www.codetable.net/decimal/32)| 11408
`· ` | Midle Dot | [`&#183`](https://www.codetable.net/decimal/183) & [`&#32`](https://www.codetable.net/decimal/32) | 4710
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) & [`&#32`](https://www.codetable.net/decimal/32) | 1938
`,— ` | Comma, Em Dash & Space | [`&#44`](https://www.codetable.net/decimal/44) & [`&#8212`](https://www.codetable.net/decimal/8212)  & [`&#32`](https://www.codetable.net/decimal/32) |  36
`— ` | Em Dash & Space | [`&#8212`](https://www.codetable.net/decimal/8212) + [`&#32`](https://www.codetable.net/decimal/32) | 14
`). ` | | | 12
`.]] ` | | | 8
`·— ` | | | 8
etc.. | various | various | another 11

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

