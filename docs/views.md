# Views <a name="start"></a>

## The view types

This database offers the users two distinct views to represent the syntax trees:
   * [Syntactic view](syntactic-view.md#start) (default): presents the syntax tree using linguistic terms like phrases and clauses.
   * [WordGroup view](wg-view.md#start): presents the syntax tree in a more agnostic manner by means of word groups.

## User impact

It was found that both data designs with their repective views might have their uses, hence this Text-Fabric dataset providing both. As a result, syntactic queries can be constructed to match either one of these data structures. The following figure provides two functionaly equivalent queries:

<img src="features\images\compare_queries.png">

These queries, for example, can be used to investigate what is thrown down by fire or to determine the specific preposition used for this indication. This is because we specified word class instead of lexeme. The query searches for clauses or word groups containing the verb βάλλω (meaning 'to throw down') together with a complement phrase or adverbial word group containing the lemma πῦρ (meaning 'fire'). Both queries yield identical results in terms of verses (Matthew 3:10; 7:19, Mark 9:22, and Luke 3:9) and words. However, it is also important to note that different nodes are reported for clauses and phrases compared to word groups, as evidenced by the values of each tuple's third item.

## Implementation notes

