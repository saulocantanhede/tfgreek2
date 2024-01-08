N1904 Greek New Testament Text-Fabric dataset [saulocantanhede/tfgreek2 - 0.5.4](https://github.com/saulocantanhede/tfgreek2)
# Overview features per type
## Node

Feature|Datatype|Available on nodes|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |material after the end of the word| `Link` 
[`appositioncontainer`](appositioncontainer.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |1 if it is an apposition container| `Link` 
[`articular`](articular.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |1 if the sentence, group, clause, phrase or wg has an article| `Link` 
[`before`](before.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute before| `Link` 
[`book`](book.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |book name (full name)| `Link` 
[`bookshort`](bookshort.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |book name (abbreviated) from ref attribute in xml| `Link` 
[`case`](case.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |grammatical case| `Link` 
[`chapter`](chapter.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |chapter number, from ref attribute in xml| `Link` 
[`clausetype`](clausetype.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |clause type| `Link` 
[`cls`](cls.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute cls| `Link` 
[`cltype`](cltype.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |clause type| `Link` 
[`criticalsign`](criticalsign.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute criticalsign| `Link` 
[`crule`](crule.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |clause rule (from xml attribute Rule)| `Link` 
[`degree`](degree.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |grammatical degree| `Link` 
[`discontinuous`](discontinuous.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |1 if the word is out of sequence in the xml| `Link` 
[`domain`](domain.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |domain| `Link` 
[`framespec`](framespec.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute framespec| `Link` 
[`function`](function.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute function| `Link` 
[`gender`](gender.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |grammatical gender| `Link` 
[`gloss`](gloss.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |short translation| `Link` 
[`id`](id.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |xml id| `Link` 
[`junction`](junction.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |type of junction| `Link` 
[`lang`](lang.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |language the text is in| `Link` 
[`lemma`](lemma.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |lexical lemma| `Link` 
[`ln`](ln.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |ln| `Link` 
[`mood`](mood.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |verbal mood| `Link` 
[`morph`](morph.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |morphological code| `Link` 
[`nodeid`](nodeid.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |node id (as in the XML source data| `Link` 
[`normalized`](normalized.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |lemma normalized| `Link` 
[`note`](note.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |annotation of linguistic nature| `Link` 
[`num`](num.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.| `Link` 
[`number`](number.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |grammatical number| `Link` 
[`otype`](otype.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |No feature description| `Link` 
[`person`](person.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |grammatical person| `Link` 
[`punctuation`](punctuation.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute punctuation| `Link` 
[`ref`](ref.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |biblical reference with word counting| `Link` 
[`referent`](referent.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |number of referent| `Link` 
[`rela`](rela.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute rela| `Link` 
[`role`](role.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |role| `Link` 
[`rule`](rule.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |syntactical rule| `Link` 
[`strong`](strong.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |strong number| `Link` 
[`subjrefspec`](subjrefspec.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute subjrefspec| `Link` 
[`tense`](tense.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |verbal tense| `Link` 
[`text`](text.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |the text of a word| `Link` 
[`typ`](typ.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute typ| `Link` 
[`type`](type.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)| `Link` 
[`unicode`](unicode.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |word in unicode characters plus material after it| `Link` 
[`variant`](variant.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |this is XML attribute variant| `Link` 
[`verse`](verse.md#readme)|[`Integer`](featurebydatatype.md#integer)|[`word`](featurebynodetype.md#word) |verse number, from ref attribute in xml| `Link` 
[`voice`](voice.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |verbal voice| `Link` 
## Edge

Feature|Datatype|Available on nodes|Description|Examples
---|---|---|---|---
[`frame`](frame.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |frame| `Link` 
[`oslots`](oslots.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |No feature description| `Link` 
[`parent`](parent.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |parent relationship between words| `Link` 
[`subjref`](subjref.md#readme)|[`String`](featurebydatatype.md#string)|[`word`](featurebynodetype.md#word) |number of subject referent| `Link` 
