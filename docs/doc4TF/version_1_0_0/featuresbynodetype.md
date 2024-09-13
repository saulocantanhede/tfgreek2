Doc4TF pages for [Nestle 1904 Greek New Testament](https://github.com/saulocantanhede/tfgreek2/releases/download/1.0.0/tf-1.0.0.zip) (version 1.0.0)
# Overview features by node type
Overview by [name](featuresbyname.md), [data type](featuresbydatatype.md), or [feature type](featuresbytype.md).
## book

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`lang`](lang.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|language the text is in|`el`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
## chapter

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
## verse

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## sentence

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`clausetype`](clausetype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`nodeid`](nodeid.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|node id (as in the XML source data)|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## group

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical type (on sentence, group, clause or phrase)|`conjuncted` `apposition`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## clause

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`clausetype`](clausetype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`junction`](junction.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`nodeid`](nodeid.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|node id (as in the XML source data)|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical type (on sentence, group, clause or phrase)|`conjuncted` `apposition`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## wg

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`clausetype`](clausetype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause type|`Verbless` `VerbElided` `Minor`
[`crule`](crule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`junction`](junction.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`nodeid`](nodeid.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|node id (as in the XML source data)|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`rela`](rela.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical type (on sentence, group, clause or phrase)|`conjuncted` `apposition`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
## phrase

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word|` ` `, ` `. ` `· `
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`before`](before.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`case`](case.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|domain|`092004` `033006` `013001` `069002`
[`framespec`](framespec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`id`](id.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`junction`](junction.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`lemma`](lemma.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `εἰμί` `σύ`
[`lemmatranslit`](lemmatranslit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word lemma|`autos` `lego` `eimi` `su`
[`ln`](ln.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological code|`V-PAI-3S` `ADV` `PRT-N` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical person|`p3` `p2` `p1`
[`punctuation`](punctuation.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|punctuation found after a word|`,` `.` `·` `;`
[`ref`](ref.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!15` `1CO 10:1!17` `1CO 10:1!2`
[`referent`](referent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`sp`](sp.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|part-of-speach|`verb` `pron` `advb` `subs`
[`strong`](strong.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|strong number|`846` `3004` `1510` `4771`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal tense|`aorist` `present` `future` `imperfect`
[`text`](text.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`trailer`](trailer.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word (excluding critical signs)|` ` `, ` `. ` `· `
[`trans`](trans.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|translation of the word surface text according to the Berean Interlinear Bible|`not` `you` `is` `Him`
[`translit`](translit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word surface text|`me` `estin` `auton` `auto`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical type (on sentence, group, clause or phrase)|`conjuncted` `apposition`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`unaccent`](unaccent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters without accents and diacritical markers|`εστιν` `αυτον` `μη` `αυτω`
[`unicode`](unicode.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute variant|`2` `1`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
[`voice`](voice.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`
## subphrase

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word|` ` `, ` `. ` `· `
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the sentence, group, clause, phrase or wg has an article|`1`
[`before`](before.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`case`](case.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|domain|`092004` `033006` `013001` `069002`
[`framespec`](framespec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`id`](id.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`junction`](junction.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|type of junction|`coordinate` `subordinate`
[`lemma`](lemma.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `εἰμί` `σύ`
[`lemmatranslit`](lemmatranslit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word lemma|`autos` `lego` `eimi` `su`
[`ln`](ln.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological code|`V-PAI-3S` `ADV` `PRT-N` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical person|`p3` `p2` `p1`
[`punctuation`](punctuation.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|punctuation found after a word|`,` `.` `·` `;`
[`ref`](ref.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!15` `1CO 10:1!17` `1CO 10:1!2`
[`referent`](referent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`rela`](rela.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical rule|`Conj-CL` `CLaCL` `ClCl` `ClCl2`
[`sp`](sp.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|part-of-speach|`verb` `pron` `advb` `subs`
[`strong`](strong.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|strong number|`846` `3004` `1510` `4771`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal tense|`aorist` `present` `future` `imperfect`
[`text`](text.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`trailer`](trailer.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word (excluding critical signs)|` ` `, ` `. ` `· `
[`trans`](trans.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|translation of the word surface text according to the Berean Interlinear Bible|`not` `you` `is` `Him`
[`translit`](translit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word surface text|`me` `estin` `auton` `auto`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|syntactical type (on sentence, group, clause or phrase)|`conjuncted` `apposition`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`unaccent`](unaccent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters without accents and diacritical markers|`εστιν` `αυτον` `μη` `αυτω`
[`unicode`](unicode.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute variant|`2` `1`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
[`voice`](voice.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`
## word

Feature|Feature type|Data type|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word|` ` `, ` `. ` `· `
[`before`](before.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute before|`—` `(` `[[`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`case`](case.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical case|`nominative` `accusative` `dative` `genitive`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute cls|`cl`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute criticalsign|`—` `)` `(` `]]`
[`degree`](degree.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical degree|`comparative` `superlative`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|1 if the word is out of sequence in the xml|`1`
[`domain`](domain.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|domain|`092004` `033006` `013001` `069002`
[`frame`](frame.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|frame|`A0` `A1` `A2` `AA2`
[`framespec`](framespec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical gender|`masculine` `neuter` `feminine`
[`gloss`](gloss.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|English gloss (BGVB)|`the` `and, also, likewise` `he, she, it, himself, herself, itself; even, very; same` `you`
[`id`](id.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`lemma`](lemma.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lexical lemma|`αὐτός` `λέγω` `εἰμί` `σύ`
[`lemmatranslit`](lemmatranslit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word lemma|`autos` `lego` `eimi` `su`
[`ln`](ln.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological code|`V-PAI-3S` `ADV` `PRT-N` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|annotation of linguistic nature|`discontinuous discourse`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`number`](number.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical number|`singular` `plural`
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|parent relationship between words|`Link`
[`person`](person.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|grammatical person|`p3` `p2` `p1`
[`punctuation`](punctuation.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|punctuation found after a word|`,` `.` `·` `;`
[`ref`](ref.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!15` `1CO 10:1!17` `1CO 10:1!2`
[`referent`](referent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`rela`](rela.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|role|`o` `s` `p` `adv`
[`sp`](sp.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|part-of-speach|`verb` `pron` `advb` `subs`
[`strong`](strong.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|strong number|`846` `3004` `1510` `4771`
[`subjref`](subjref.md#readme)|[`Edge`](featuresbytype.md#Edge)|[`String`](featuresbydatatype.md#String)|number of subject referent|`Link`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal tense|`aorist` `present` `future` `imperfect`
[`text`](text.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`trailer`](trailer.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|material after the end of the word (excluding critical signs)|` ` `, ` `. ` `· `
[`trans`](trans.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|translation of the word surface text according to the Berean Interlinear Bible|`not` `you` `is` `Him`
[`translit`](translit.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|transliteration of the word surface text|`me` `estin` `auton` `auto`
[`typems`](typems.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group`
[`unaccent`](unaccent.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters without accents and diacritical markers|`εστιν` `αυτον` `μη` `αυτω`
[`unicode`](unicode.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|this is XML attribute variant|`2` `1`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#Node)|[`Integer`](featuresbydatatype.md#Integer)|verse number, from ref attribute in xml|`1` `2` `3` `4`
[`voice`](voice.md#readme)|[`Node`](featuresbytype.md#Node)|[`String`](featuresbydatatype.md#String)|verbal voice|`active` `passive` `middle` `middlepassive`


Created on Sep. 13, 2024 using [Doc4TF version 0.5.2 (July 10, 2024)](https://github.com/tonyjurg/Doc4TF/blob/main/CreateFeatureDoc.ipynb)