Doc4TF pages for [Nestle 1904 Greek New Testament](https://github.com/saulocantanhede/tfgreek2/tree/master/tf) (version 0.5.5)
# Overview features per nodetype
## book

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`lang`](lang.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|language the text is in|`el`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
## chapter

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`chapter`](chapter.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
## verse

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`chapter`](chapter.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`verse`](verse.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## sentence

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`clausetype`](clausetype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`junction`](junction.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`nodeid`](nodeid.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|node id (as in the XML source data|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
## group

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`typ`](typ.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute typ|`conjuncted` `apposition`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
## clause

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`clausetype`](clausetype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`junction`](junction.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`nodeid`](nodeid.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|node id (as in the XML source data|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
## wg

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`clausetype`](clausetype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`junction`](junction.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`nodeid`](nodeid.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|node id (as in the XML source data|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`rela`](rela.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`typ`](typ.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute typ|`conjuncted` `apposition`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
## phrase

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|material after the end of the word|` ` `,` `.` `·`
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`before`](before.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`case`](case.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|domain|`092004` `033006` `069002` `092003`
[`framespec`](framespec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`gloss`](gloss.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|short translation|`not` `you` `Him` `to you`
[`id`](id.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`junction`](junction.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`lemma`](lemma.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `σύ` `ἐγώ`
[`ln`](ln.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological code|`ADV` `PRT-N` `V-PAI-3S` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical person|`third` `second` `first`
[`punctuation`](punctuation.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute punctuation|` ` `,` `.` `·`
[`ref`](ref.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!17` `1CO 10:1!2` `1CO 10:1!21`
[`referent`](referent.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`strong`](strong.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|strong number|`846` `3004` `4771` `1473`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal tense|`aorist` `present` `future` `perfect`
[`text`](text.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`typ`](typ.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute typ|`conjuncted` `apposition`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
[`unicode`](unicode.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute variant|`2` `1`
[`voice`](voice.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`
## subphrase

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|material after the end of the word|` ` `,` `.` `·`
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`before`](before.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`case`](case.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|domain|`092004` `033006` `069002` `092003`
[`framespec`](framespec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`gloss`](gloss.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|short translation|`not` `you` `Him` `to you`
[`id`](id.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`junction`](junction.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`lemma`](lemma.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `σύ` `ἐγώ`
[`ln`](ln.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological code|`ADV` `PRT-N` `V-PAI-3S` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical person|`third` `second` `first`
[`punctuation`](punctuation.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute punctuation|` ` `,` `.` `·`
[`ref`](ref.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!17` `1CO 10:1!2` `1CO 10:1!21`
[`referent`](referent.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`rela`](rela.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`strong`](strong.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|strong number|`846` `3004` `4771` `1473`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal tense|`aorist` `present` `future` `perfect`
[`text`](text.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`typ`](typ.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute typ|`conjuncted` `apposition`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
[`unicode`](unicode.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute variant|`2` `1`
[`voice`](voice.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`
## word

Feature|Featuretype|Datatype|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|material after the end of the word|` ` `,` `.` `·`
[`before`](before.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`book`](book.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`case`](case.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`chapter`](chapter.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`cls`](cls.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|domain|`092004` `033006` `069002` `092003`
[`frame`](frame.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|frame|`A0` `A1` `A2` `AA2`
[`framespec`](framespec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`gloss`](gloss.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|short translation|`not` `you` `Him` `to you`
[`id`](id.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`lemma`](lemma.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `σύ` `ἐγώ`
[`ln`](ln.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological code|`ADV` `PRT-N` `V-PAI-3S` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|grammatical person|`third` `second` `first`
[`punctuation`](punctuation.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute punctuation|` ` `,` `.` `·`
[`ref`](ref.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!17` `1CO 10:1!2` `1CO 10:1!21`
[`referent`](referent.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`rela`](rela.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|role|`adv` `o` `s` `apposition`
[`sibling`](sibling.md#readme)|[`Edge`](featurebytype.md#Edge)|[`Integer`](featurebydatatype.md#Integer)|this is XML attribute sibling|`1` `2` `3` `4`
[`strong`](strong.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|strong number|`846` `3004` `4771` `1473`
[`subjref`](subjref.md#readme)|[`Edge`](featurebytype.md#Edge)|[`String`](featurebydatatype.md#String)|number of subject referent|`Link`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal tense|`aorist` `present` `future` `perfect`
[`text`](text.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`type`](type.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
[`unicode`](unicode.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|this is XML attribute variant|`2` `1`
[`verse`](verse.md#readme)|[`Node`](featurebytype.md#Node)|[`Integer`](featurebydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
[`voice`](voice.md#readme)|[`Node`](featurebytype.md#Node)|[`String`](featurebydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`


Created on Jan. 24, 2024 using [Doc4TF  version 0.3 (Jan. 24, 2024)](https://github.com/tonyjurg/Doc4TF)