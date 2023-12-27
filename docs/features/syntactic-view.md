# Syntactic view <a name="start"></a>

*draft notes for now* 

default view (need to be implemented). Utilizes the terms common in linguistic research.

The two views are possible since in the database there is a replication of data.

A.show() with option hiddenTypes={"wg"}

The relation between node types and view types is shown in the following table.
View | Node types | 
---|---
wordgroup | [`wg`](featuresbynodetype.md#wordgroup-nodes) 
Syntactical | [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`group`](featuresbynodetype.md#group-nodes)

Understanding this distinction is especialy important when building queries that involve parent-child relations. E.g. when using the edge features [parent](parent.md#start) and [sibling](sibling.md#start). See following image for details:

<img src="images/wordgroup_syntactic_view.png" width="600">




Other view: [WordGroup view](wg-view.md#start)
