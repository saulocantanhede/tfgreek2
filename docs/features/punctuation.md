# Feature: punctuation <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature includes either a regular space character or a punctuation mark followed by a regular space character, occurring after a word. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values 

Value | Description | Unicode codepoint | Frequency
---  |  --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  238522
`, ` | Comma |  [`&#44`](https://www.codetable.net/decimal/44)   | 18878
`. ` | Full Stop | [`&#46`](https://www.codetable.net/decimal/46) | 11408
`· ` | Midle Dot | [`&#183`](https://www.codetable.net/decimal/183) | 4710
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) | 1938
`,— ` |  | 36
`— ` |  | 14
`). ` | | 12
`.]] ` | | 8
`·— ` | | 8
etc.. | | another 11

## Notes

See also the following related features:
   * [after](after.md#start): All material found after a word.
   * [before](before.md#start): All material found before a word.
   * [criticalsign](criticalsign.md#start): Text-critical signs.
   * [text](text.md#start): Word without punctuations and text-critical signs.
   * [unicode](unicode.md#start): Unicode presentation including all material before and after word.

The following image shows the relation between these features.

<img src="images/details_surface_features.png" width="400" >

The following text-formating options are defined in this dataset using this feature:
<pre>
  A.showFormats()
     format           level    template
     text-orig-full   word     {before}{text}{after}
     text-orig-plain  word     {text}{punctuation}
</pre>

## Source description

Calculated from the from XML attribute `after` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*



