# Feature: otype <a name="start"></a>

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Grid`](featuresbygroup.md#grid-features) | [`Node`](featuresbyfeaturetype.md#node-features) | Configuration | [`word`](featuresbynodetype.md#word-nodes) [`wg`](featuresbynodetype.md#wordgroup-nodes) [`Sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`Book`](featuresbynodetype.md#book-nodes) [`phrase`](featuresbynodetype.md#phrase-nodes) [`subphrase`](featuresbynodetype.md#subphrase-nodes) [`Group`](featuresbynodetype.md#group-nodes) [`Clause`](featuresbynodetype.md#clause-nodes) 

## Feature description

Types for text objects as they are represented by nodes.
 
type | kind | description
--- |--- |---
[`word`](featuresbynodetype.md#word-nodes) | slot | single word, fills a *slot*;
[`wg`](featuresbynodetype.md#wordgroup-nodes) | functional | wordgroup, maybe with gaps
[`subphrase`](featuresbynodetype.md#subphrase-nodes) | functional | subphrase, maybe with gaps
[`Phrase`](featuresbynodetype.md#phrase-nodes) | functional | phrase, maybe with gaps
[`Clause`](featuresbynodetype.md#clause-nodes) | functional | clause, maybe with gaps
[`Group`](featuresbynodetype.md#group-nodes) | functional | group, maybe with gaps
[`Sentence`](featuresbynodetype.md#sentence-nodes) |functional| clause, maybe with gaps
[`verse`](featuresbynodetype.md#verse-nodes) |section | numbered unit of a chapter
[`chapter`](featuresbynodetype.md#chapter-nodes) | section | numbered unit of a book
[`Book`](featuresbynodetype.md#book-nodes) | section | named part of the Greek New Testament

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

## Notes

This feature can be very usefull to generate a list of nodes of a certain type, e.g. `verse` nodes:
<pre>
for verse in F.otype.s('verse'):
    "do something with verse nodes"
 </pre>

 ## Source description

 Calculated during datacreation.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), [feature group](featuresbygroup.md#start) or [feature type](featuresbyfeaturetype.md#start).*

