# Syntactic view <a name="start"></a>

default view (need to be implemented).

The two views are possible since in the database there is a replication of data.

A.show() with option hiddenTypes={"wg"}

relation between node typess:
* [`wg`](featuresbynodetype.md#wordgroup-nodes) (wordgroup): refers to a collection or grouping of words that form a cohesive unit. It can match any of the following:
   * [`subphrase`](featuresbynodetype.md#subphrase-nodes): Nodes pertaining to a subphrase unit.
   * [`phrase`](featuresbynodetype.md#phrase-nodes): Nodes pertaining to a phrase unit.
   * [`clause`](featuresbynodetype.md#clause-nodes): Nodes pertaining to a clause unit.
   * [`group`](featuresbynodetype.md#group-nodes): Nodes pertaining to a phrase unit.

Other view: [WordGroup view](wg-view.md#start)
