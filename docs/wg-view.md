# WordGroup view <a name="start"></a>

*draft notes for now* 

Can be switched to when prefered.

The two views are possible since in the database there is a replication of data.

WG is an agnostic presentation. 

Swithing to a specific viewtype can be done using the command A.Viewtype(), which is specific to this dataset and automaticaly loaded upon invocation of the TF dataset.

The relation between node types and view types is shown in the following table.

View | Invocation | Associated node types | 
--- | --- | ---
Wordgroup (this view) | A.Viewtype('wg') | [`wg`](featuresbynodetype.md#wordgroup-nodes) 
[Syntactic](syntactic-view.md#start) | A.Viewtype('syntax') | [`subphrase`](features/featuresbynodetype.md#subphrase-nodes) [`phrase`](features/featuresbynodetype.md#phrase-nodes) [`clause`](features/featuresbynodetype.md#clause-nodes) [`group`](features/featuresbynodetype.md#group-nodes)

The following images show the different presentation of the syntax tree for the two views:

### Syntactic view

<img src="features/images/syntax_view.png" width="650">

### Wordgroup view

<img src="features/images/wgview.png" width="650">

### Impact on using parent and sibling feature 

Understanding the distinctions between these two views is especialy important when building queries that involve parent-child relations. E.g. when using the edge features [parent](features/parent.md#start) and [sibling](features/sibling.md#start). See following image for details:

<img src="features/images/wordgroup_syntactic_view.png" width="600">

This image compares the parent (arrows) and sibling features (connector with circle) for the first phrase of the book of John (John 1:1) for the word group view and the [Syntax view](syntactic-view.md#start) for the data. The parent feature for a specific node can be obtained using *E.parent.f(node)* and the sibling feature can be calculated using *E.sibling.b(node)*, where node stands for the number of the node. The direction of the arrow indicates the parent node of a given node. The dotted lines indicate that the `wg` nodes share the same data as the [`sentence`](features/featuresbynodetype.md#sentence-nodes), [`clause`](features/featuresbynodetype.md#clause-nodes), and [`phrase`](features/featuresbynodetype.md#phrase-nodes). The [`subphrase`](features/featuresbynodetype.md#subphrase-nodes), [`verse`](features/featuresbynodetype.md#verse-nodes), and [`chapter`](features/featuresbynodetype.md#chapter-nodes) nodes are not nested in the calculation of the parent and sibling features.
