# Feature: otype

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Grid`](featuresbygroup.md#grid-features) | [`Node`](featuresbyfeaturetype.md#node-features) | Configuration | All (see below)

## Feature description

Types for text objects as they are represented by nodes.
 
type | kind | description
--- |--- |---
[`w`](wordnodefeatures.md#readme) | slot | single word, fills a *slot*;
[`wg`](wordgroupnodefeatures.md#readme) | functional | wordgroup, maybe with gaps
[`Phrase`](phrasenodefeatures.md#readme) | functional | phrase, maybe with gaps
[`Clause`](clausenodefeatures.md#readme) |functional | clause, maybe with gaps
[`Sentence`](sentencenodefeatures.md#readme) |functional| clause, maybe with gaps
[`verse`](versenodefeatures.md#readme) |section | numbered unit of a chapter
[`chapter`](chapternodefeatures.md#readme) | section | numbered unit of a book
[`Book`](booknodefeatures.md#readme) | section | named part of the Greek New Testament

All objects have a type, which is just a label.
Objects and their slots are represented in Text-Fabric as *nodes*.
The information which object occupies which slot is stored in the edge feature [oslots](oslots.md).

type|description
---|---
[Section types](#section-types) |division in books, chapters, etc.
[Word type](#word-type)  |all about the individual words
[Linguistic types](#linguistic-types) |wordgroups (wg), phrases, clauses, etc.

# Section types

The section types correspond to the various divisional units in the Bible.
The Greek New Testament is divided in books, books are divided in chapters, chapters are divided in verses.
The sectional types `book`, `chapter`, `verse` specify features which indicate which book, chapter, verse their objects refer to.

A `book` object carries the [book](book.md) feature, which contains the name of the book.
A `chapter` object carries the [chapter](chapter.md) feature, which contains the number of the chapter.
It carries also the [book](book.md) feature to indicate the book of which it is a chapter.
Analogously, the `verse` object carries the [verse](verse.md) feature, which contains the number of the chapter,
and the [book](book.md) and [chapter](chapter.md) features.

# Word type

There is only one type for words, the `word` type.
Word objects correspond to the smallest divisional units in the Greek New Testament dataset.
They are also identified with *slots*, because each slot is filled by a word and each word fills a slot.
Words are not identified with strings, because there are various
string representations of the words, none of which is canonical. All word occurrences are numbered
with a slot number.

Word occurrences corresponds to lexemes, i.e. dictionary entries, for which we have a separate object type.
For the textual representation of lexemes we have a variety of features, in order to get their 


# Linguistic types

Linguistic types correspond to syntactical entities such as sentences, clauses and phrases.
The functional object types are `sentence`, `clause`, and `phrase`.
They correspond to possibly discontinuous stretches of text that function as a unit.

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
