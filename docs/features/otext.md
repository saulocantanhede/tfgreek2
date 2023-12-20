# Feature: otext

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Grid`](featuresbygroup.md#grid-features) | [`Config`](featuresbyfeaturetype.md#config-features) | Textformatting and corpus segmenting configuration | Not applicable

## Feature description

This feature does not contain node specific data, but contains information that tells Text-Fabric how to produce text strings for slots and the structure of the corpus.

## Notes 
The defined text-formating options for this dataset are:
<pre>
  A.showFormats()
     format           level    template
     text-orig-full   word     {before}{text}{after}
     text-orig-plain  word     {text}{punctuation}
</pre>

This feature also declares  which node type and feature correspond with which section level. This information is used to format the output of functions like [T.sectionFromNode(node)](https://annotation.github.io/text-fabric/tf/cheatsheet.html#sections). In this dataset section structure is the three level book, chapter, and verse division of the material.

## Source description

Defined during creation of the  dataset.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

