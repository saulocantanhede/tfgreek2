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
