<a name="start"></a>
<small>`Transcription`</small> | [<small>`Features`</small>](features.md#start) | [<small>`Views`</small>](views.md#start) | [<small>`Syntaxtrees`</small>](syntaxtrees.md#start) | [<small>`Tutorial`</small>](../tutorial/README.md#start) | [<small>`Usecases`</small>](usecases/README.md#start) |[<small>`About`</small>](about.md#start)
---  | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Corpus Transcription

This page provides a high level overview of how the Nestle 1904 GNT corpus has been transcipted into a Text-Fabric dataset. 

## The concept 'features' in Text-Fabric


## Views

The concept of [views](views.md#start) is important to this dataset. This database offers the users two distinct views to represent the syntax trees:
   * [Syntactic view](syntactic-view.md#start) (default): present syntax tree in linguistic terms like phrases and clauses.
   * [WordGroup view](wg-view.md#start): present syntax tree in agnostic terms like word groups.

## Features 

In Text-Fabric, a "feature" refers to attributes associated with nodes, which represent linguistic elements in the text, including words, word groups, sentences, and verses. These features contain additional information specific to these nodes, facilitating diverse linguistic analyses and data extraction.
Text-Fabric, true to its name, implements the concepts of 'warp' and 'weft', inspired by textile weaving, to represent its data. The 'warp' denotes the foundational structured data, encompassing linguistic annotations like words, and phrases, while the 'weft' refers to the additional layers of information, known as features. These features encompass linguistic data, annotations, and metadata, seamlessly woven into the 'warp' data, resulting in a clear separation between structure and content. This approach enables Text-Fabric to efficiently handle complex linguistic datasets with versatility.

Feature descriptions listed by different groupings:
* [Grouped by feature group](features/featuresbygroup.md#start): e.g., [`Orthographic`](features/featuresbygroup.md#orthograpic-features), [`Syntactic`](features/featuresbygroup.md#syntactic-features).
* [Grouped by node type](features/featuresbynodetype.md#start): e.g., [`word`](features/featuresbynodetype.md#word-nodes), [`clause`](features/featuresbynodetype.md#clause-nodes).
* [Grouped by data type](features/featuresbydatatype.md#start): e.g., [`str`](features/featuresbydatatype.md#string-datatype), [`int`](features/featuresbydatatype.md#integer-datatype).
* [Grouped by feature type](features/featuresbyfeaturetype.md#start): e.g., [`node`](features/featuresbyfeaturetype.md#node-features), [`edge`](features/featuresbyfeaturetype.md#edge-features).

## Example use-cases of this Text-Fabric dataset

The following are several use-case examples that demonstrate the utilization of the Text-Fabric dataset. While Text-Fabric,  which is implemented as a Python package, can be employed in any stand-alone Python script, it is commonly utilized from within a [Jupyter Notebook](https://jupyter.org) — an interactive web-based computational environment enabling users to create and share documents with live code, visualizations, and text, thus facilitating the inclusion of explanatory notes alongside queries and results obtained from Text-Fabric.

### Basic / general

* [Load Text-Fabric in Jupyter notebook](https://nbviewer.org/github/saulocantanhede/tfgreek2/blob/main/docs/usecases/load_text_fabric.ipynb)
