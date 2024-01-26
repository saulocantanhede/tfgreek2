# N1904 Text-Fabric Corpus Documentation

In Text-Fabric, a "feature" refers to attributes associated with nodes, which represent linguistic elements in the text, including words, word groups, sentences, and verses. These features contain additional information specific to these nodes, facilitating diverse linguistic analyses and data extraction.

The full featureset of this Text-Fabric dataset can be viewed by different grouping methods:
* [Grouped by feature type](features/featuresbyfeaturetype.md#start)
     * [`Node`](features/featuresbyfeaturetype.md#node-features): the fundamental units or entities in the data model.
     * [`Edge`](features/featuresbyfeaturetype.md#edge-features): relationships or links, establishing connections between nodes in the data model.
     * [`Config`](features/featuresbyfeaturetype.md#config-features): contains the configuration or settings that define the behavior and parameters of the data processing or analysis.
* [Grouped by feature group](features/featuresbygroup.md#start):
     * [`Grid`](features/featuresbygroup.md#grid-features): pertains to the arrangement and organization of the data.
     * [`Sectional`](features/featuresbygroup.md#sectional-features): encompasses attributes or elements related to divisions within the text.
     * [`Lexical`](features/featuresbygroup.md#lexical-features): focuses on aspects related to individual words, their meanings, and lexical properties.
     * [`Orthograpic`](features/featuresbygroup.md#Orthograpic-features): deals with features related to the visual representation of the text.
     * [`Textcritical features`](features/featuresbygroup.md#textcritical-features): deals with features related to textual critical issue.
     * [`Morphological`](features/featuresbygroup.md#morphological-features):  involves attributes that describe the internal structure and form of words.
     * [`Syntactic`](features/featuresbygroup.md#syntactic-features): covers properties related to the arrangement of words and phrases to form meaningful sentences and phrases. 
     * [`Relational`](features/featuresbygroup.md#relational-features):  encompasses attributes that describe various relationships or connections between elements in the text.
* [Grouped by node type](features/featuresbynodetype.md#start):
     * [`word`](features/featuresbynodetype.md#word-nodes): represents individual words in the text.
     * [`wg`](features/featuresbynodetype.md#wordgroup-nodes) (wordgroup): refers to a collection or grouping of words that form a cohesive unit. Each individual wordgroup node has an acompanying shadow node of one of the following types: 
         * [`subphrase`](features/featuresbynodetype.md#subphrase-nodes): Nodes pertaining to a subphrase unit.
         * [`phrase`](features/featuresbynodetype.md#phrase-nodes): Nodes pertaining to a phrase unit.
         * [`clause`](features/featuresbynodetype.md#clause-nodes): Nodes pertaining to a clause unit.
         * [`group`](features/featuresbynodetype.md#group-nodes): Nodes pertaining to a phrase unit.
     * [`sentence`](features/featuresbynodetype.md#sentence-nodes): represents individual sentences in the text.
     * [`verse`](features/featuresbynodetype.md#verse-nodes): pertains to divisions within a larger textual unit, specificaly the biblical verse.
     * [`chapter`](features/featuresbynodetype.md#chapter-nodes): divisions within the text that group related content together, specificaly the biblical chapter.
     * [`book`](features/featuresbynodetype.md#book-nodes): the highest-level division within the text, corresponding to a bible book.

# Example use-cases of this Text-Fabric dataset

The following are several use-case examples that demonstrate the utilization of the Text-Fabric dataset. While Text-Fabric,  which is implemented as a Python package, can be employed in any stand-alone Python script, it is commonly utilized from within a [Jupyter Notebook](https://jupyter.org) — an interactive web-based computational environment enabling users to create and share documents with live code, visualizations, and text, thus facilitating the inclusion of explanatory notes alongside queries and results obtained from Text-Fabric.

## Basic / general

* [Load Text-Fabric in Jupyter notebook](https://nbviewer.org/github/saulocantanhede/tfgreek2/blob/main/docs/usecases/load_text_fabric.ipynb)
