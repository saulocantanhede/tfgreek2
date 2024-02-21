<a name="start"></a>
[<small>`Transcription`</small>](../transcription.md#start) | [<small>`Features`</small>](../features.md#start) | [<small>`Views`</small>](../views.md#start) | [<small>`Syntaxtrees`</small>](../syntaxtrees.md#start) | [<small>`Tutorial`</small>](../../tutorial/README.md#start) | [<small>`Usecases`</small>](../usecases/README.md#start) |[<small>`About`</small>](../about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT -  Feature: before

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description 

This feature provides all the material pressent before a word. 

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values 

For [`word`](featuresbynodetype.md#word-nodes) nodes:
Value | Description | Unicode codepoint | Frequency
--- |  --- | --- | ---
`—` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 16
`(` |	Left Parenthesis | [`&#40`](https://www.codetable.net/decimal/40)| 10
`[[` | Left Square Bracket (2x) | [`&#91`](https://www.codetable.net/decimal/91) (2x) | 7
`[` |	Left Square Bracket | [`&#91`](https://www.codetable.net/decimal/91) | 1

For [`subphrase`](featuresbynodetype.md#subphrase-nodes) nodes:
Value | Description | Unicode codepoint | Frequency
--- |  --- | --- | ---
`—` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 16
`(` |	Left Parenthesis | [`&#40`](https://www.codetable.net/decimal/40)| 10
`[[` | Left Square Bracket (2x) | [`&#91`](https://www.codetable.net/decimal/91) (2x) | 7
`[` |	Left Square Bracket | [`&#91`](https://www.codetable.net/decimal/91) | 1

For [`phrase`](featuresbynodetype.md#phrase-nodes) nodes:
Value | Description | Unicode codepoint | Frequency
--- |  --- | --- | ---
`—` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 8
`(` |	Left Parenthesis | [`&#40`](https://www.codetable.net/decimal/40)| 6
`[[` | Left Square Bracket (2x) | [`&#91`](https://www.codetable.net/decimal/91) (2x) | 2

## Notes

See also the following related features:
   * [after](after.md#start): All material found after a word.
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

Determined from the value of XML tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

