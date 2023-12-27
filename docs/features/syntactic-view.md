# Syntactic view <a name="start"></a>

*draft notes for now* 

default view (need to be implemented). Utilizes the terms common in linguistic research.

The two views are possible since in the database there is a replication of data.

A.show() with option hiddenTypes={"wg"}

The relation between node types and view types is shown in the following table.
View | Associated node types | 
---|---
[Wordgroup](wg-view.md#start) | [`wg`](featuresbynodetype.md#wordgroup-nodes) 
Syntactical (this) | [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`group`](featuresbynodetype.md#group-nodes)

Understanding this distinction is especialy important when building queries that involve parent-child relations. E.g. when using the edge features [parent](parent.md#start) and [sibling](sibling.md#start). See following image for details:

<img src="images/wordgroup_syntactic_view.png" width="600">

This image compares the parent (arrows) and sibling features (connector with circle) for the first phrase of the book of John (John 1:1) for the [WordGroup view](wg-view.md#start) and the Syntax view for the data. The parent feature for a specific node can be obtained using *E.parent.f(node)* and the sibling feature can be calculated using *E.sibling.b(node)*, where node stands for the number of the node. The direction of the arrow indicates the parent node of a given node. The dotted lines indicate that the `wg` nodes share the same data as the [`sentence`](featuresbynodetype.md#sentence-nodes), [`clause`](featuresbynodetype.md#clause-nodes), and [`phrase`](featuresbynodetype.md#phrase-nodes). The [`subphrase`](featuresbynodetype.md#subphrase-nodes), [`verse`](featuresbynodetype.md#verse-nodes), and [`chapter`](featuresbynodetype.md#chapter-nodes) nodes are not nested in the calculation of the parent and sibling features.
