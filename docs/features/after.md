<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Views`](../views.md#start) | [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) |[`About`](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Feature: after

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) 

## Feature description 

This feature includes all material found after a word: regular space character,  punctuation marks followed by a regular space character, and text-critical markers. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values 

Value | Description | Unicode codepoint | Frequency<sup>1</sup>
---  |  --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  119261
`, ` | Comma | [`&#44`](https://www.codetable.net/decimal/44) & [`&#32`](https://www.codetable.net/decimal/32)   | 9439
`. ` | Full stop | [`&#46`](https://www.codetable.net/decimal/46) & [`&#32`](https://www.codetable.net/decimal/32)| 5704
`· ` | Midle dot | [`&#183`](https://www.codetable.net/decimal/183) & [`&#32`](https://www.codetable.net/decimal/32) | 2355
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) & [`&#32`](https://www.codetable.net/decimal/32) | 969
`,— ` | Comma, em dash & space | [`&#44`](https://www.codetable.net/decimal/44) & [`&#8212`](https://www.codetable.net/decimal/8212)  & [`&#32`](https://www.codetable.net/decimal/32) | 18
`— ` | Em dash & space | [`&#8212`](https://www.codetable.net/decimal/8212) & [`&#32`](https://www.codetable.net/decimal/32) | 7
`). ` | Closing round bracket, full stop & space | [`&#41`](https://www.codetable.net/decimal/41) & [`&#46`](https://www.codetable.net/decimal/46) & [`&#32`](https://www.codetable.net/decimal/32) | 6
`.]] ` | full stop & 2 Right Square Bracket | [`&#46`](https://www.codetable.net/decimal/46) & 2x [`&#93`](https://www.codetable.net/decimal/93)| 4
etc.. | various | various | another 15

<sup>1</sup> Frequency figures are listed for word nodes only. 

## Notes

See also the following related features:
   * [before](before.md#start): All material found before a word.
   * [criticalsign](criticalsign.md#start): Text-critical signs.
   * [punctuation](punctuation.md#start): Punctuations found after a word.
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

Taken from XML attribute `after` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

