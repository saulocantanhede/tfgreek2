# Feature: bol_lemma <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes)

## Feature description

Lexical lemma provided by [Bible Online Learner](http://www.dadel.org/). 

## Notes

This feature is required to enhance compatibility between the Bible Online Learner and Text-Fabric. 

<img src="images/bol_lexeme.png" width="500">

The highligted value can be copy-pasted into a TF queries like:
<pre>
   BolQuery = '''
   word bol_lemma=ἀρχή
   '''
   BolQueryResults = A.search(BolQuery)
</pre>


## Source description

External (from Bible Online Learner).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*
