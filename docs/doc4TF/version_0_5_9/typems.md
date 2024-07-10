Doc4TF pages for [Nestle 1904 Greek New Testament](https://github.com/saulocantanhede/tfgreek2/tree/main/tf) (version 0.5.9)
# Feature: typems
Data type|Feature type|Available for nodes
---|---|---
[`String`](featuresbydatatype.md#string)|[`Node`](featuresbytype.md#node)| [`sentence`](featuresbynodetype.md#sentence)  [`group`](featuresbynodetype.md#group)  [`clause`](featuresbynodetype.md#clause)  [`wg`](featuresbynodetype.md#wg)  [`phrase`](featuresbynodetype.md#phrase)  [`subphrase`](featuresbynodetype.md#subphrase)  [`word`](featuresbynodetype.md#word) 
## Description
morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)
## Feature Values
### Frequency for nodetype [sentence](featuresbynodetype.md#sentence)
Value|Occurences
---|---
wrapper-clause-scope|5571
group|375

Total frequency of feature: 5946.
 ### Frequency for nodetype [group](featuresbynodetype.md#group)
Value|Occurences
---|---
conjuncted-wg|8075
apposition-group|870

Total frequency of feature: 8945.
 ### Frequency for nodetype [clause](featuresbynodetype.md#clause)
Value|Occurences
---|---
wrapper-clause-scope|6595
group|2257
apposition-group|21

Total frequency of feature: 8873.
 ### Frequency for nodetype [wg](featuresbynodetype.md#wg)
Value|Occurences
---|---
modifier-scope|29645
wrapper-clause-scope|12166
wrapper-scope|11264
conjuncted-wg|8075
group|4957
modifier-clause-scope|1712
apposition-group|891

Total frequency of feature: 68710.
 ### Frequency for nodetype [phrase](featuresbynodetype.md#phrase)
Value|Occurences
---|---
modifier-scope|10484
wrapper-scope|9535
personal|5885
common|2120
relative|1364
group|952
modifier-clause-scope|755
demonstrative|744
proper|683
interrogative|480

Total frequency of feature: 33293. Note: table truncated.
 ### Frequency for nodetype [subphrase](featuresbynodetype.md#subphrase)
Value|Occurences
---|---
modifier-scope|29645
common|23644
personal|11521
wrapper-scope|11264
proper|4639
group|2325
demonstrative|1722
modifier-clause-scope|1712
relative|1674
interrogative|633

Total frequency of feature: 89404. Note: table truncated.
 ### Frequency for nodetype [word](featuresbynodetype.md#word)
Value|Occurences
---|---
common|23644
personal|11521
proper|4639
demonstrative|1722
relative|1674
interrogative|633
indefinite|552
possessive|70
adverbial|3

Total frequency of feature: 44458.
  

Created on Jul. 10, 2024 using [Doc4TF version 0.5.2 (July 10, 2024)](https://github.com/tonyjurg/Doc4TF/blob/main/CreateFeatureDoc.ipynb) 