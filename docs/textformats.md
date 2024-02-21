<a name="start"></a>
[<small>`Transcription`</small>](transcription.md#start) | [<small>`Features`</small>](features.md#start) | [<small>`Views`</small>](views.md#start) | <small>`Textformats`</small>| [<small>`Syntaxtrees`</small>](syntaxtrees.md#start) | [<small>`Tutorial`</small>](../tutorial/README.md#start) | [<small>`Usecases`</small>](usecases/README.md#start) |[<small>`About`</small>](about.md#start)
---  | --- | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Textformats 

Surface text related features:
   * [before](features/before.md#start): All material found before a word.
   * [criticalsign](features/criticalsign.md#start): Text-critical signs.
   * [punctuation](features/punctuation.md#start): Punctuations found after a word.
   * [text](features/text.md#start): Word without punctuations and text-critical signs.
   * [unicode](features/unicode.md#start): Unicode presentation including all material before and after word.
The following image shows the relation between these features.

<img src="features/images/details_surface_features.png" width="400" >


The following text-formating options are defined in this dataset:
<pre>
  A.showFormats()
     format           level    template
     text-orig-full   word     {before}{text}{after}
     text-orig-plain  word     {text}{punctuation}
</pre>

need to add something like (this is from N1904LFT):
## Example
```
for formats in T.formats:
    print(f'fmt={formats}\t: {T.text(139200,formats)}')
fmt=text-critical	: Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
fmt=text-normalized	: Ἀρχή τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
fmt=text-orig-full	: Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
fmt=text-transliterated	: Arkhe tou euaggeliou Iesou Khristou Uiou Theou. 
fmt=text-unaccented	: Αρχη του ευαγγελιου Ιησου Χριστου Υιου Θεου.
```
