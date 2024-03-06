<a name="start"></a>
[`Transcription`](transcription.md#start) | [`Features`](features/README.md#start) | [`Viewtypes`](viewtypes.md#start) | `Textformats`| [`Syntaxtrees`](syntaxtrees.md#start) | [`Tutorial`](../tutorial/README.md#start) | [`Usecases`](usecases/README.md#start) |[`About`](about.md#start)

# Nestle 1904 GNT - Textformats 

Surface text related features:
   * [after](features/after.md#start): All material found after a word.
   * [before](features/before.md#start): All material found before a word.
   * [criticalsign](features/criticalsign.md#start): Text-critical signs.
   * [normalized](features/normalized.md#start): Normalized Greek text.
   * [punctuation](features/punctuation.md#start): Punctuations found after a word.
   * [text](features/text.md#start): Word without punctuations and text-critical signs.
   * [translit](features/translit.md#start): Transliteration of the word surface texts.
   * [unaccent](features/unaccent.md#start): word without accents and diacritical markers.
   * [unicode](features/unicode.md#start): Unicode presentation including all material before and after word.

The following image shows the relation between these features.

<img src="features/images/details_surface_features.png" width="400" >


The following text-formating options are defined in this dataset:

Format | Usage
--- | ---
lex-orig-plain | Lexemes of the Greek surface text 
lex-translit-plain | Transliteration of the lexemes of the Greek surface text 
text-orig-full | The Greek surface text in unicode including text-critical markers
text-orig-plain | The Greek surface text in unicode
text-translit-plain | Transliteration of the Greek surface text
text-unaccent-plain | The Greek surface text in unicode without accents

The template for each format can easily been checked using the following command:

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


## Example

This example illustrates how the different formats in this dataset affect the presentation of Mark 1:1.

```
# note: node 383782 is of type 'verse' and associated to Mark 1:1 
for formats in T.formats:
    print(f'fmt={formats}\t: {T.text(383782,formats)}')
fmt=lex-orig-plain       : ἀρχή ὁ εὐαγγέλιον Ἰησοῦς Χριστός υἱός θεός.
fmt=lex-translit-plain   : arkhe o euaggelion Iesous Khristos uios theos.
fmt=text-orig-full       : Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ).
fmt=text-orig-plain      : Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ.
fmt=text-translit-plain  : Arkhe tou euaggeliou Iesou Khristou Uiou Theou.
fmt=text-unaccent-plain  : Αρχη του ευαγγελιου Ιησου Χριστου Υιου Θεου.
```
