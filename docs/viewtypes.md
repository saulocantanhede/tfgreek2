<a name="start"></a>
[`Transcription`](transcription.md#start) | [`Features`](features/README.md#start) | `Viewtypes` | [`Textformats`](textformats.md#start) | [`Syntaxtrees`](syntaxtrees.md#start) | [`Tutorial`](../tutorial/README.md#start) | [`Usecases`](usecases/README.md#start) |[`About`](about.md#start)
---  | --- | --- | --- | --- | --- | --- | ---

# Nestle 1904 GNT - Viewtypes

## The view types

This database offers users two distinct views to represent the syntax trees. The relation between node types and view types is shown in the following table.

Viewtypes | Description | Invocation | Associated node types | 
--- | --- | --- | ---
[`wg-view`](wg-view.md#start) | Display syntax tree in agnostic terms like word groups | A.Viewtype('wg') |  [`wg`](features/featuresbynodetype.md#wordgroup-nodes) 
[`syntax-view`](syntax-view.md#start) | Display syntax tree in linguistic terms like phrases and clauses | A.Viewtype('syntax') | [`subphrase`](features/featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`clause`](features/featuresbynodetype.md#clause-nodes) [`group`](featuresbynodetype.md#group-nodes)

<sup>Note: the node types  [`Word`](features/featuresbynodetype.md#word-nodes), [`Sentence`](features/featuresbynodetype.md#sentence-nodes), [`verse`](featuresbynodetype.md#verse-nodes), [`chapter`](features/featuresbynodetype.md#chapter-nodes), and [`Book`](features/featuresbynodetype.md#book-nodes) are common for both views.</sup>

## User impact

It was found that both data designs with their repective views might have their uses, hence this Text-Fabric dataset providing both. As a result, syntactic queries can be constructed to match either one of these data structures. The following figure provides two functionaly equivalent queries:

<img src="features\images\compare_queries.png" width="600">

These queries, for example, can be used to investigate what is thrown down by fire or to determine the specific preposition used for this indication. This is because we specified word class instead of lexeme. The query searches for clauses or word groups containing the verb βάλλω (meaning 'to throw down') together with a complement phrase or adverbial word group containing the lemma πῦρ (meaning 'fire'). Both queries yield identical results in terms of verses (Matthew 3:10; 7:19, Mark 9:22, and Luke 3:9) and words. However, it is also important to note that different nodes are reported for clauses and phrases compared to word groups, as evidenced by the values of each tuple's first and third item.

### Impact on using parent and sibling feature 

Understanding the distinctions between these two views is especialy important when building queries that involve parent-child relations. E.g. when using the edge features [parent](features/parent.md#start) and [sibling](features/sibling.md#start). See following image for details:

<img src="features/images/wordgroup_syntactic_view.png" width="600">

This image compares the parent (arrows) and sibling features (connector with circle) for the first phrase of the book of John (John 1:1) for the [`wg-view`](wg-view.md#start) and the [`syntax-view`](syntactic-view.md#start) for the data. The parent feature for a specific node can be obtained using *E.parent.f(node)* and the sibling feature can be calculated using *E.sibling.b(node)*, where node stands for the number of the node. The direction of the arrow indicates the parent node of a given node. The dotted lines indicate that the `wg` nodes share the same data as the [`sentence`](features/featuresbynodetype.md#sentence-nodes), [`clause`](features/featuresbynodetype.md#clause-nodes), and [`phrase`](features/featuresbynodetype.md#phrase-nodes). The [`subphrase`](features/featuresbynodetype.md#subphrase-nodes), [`verse`](features/featuresbynodetype.md#verse-nodes), and [`chapter`](features/featuresbynodetype.md#chapter-nodes) nodes are not nested in the calculation of the parent and sibling features.

## Implementation notes

## Matching table

For feature pair [cls](features/cls.md#start) and [typ](features/typ.md#start)
cls (WG view) | typ (Syntax view)
---|---
adjp | AdjP
advp | AdvP
np | NP
pp | PP
vp | VP




