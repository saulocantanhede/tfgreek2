<p>N1904 Greek New Testament Text-Fabric dataset <a href="https://github.com/saulocantanhede/tfgreek2">saulocantanhede/tfgreek2 - 0.5.2</a></p>

<h1>Features per node type</h1>

<h2>book</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute book_short</td>
  <td><code>LUK</code> <code>ACT</code></td>
</tr>
<tr>
  <td><A HREF="lang.md#readme">lang</A></td>
  <td><code>string</code></td>
  <td>language the text is in</td>
  <td><code>el</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
</tbody>
</table>

<h2>chapter</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>chapter number, from ref attribute in xml</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
</tbody>
</table>

<h2>verse</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>chapter number, from ref attribute in xml</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td><code>integer</code></td>
  <td>verse number, from ref attribute in xml</td>
  <td><code>10</code> <code>12</code></td>
</tr>
</tbody>
</table>

<h2>sentence</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td><code>integer</code></td>
  <td>1 if the wg has an article</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>nominalized</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>VerbElided</code> <code>Verbless</code></td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td><code>string</code></td>
  <td>clause rule (from xml attribute Rule)</td>
  <td><code>ClCl</code> <code>ClCl2</code></td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td><code>string</code></td>
  <td>type of junction</td>
  <td><code>coordinate</code> <code>subordinate</code></td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td><code>integer</code></td>
  <td>node id (as in the XML source data</td>
  <td><code>400010200010490</code> <code>400010200120390</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td><code>string</code></td>
  <td>syntactical rule</td>
  <td><code>DetNP</code> <code>PrepNp</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
</tbody>
</table>

<h2>group</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td><code>integer</code></td>
  <td>1 if the wg has an article</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td><code>string</code></td>
  <td>syntactical rule</td>
  <td><code>DetNP</code> <code>PrepNp</code></td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute typ</td>
  <td><code>NP</code> <code>PP</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
</tbody>
</table>

<h2>clause</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td><code>integer</code></td>
  <td>1 if the wg has an article</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>nominalized</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>VerbElided</code> <code>Verbless</code></td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td><code>string</code></td>
  <td>clause rule (from xml attribute Rule)</td>
  <td><code>ClCl</code> <code>ClCl2</code></td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td><code>string</code></td>
  <td>type of junction</td>
  <td><code>coordinate</code> <code>subordinate</code></td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td><code>integer</code></td>
  <td>node id (as in the XML source data</td>
  <td><code>400010200010490</code> <code>400010200120390</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td><code>string</code></td>
  <td>syntactical rule</td>
  <td><code>DetNP</code> <code>PrepNp</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
</tbody>
</table>

<h2>wg</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td><code>integer</code></td>
  <td>1 if it is an apposition container</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td><code>integer</code></td>
  <td>1 if the wg has an article</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>nominalized</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td><code>string</code></td>
  <td>clause type</td>
  <td><code>VerbElided</code> <code>Verbless</code></td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td><code>string</code></td>
  <td>clause rule (from xml attribute Rule)</td>
  <td><code>ClCl</code> <code>ClCl2</code></td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute function</td>
  <td><code>Pred</code> <code>Subj</code></td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td><code>string</code></td>
  <td>type of junction</td>
  <td><code>coordinate</code> <code>subordinate</code></td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td><code>integer</code></td>
  <td>node id (as in the XML source data</td>
  <td><code>400010200010490</code> <code>400010200120390</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute rela</td>
  <td><code>Appo</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td><code>string</code></td>
  <td>syntactical rule</td>
  <td><code>DetNP</code> <code>PrepNp</code></td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute typ</td>
  <td><code>NP</code> <code>PP</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
</tbody>
</table>

<h2>phrase</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td><code>string</code></td>
  <td>material after the end of the word</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td><code>integer</code></td>
  <td>1 if it is an apposition container</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td><code>integer</code></td>
  <td>1 if the wg has an article</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute before</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td><code>string</code></td>
  <td>grammatical case</td>
  <td><code>nominative</code> <code>accusative</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute criticalsign</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td><code>string</code></td>
  <td>grammatical degree</td>
  <td><code>comparative</code> <code>superlative</code></td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td><code>integer</code></td>
  <td>1 if the word is out of sequence in the xml</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td><code>string</code></td>
  <td>domain</td>
  <td><code>092004</code> <code>089017</code></td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute framespec</td>
  <td><code>A0:n00000000000</code> <code>A1:n00000000000</code></td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute function</td>
  <td><code>Pred</code> <code>Subj</code></td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td><code>string</code></td>
  <td>grammatical gender</td>
  <td><code>masculine</code> <code>feminine</code></td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td><code>string</code></td>
  <td>short translation</td>
  <td><code>the</code> <code>and</code></td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td><code>string</code></td>
  <td>xml id</td>
  <td><code>n40001001001</code> <code>n40001001002</code></td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td><code>string</code></td>
  <td>type of junction</td>
  <td><code>coordinate</code> <code>subordinate</code></td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td><code>string</code></td>
  <td>lexical lemma</td>
  <td><code>ὁ</code> <code>καί</code></td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td><code>string</code></td>
  <td>ln</td>
  <td><code>92.24</code> <code>92.11</code></td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td><code>string</code></td>
  <td>verbal mood</td>
  <td><code>indicative</code> <code>participle</code></td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td><code>string</code></td>
  <td>morphological code</td>
  <td><code>CONJ</code> <code>PREP</code></td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td><code>string</code></td>
  <td>lemma normalized</td>
  <td><code>καί</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td><code>string</code></td>
  <td>annotation of linguistic nature</td>
  <td><code>discontinuous discourse</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td><code>string</code></td>
  <td>grammatical number</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td><code>string</code></td>
  <td>grammatical person</td>
  <td><code>third</code> <code>second</code></td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute punctuation</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td><code>string</code></td>
  <td>biblical reference with word counting</td>
  <td><code>1CO 10:1!1</code> <code>1CO 10:1!10</code></td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td><code>string</code></td>
  <td>number of referent</td>
  <td><code>n40005001015</code> <code>n43014023002</code></td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute rela</td>
  <td><code>Appo</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td><code>string</code></td>
  <td>syntactical rule</td>
  <td><code>DetNP</code> <code>PrepNp</code></td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td><code>integer</code></td>
  <td>strong number</td>
  <td><code>3588</code> <code>2532</code></td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute subjrefspec</td>
  <td><code>n46003022002</code> <code>n66001009002</code></td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td><code>string</code></td>
  <td>verbal tense</td>
  <td><code>aorist</code> <code>present</code></td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td><code>string</code></td>
  <td>the text of a word</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute typ</td>
  <td><code>NP</code> <code>PP</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td><code>string</code></td>
  <td>word in unicode characters plus material after it</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td><code>string</code></td>
  <td>verbal voice</td>
  <td><code>active</code> <code>passive</code></td>
</tr>
</tbody>
</table>

<h2>subphrase</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td><code>string</code></td>
  <td>material after the end of the word</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute before</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td><code>string</code></td>
  <td>grammatical case</td>
  <td><code>nominative</code> <code>accusative</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute criticalsign</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td><code>string</code></td>
  <td>grammatical degree</td>
  <td><code>comparative</code> <code>superlative</code></td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td><code>integer</code></td>
  <td>1 if the word is out of sequence in the xml</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td><code>string</code></td>
  <td>domain</td>
  <td><code>092004</code> <code>089017</code></td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute framespec</td>
  <td><code>A0:n00000000000</code> <code>A1:n00000000000</code></td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td><code>string</code></td>
  <td>grammatical gender</td>
  <td><code>masculine</code> <code>feminine</code></td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td><code>string</code></td>
  <td>short translation</td>
  <td><code>the</code> <code>and</code></td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td><code>string</code></td>
  <td>xml id</td>
  <td><code>n40001001001</code> <code>n40001001002</code></td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td><code>string</code></td>
  <td>lexical lemma</td>
  <td><code>ὁ</code> <code>καί</code></td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td><code>string</code></td>
  <td>ln</td>
  <td><code>92.24</code> <code>92.11</code></td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td><code>string</code></td>
  <td>verbal mood</td>
  <td><code>indicative</code> <code>participle</code></td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td><code>string</code></td>
  <td>morphological code</td>
  <td><code>CONJ</code> <code>PREP</code></td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td><code>string</code></td>
  <td>lemma normalized</td>
  <td><code>καί</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td><code>string</code></td>
  <td>grammatical number</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td><code>string</code></td>
  <td>grammatical person</td>
  <td><code>third</code> <code>second</code></td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute punctuation</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td><code>string</code></td>
  <td>biblical reference with word counting</td>
  <td><code>1CO 10:1!1</code> <code>1CO 10:1!10</code></td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td><code>string</code></td>
  <td>number of referent</td>
  <td><code>n40005001015</code> <code>n43014023002</code></td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td><code>integer</code></td>
  <td>strong number</td>
  <td><code>3588</code> <code>2532</code></td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute subjrefspec</td>
  <td><code>n46003022002</code> <code>n66001009002</code></td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td><code>string</code></td>
  <td>verbal tense</td>
  <td><code>aorist</code> <code>present</code></td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td><code>string</code></td>
  <td>the text of a word</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td><code>string</code></td>
  <td>word in unicode characters plus material after it</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td><code>string</code></td>
  <td>verbal voice</td>
  <td><code>active</code> <code>passive</code></td>
</tr>
</tbody>
</table>

<h2>word</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td><code>string</code></td>
  <td>material after the end of the word</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute before</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute book_short</td>
  <td><code>LUK</code> <code>ACT</code></td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td><code>string</code></td>
  <td>grammatical case</td>
  <td><code>nominative</code> <code>accusative</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>chapter number, from ref attribute in xml</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute cls</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute criticalsign</td>
  <td><code>—</code> <code>(</code></td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td><code>string</code></td>
  <td>grammatical degree</td>
  <td><code>comparative</code> <code>superlative</code></td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td><code>integer</code></td>
  <td>1 if the word is out of sequence in the xml</td>
  <td><code>1</code></td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td><code>string</code></td>
  <td>domain</td>
  <td><code>092004</code> <code>089017</code></td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute framespec</td>
  <td><code>A0:n00000000000</code> <code>A1:n00000000000</code></td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute function</td>
  <td><code>Pred</code> <code>Subj</code></td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td><code>string</code></td>
  <td>grammatical gender</td>
  <td><code>masculine</code> <code>feminine</code></td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td><code>string</code></td>
  <td>short translation</td>
  <td><code>the</code> <code>and</code></td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td><code>string</code></td>
  <td>xml id</td>
  <td><code>n40001001001</code> <code>n40001001002</code></td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td><code>string</code></td>
  <td>lexical lemma</td>
  <td><code>ὁ</code> <code>καί</code></td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td><code>string</code></td>
  <td>ln</td>
  <td><code>92.24</code> <code>92.11</code></td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td><code>string</code></td>
  <td>verbal mood</td>
  <td><code>indicative</code> <code>participle</code></td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td><code>string</code></td>
  <td>morphological code</td>
  <td><code>CONJ</code> <code>PREP</code></td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td><code>string</code></td>
  <td>lemma normalized</td>
  <td><code>καί</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td><code>string</code></td>
  <td>annotation of linguistic nature</td>
  <td><code>discontinuous discourse</code></td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td><code>integer</code></td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td><code>string</code></td>
  <td>grammatical number</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> <code>plural</code></td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td><code>string</code></td>
  <td>grammatical person</td>
  <td><code>third</code> <code>second</code></td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute punctuation</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td><code>string</code></td>
  <td>biblical reference with word counting</td>
  <td><code>1CO 10:1!1</code> <code>1CO 10:1!10</code></td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td><code>string</code></td>
  <td>number of referent</td>
  <td><code>n40005001015</code> <code>n43014023002</code></td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute rela</td>
  <td><code>Appo</code></td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td><code>string</code></td>
  <td>role</td>
  <td><code>v</code> <code>adv</code></td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td><code>integer</code></td>
  <td>strong number</td>
  <td><code>3588</code> <code>2532</code></td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td><code>string</code></td>
  <td>this is XML attribute subjrefspec</td>
  <td><code>n46003022002</code> <code>n66001009002</code></td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td><code>string</code></td>
  <td>verbal tense</td>
  <td><code>aorist</code> <code>present</code></td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td><code>string</code></td>
  <td>the text of a word</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td><code>modifier-scope</code> <code>common</code></td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td><code>string</code></td>
  <td>word in unicode characters plus material after it</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td><code>integer</code></td>
  <td>verse number, from ref attribute in xml</td>
  <td><code>10</code> <code>12</code></td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td><code>string</code></td>
  <td>verbal voice</td>
  <td><code>active</code> <code>passive</code></td>
</tr>
</tbody>
</table>
