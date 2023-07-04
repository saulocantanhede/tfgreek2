# Feature: domain

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`w`](featuresbynodetype.md#word-nodes)

## Feature description

Lexical domain according to Semantic Dictionary of Biblical Greek (SDBG).

## Feature values

domain (this feature) | Comment | Frequency
--- | --- | ---
xxxyyy  | Lexical Domain value| 126757
'' | Empty | 11022

## Interpreting the data
Feature domain is equivalent to a numerical representation of feature [ln](ln.md) and can be decoded using the following method. Take for example lex_domain = "089007". The 6-digit value "089007" first need to be split into two 3-digit parts: "087" and "007". The second part should be interpreted as a alphabetic (A=1, B=2, C=3, D=4, E=5, ..., Z=26). Taken the two parts together, this will result in 89G, which points to an entry in Louw-Nida. For this example (i.e. 89G) this maps to main section [relations](https://www.laparola.net/greco/louwnida.php?sezmag=89) and subsection [Cause and/or Reason](https://www.laparola.net/greco/louwnida.php?sezmag=89&sez1=15&sez2=38).

## Note

See also related feature [ln](ln.md#readme) (Louw-Nida lexical classification).

## Source description

Taken from XML attribute `domain` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
