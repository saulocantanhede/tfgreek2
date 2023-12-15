# Feature: before <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature provides all the material pressent before a word.

## Feature values 

Value | Description | Unicode codepoint | Frequency
--- |  --- | --- | ---
`—` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 32
`(` |	Left Parenthesis | [`&#40`](https://www.codetable.net/decimal/40)| 20
`[[` | Left Square Bracket (2x) | [`&#91`](https://www.codetable.net/decimal/91) (2x) | 14
`[` |	Left Square Bracket | [`&#91`](https://www.codetable.net/decimal/91) | 2

## Notes

See also the following related features:
   * [after](after.md#start): All material found after a word.
   * [criticalsign](criticalsign.md#start): Text-critical signs.
   * [punctuation](punctuation.md#start): Punctuations found after a word.
   * [text](text.md#start): Word without punctuations and text-critical signs.
   * [unicode](unicode.md#start): Unicode presentation including all material before and after word.

The following image shows the relation between these features.

<img src="images/details_surface_features.png" width="400" >

## Source description

Taken from XML of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

