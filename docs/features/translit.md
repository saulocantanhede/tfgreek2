<a name="start"></a>
[`Transcription`](../transcription.md#start) | [`Features`](README.md#start) | [`Viewtypes`](../viewtypes.md#start) | [`Textformats`](../textformats.md#start) |  [`Syntaxtrees`](../syntaxtrees.md#start) | [`Tutorial`](../../tutorial/README.md#start) | [`Usecases`](../usecases/README.md#start) | [`About`](../about.md#start)

# Nestle 1904 GNT - Feature: translit

Feature group | Feature type | Data type | Available for node types | Used by viewtype
---  | --- | --- | --- | ---
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) | [`syntax-view`](../syntax-view.md#start) [`wg-view`](../wg-view.md#start) 

## Feature description

Transliteration of the Greek word surface text into latin characters.

This feature is also populated for `phrase` or `subphrase`, but only if they consist of just one `word` node.

## Feature values 

The following tables only show the first fifh entries with the highest frequency.

For [`word`](featuresbynodetype.md#word-nodes) nodes (used in [`syntax-view`](../syntax-view.md#start) and  [`wg-view`](../wg-view.md#start)):

Value	| Occurences
--- | ---
kai	| 8576
en	| 3152
o	| 3149
to | 2885
de | 2769

For [`subphrase`](featuresbynodetype.md#subphrase-nodes) nodes (used in [`wg-view`](../wg-view.md#start)):

Value	| Occurences
--- | ---
kai	| 8576
en	| 3152
o	| 3149
to | 2885
de | 2769

For [`phrase`](featuresbynodetype.md#phrase-nodes) nodes (used in [`wg-view`](../wg-view.md#start)):

Value	| Occurences
--- | ---
me |	976
estin |	865
auton	| 815
auto | 768
ouk	| 660

## Notes

This feature allows for easy writing of queries without the use of Greek characters. The following snippet provides an example:
```python
    logosQuery='''
    verse 
       word translit=logos
    '''
    logosResults=PLAY.search(logosQuery) # this will provide a list of tuples
    T.text(logosResults[0][0]) # print the Greek text related to the first node in the first tuple (which is a verse node)
```
The query returns 63 results. the first one is printed by the last statement:
`'ἔστω δὲ ὁ λόγος ὑμῶν ναὶ ναί,οὒ οὔ·τὸ δὲ περισσὸν τούτων ἐκ τοῦ πονηροῦ ἐστιν.'`

See also the following related features:
   * [after](after.md#start): All material found after a word.
   * [before](before.md#start): All material found before a word.
   * [criticalsign](criticalsign.md#start): Text-critical signs.
   * [punctuation](punctuation.md#start): Punctuations found after a word.
   * [text](text.md#start): Word without punctuations and text-critical signs.
   * [unaccent](unaccent.md#start): word without accents and diacritical markers.

The following image shows the relation between these features.

<img src="images/details_surface_features.png" width="400">

The following [text-formating options](../textformats.md#start) are defined in this dataset using this feature:
<pre>
  A.showFormats()
     format              level    template
     lex-orig-plain      word     {lemma}{punctuation}
     lex-translit-plain  word     {lextranslit}{punctuation}
     text-orig-full      word     {before}{text}{after}
     text-orig-plain     word     {text}{punctuation}
     text-translit-plain word     {translit}{punctuation}
     text-unaccent-plain word     {unaccent}{punctuation}
</pre>

## Source description

Calculated from the XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
