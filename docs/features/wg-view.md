# WordGroup view <a name="start"></a>

*draft notes for now* 

Can be switched to when prefered.

The two views are possible since in the database there is a replication of data.

WG is an agnostic presentation. 
A.show() with option hiddenTypes={"clause","group","subphrase","phrase"}

The relation between node types and view types is shown in the following table.
View | Node types | 
---|---
wordgroup | [`wg`](featuresbynodetype.md#wordgroup-nodes) 
Syntactical | [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`clause`](featuresbynodetype.md#clause-nodes) [`group`](featuresbynodetype.md#group-nodes)

Understanding this distinction is especialy important when building queries that involve parent-child relations. E.g. when using the edge features [parent](parent.md#start) and [sibling](sibling.md#start).

Other view: [Syntax view](syntactic-view.md#start)
