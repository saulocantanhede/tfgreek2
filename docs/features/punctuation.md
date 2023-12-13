# Feature: punctuation

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`w`](featuresbynodetype.md#word-nodes)

## Feature description 

This feature includes either a regular space character or a punctuation mark followed by a regular space character, occurring after a word.

## Feature values 

Value | Description | Unicode codepoint | Frequency
---  |  --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  238528
`, ` | Comma |  [`&#44`](https://www.codetable.net/decimal/44)   | 18924
`. ` | Full Stop | [`&#46`](https://www.codetable.net/decimal/46) | 11434
`· ` | Midle Dot | [`&#183`](https://www.codetable.net/decimal/183) | 4718
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) | 1942


## Source description

Calculated from the from XML attribute `after` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*


