# Copyright 2024 Tomas Brabec
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import RstWriterTestUtils
import docutils
import docutils.core
import b1rst.writers.YamlWriter
import b1rst.parsers.html.Bs4HtmlParser

def suite():
    s = RstWriterTestUtils.PublishTestSuite(
        test_class=RstWriterTestUtils.WriterNoTransformTestCase,
        writer_name='',
        writer_class=b1rst.writers.YamlWriter.YamlWriter,
        parser_class=b1rst.parsers.html.Bs4HtmlParser.Bs4HtmlParser)
    s.generateTests(totest)
    return s

totest = {}

#
# emphasis
#
totest['emphasis'] = [
["""\
<emph>emphasis emph</emph>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - emphasis:
      children:
      - emphasis emph
"""],
["""\
<i>emphasis i</i>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - emphasis:
      children:
      - emphasis i
"""],
["""\
<emph>multi
line</emph>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - emphasis:
      children:
      - 'multi

        line'
"""],
["""\
text with <emph>emphasized</emph> part
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'text with '
  - emphasis:
      children:
      - emphasized
  - ' part'
"""],
[u"""\
l'<emph>emphasis</emph> with the <emph>emphasis</emph>' apostrophe.
l\u2019<emph>emphasis</emph> with the <emph>emphasis</emph>\u2019 apostrophe.
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - l'
  - emphasis:
      children:
      - emphasis
  - ' with the '
  - emphasis:
      children:
      - emphasis
  - "' apostrophe.\\nl\\u2019"
  - emphasis:
      children:
      - emphasis
  - ' with the '
  - emphasis:
      children:
      - emphasis
  - "\\u2019 apostrophe."
"""],
["""\
<emph>emphasized sentence
across lines</emph>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - emphasis:
      children:
      - 'emphasized sentence

        across lines'
"""],
["""\
Emphasized asterisk: <emph>*</emph>

Emphasized double asterisk: <emph>**</emph>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'Emphasized asterisk: '
  - emphasis:
      children:
      - '*'
  - '


    Emphasized double asterisk: '
  - emphasis:
      children:
      - '**'
"""],
]


#
# strong
#
totest['strong'] = [
["""\
<b>strong b</b>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - strong:
      children:
      - strong b
"""],
["""\
<strong>strong strong</strong>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - strong:
      children:
      - strong strong
"""],
["""\
<b>multi
line</b>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - strong:
      children:
      - 'multi

        line'
"""],
["""\
text with <b>strong</b> part
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'text with '
  - strong:
      children:
      - strong
  - ' part'
"""],
[u"""\
l'<b>strong</b> and l\u2019<b>strong</b> with apostrophe
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - l'
  - strong:
      children:
      - strong
  - " and l\\u2019"
  - strong:
      children:
      - strong
  - ' with apostrophe'
"""],
["""\
Strong asterisk: <b>*</b>

Strong double asterisk: <b>**</b>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'Strong asterisk: '
  - strong:
      children:
      - '*'
  - '


    Strong double asterisk: '
  - strong:
      children:
      - '**'
"""],
]


#
# literal
#
totest['literal'] = [
["""\
<tt>literal tt</tt>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - literal tt
"""],
["""\
<code>literal code</code>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - literal code
"""],
["""\
<tt>multi
line</tt>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - 'multi

        line'
"""],
["""\
text with <tt>literal</tt> part
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'text with '
  - literal:
      children:
      - literal
  - ' part'
"""],
[r"""
<tt>\literal</tt>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - \\literal
"""],
[r"""
<tt>lite\ral</tt>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - lite\\ral
"""],
[r"""
<tt>literal\</tt>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - literal:
      children:
      - literal\\
"""],
[u"""\
l'<tt>literal</tt> and l\u2019<tt>literal</tt> with apostrophe
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - l'
  - literal:
      children:
      - literal
  - " and l\\u2019"
  - literal:
      children:
      - literal
  - ' with apostrophe'
"""],
["""\
Python <tt>list</tt>s use square bracket syntax.
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - 'Python '
  - literal:
      children:
      - list
  - s use square bracket syntax.
"""],
]

#
# reference
#
#TODO totest['references'] = [
#TODO ["""\
#TODO ref_
#TODO """,
#TODO """\
#TODO ref_
#TODO """],
#TODO [u"""\
#TODO l'ref_ and l\u2019ref_ with apostrophe
#TODO """,
#TODO u"""\
#TODO l'ref_ and l\u2019ref_ with apostrophe
#TODO """],
#TODO [u"""\
#TODO quoted 'ref_', quoted "ref_",
#TODO quoted \u2018ref_\u2019, quoted \u201cref_\u201d,
#TODO quoted \xabref_\xbb,
#TODO but not 'ref ref'_, "ref ref"_, \u2018ref ref\u2019_,
#TODO \u201cref ref\u201d_, or \xabref ref\xbb_
#TODO """,
#TODO u"""\
#TODO quoted 'ref_', quoted "ref_",
#TODO quoted \u2018ref_\u2019, quoted \u201cref_\u201d,
#TODO quoted \xabref_\xbb,
#TODO but not 'ref ref'_, "ref ref"_, \u2018ref ref\u2019_,
#TODO \u201cref ref\u201d_, or \xabref ref\xbb_
#TODO """],
#TODO ["""\
#TODO ref__
#TODO """,
#TODO """\
#TODO ref__
#TODO """],
#TODO [u"""\
#TODO l'ref__ and l\u2019ref__ with apostrophe
#TODO """,
#TODO u"""\
#TODO l'ref__ and l\u2019ref__ with apostrophe
#TODO """],
#TODO [u"""\
#TODO quoted 'ref__', quoted "ref__",
#TODO quoted \u2018ref__\u2019, quoted \u201cref__\u201d,
#TODO quoted \xabref__\xbb,
#TODO but not 'ref ref'__, "ref ref"__, \u2018ref ref\u2019__,
#TODO \u201cref ref\u201d__, or \xabref ref\xbb__
#TODO """,
#TODO u"""\
#TODO quoted 'ref__', quoted "ref__",
#TODO quoted \u2018ref__\u2019, quoted \u201cref__\u201d,
#TODO quoted \xabref__\xbb,
#TODO but not 'ref ref'__, "ref ref"__, \u2018ref ref\u2019__,
#TODO \u201cref ref\u201d__, or \xabref ref\xbb__
#TODO """],
#TODO ["""\
#TODO ref_, r_, r_e-f_, -ref_, and anonymousref__,
#TODO but not _ref_ or __attr__ or object.__attr__
#TODO """,
#TODO """\
#TODO ref_, r_, r_e-f_, -ref_, and anonymousref__,
#TODO but not _ref_ or __attr__ or object.__attr__
#TODO """],
#TODO ]


#TODO totest['phrase_references'] = [
#TODO ["""\
#TODO `phrase reference`_
#TODO """,
#TODO """\
#TODO `phrase reference`_
#TODO """],
#TODO [u"""\
#TODO l'`phrase reference`_ and l\u2019`phrase reference`_ with apostrophe
#TODO """,
#TODO u"""\
#TODO l'`phrase reference`_ and l\u2019`phrase reference`_ with apostrophe
#TODO """],
#TODO [u"""\
#TODO quoted '`phrase reference`_', quoted "`phrase reference`_",
#TODO quoted \u2018`phrase reference`_\u2019,
#TODO quoted \u201c`phrase reference`_\u201d,
#TODO quoted \xab`phrase reference`_\xbb
#TODO """,
#TODO u"""\
#TODO quoted '`phrase reference`_', quoted "`phrase reference`_",
#TODO quoted \u2018`phrase reference`_\u2019,
#TODO quoted \u201c`phrase reference`_\u201d,
#TODO quoted \xab`phrase reference`_\xbb
#TODO """],
#TODO [u"""\
#TODO `'phrase reference'`_ with quotes, `"phrase reference"`_ with quotes,
#TODO `\u2018phrase reference\u2019`_ with quotes,
#TODO `\u201cphrase reference\u201d`_ with quotes,
#TODO `\xabphrase reference\xbb`_ with quotes
#TODO """,
#TODO u"""\
#TODO `'phrase reference'`_ with quotes, `"phrase reference"`_ with quotes,
#TODO `\u2018phrase reference\u2019`_ with quotes,
#TODO `\u201cphrase reference\u201d`_ with quotes,
#TODO `\xabphrase reference\xbb`_ with quotes
#TODO """],
#TODO ["""\
#TODO `anonymous reference`__
#TODO """,
#TODO """\
#TODO `anonymous reference`__
#TODO """],
#TODO [u"""\
#TODO l'`anonymous reference`__ and l\u2019`anonymous reference`__ with apostrophe
#TODO """,
#TODO u"""\
#TODO l'`anonymous reference`__ and l\u2019`anonymous reference`__ with apostrophe
#TODO """],
#TODO [u"""\
#TODO quoted '`anonymous reference`__', quoted "`anonymous reference`__",
#TODO quoted \u2018`anonymous reference`__\u2019,
#TODO quoted \u201c`anonymous reference`__\u201d,
#TODO quoted \xab`anonymous reference`__\xbb
#TODO """,
#TODO u"""\
#TODO quoted '`anonymous reference`__', quoted "`anonymous reference`__",
#TODO quoted \u2018`anonymous reference`__\u2019,
#TODO quoted \u201c`anonymous reference`__\u201d,
#TODO quoted \xab`anonymous reference`__\xbb
#TODO """],
#TODO [u"""\
#TODO `'anonymous reference'`__ with quotes, `"anonymous reference"`__ with quotes,
#TODO `\u2018anonymous reference\u2019`__ with quotes,
#TODO `\u201canonymous reference\u201d`__ with quotes,
#TODO `\xabanonymous reference\xbb`__ with quotes
#TODO """,
#TODO u"""\
#TODO `'anonymous reference'`__ with quotes, `"anonymous reference"`__ with quotes,
#TODO `\u2018anonymous reference\u2019`__ with quotes,
#TODO `\u201canonymous reference\u201d`__ with quotes,
#TODO `\xabanonymous reference\xbb`__ with quotes
#TODO """],
#TODO ["""\
#TODO `phrase reference
#TODO across lines`_
#TODO """,
#TODO """\
#TODO `phrase reference
#TODO across lines`_
#TODO """],
#TODO ["""\
#TODO `phrase\\`_ reference`_
#TODO """,
#TODO """\
#TODO `phrase\\`_ reference`_
#TODO """],
#TODO ["""\
#TODO Invalid phrase reference:
#TODO 
#TODO :role:`phrase reference`_
#TODO """,
#TODO """\
#TODO Invalid phrase reference:
#TODO 
#TODO :role:`phrase reference`_
#TODO """],
#TODO ["""\
#TODO Invalid phrase reference:
#TODO 
#TODO `phrase reference`:role:_
#TODO """,
#TODO """\
#TODO Invalid phrase reference:
#TODO 
#TODO `phrase reference`:role:_
#TODO """],
#TODO ["""\
#TODO `phrase reference_ without closing backquote
#TODO """,
#TODO """\
#TODO `phrase reference_ without closing backquote
#TODO """],
#TODO ["""\
#TODO `anonymous phrase reference__ without closing backquote
#TODO """,
#TODO """\
#TODO `anonymous phrase reference__ without closing backquote
#TODO """],
#TODO ]



totest['embedded_URIs'] = [
["""\
<a href="https://www.python.org/">Python</a>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - reference:
      attrs:
        name: Python
        refuri: https://www.python.org/
      children:
      - Python
"""],
["""\
<a href="https://www.python.org/">Python</a>
<a href="https://www.w3schools.com">W3Schools.com</a>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - reference:
      attrs:
        name: Python
        refuri: https://www.python.org/
      children:
      - Python
  - reference:
      attrs:
        name: W3Schools.com
        refuri: https://www.w3schools.com
      children:
      - W3Schools.com
"""],
#TODO # Anonymous URI references resolve to normal ones!
#TODO ["""\
#TODO `anonymous reference <http://example.com>`__
#TODO """,
#TODO """\
#TODO `anonymous reference <http://example.com>`_
#TODO """],
["""\
<a href="mailto:jdoe@example.com">embedded email address</a>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - reference:
      attrs:
        name: embedded email address
        refuri: mailto:jdoe@example.com
      children:
      - embedded email address
"""],
#TODO ["""\
#TODO Relative URIs' reference text can be omitted:
#TODO 
#TODO `<reference>`_
#TODO 
#TODO `<anonymous>`__
#TODO """,
#TODO # A relative anonymous reference aliases with a normal relative reference
#TODO """\
#TODO Relative URIs' reference text can be omitted:
#TODO 
#TODO `<reference>`_
#TODO 
#TODO `<anonymous>`_
#TODO """],
]


#TODO totest['embedded_aliases'] = [
#TODO ["""\
#TODO `phrase reference <alias_>`_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="phrase reference" refname="alias">
#TODO             phrase reference
#TODO         <target names="phrase\\ reference" refname="alias">
#TODO """],
#TODO ["""\
#TODO `anonymous reference <alias_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="anonymous reference" refname="alias">
#TODO             anonymous reference
#TODO """],
#TODO ["""\
#TODO `embedded alias on next line
#TODO <alias_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="embedded alias on next line" refname="alias">
#TODO             embedded alias on next line
#TODO """],
#TODO ["""\
#TODO `embedded alias across lines <alias
#TODO phrase_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="embedded alias across lines" refname="alias phrase">
#TODO             embedded alias across lines
#TODO """],
#TODO ["""\
#TODO `embedded alias with whitespace <alias 
#TODO long  phrase_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="embedded alias with whitespace" refname="alias long phrase">
#TODO             embedded alias with whitespace
#TODO """],
#TODO ["""\
#TODO `<embedded alias with whitespace_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="embedded alias with whitespace" refname="embedded alias with whitespace">
#TODO             embedded alias with whitespace
#TODO """],
#TODO [r"""
#TODO `no embedded alias (whitespace inside bracket) < alias_ >`__
#TODO 
#TODO `no embedded alias (no preceding whitespace)<alias_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference anonymous="1" name="no embedded alias (whitespace inside bracket) < alias_ >">
#TODO             no embedded alias (whitespace inside bracket) < alias_ >
#TODO     <paragraph>
#TODO         <reference anonymous="1" name="no embedded alias (no preceding whitespace)<alias_>">
#TODO             no embedded alias (no preceding whitespace)<alias_>
#TODO """],
#TODO [r"""
#TODO `anonymous reference <alias\ with\\ escaped \:characters_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="anonymous reference" refname="aliaswith\\ escaped :characters">
#TODO             anonymous reference
#TODO """],
#TODO [r"""
#TODO `anonymous reference <alias\ with\\ escaped \:characters_>`__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference name="anonymous reference" refname="aliaswith\\ escaped :characters">
#TODO             anonymous reference
#TODO """],
#TODO ]


#TODO totest['inline_targets'] = [
#TODO ["""\
#TODO _`target`
#TODO 
#TODO Here is _`another target` in some text. And _`yet
#TODO another target`, spanning lines.
#TODO 
#TODO _`Here is  a    TaRgeT` with case and spacial difficulties.
#TODO """,
#TODO """\
#TODO _`target`
#TODO 
#TODO Here is _`another target` in some text. And _`yet
#TODO another target`, spanning lines.
#TODO 
#TODO _`Here is  a    TaRgeT` with case and spacial difficulties.
#TODO """],
#TODO [u"""\
#TODO l'_`target1` and l\u2019_`target2` with apostrophe
#TODO """,
#TODO u"""\
#TODO l'_`target1` and l\u2019_`target2` with apostrophe
#TODO """],
#TODO [u"""\
#TODO quoted '_`target1`', quoted "_`target2`",
#TODO quoted \u2018_`target3`\u2019, quoted \u201c_`target4`\u201d,
#TODO quoted \xab_`target5`\xbb
#TODO """,
#TODO u"""\
#TODO quoted '_`target1`', quoted "_`target2`",
#TODO quoted \u2018_`target3`\u2019, quoted \u201c_`target4`\u201d,
#TODO quoted \xab_`target5`\xbb
#TODO """],
#TODO [u"""\
#TODO _`'target1'` with quotes, _`"target2"` with quotes,
#TODO _`\u2018target3\u2019` with quotes, _`\u201ctarget4\u201d` with quotes,
#TODO _`\xabtarget5\xbb` with quotes
#TODO """,
#TODO u"""\
#TODO _`'target1'` with quotes, _`"target2"` with quotes,
#TODO _`\u2018target3\u2019` with quotes, _`\u201ctarget4\u201d` with quotes,
#TODO _`\xabtarget5\xbb` with quotes
#TODO """],
#TODO ["""\
#TODO But this isn't a _target; targets require backquotes.
#TODO 
#TODO And _`this`_ is just plain confusing.
#TODO """,
#TODO """\
#TODO But this isn't a _target; targets require backquotes.
#TODO 
#TODO And _`this`_ is just plain confusing.
#TODO """],
#TODO ["""\
#TODO _`inline target without closing backquote
#TODO """,
#TODO """\
#TODO _`inline target without closing backquote
#TODO """],
#TODO ]


#TODO totest['footnote_reference'] = [
#TODO ["""\
#TODO [1]_
#TODO """,
#TODO """\
#TODO [1]_
#TODO """],
#TODO ["""\
#TODO [#]_
#TODO """,
#TODO """\
#TODO [#]_
#TODO """],
#TODO ["""\
#TODO [#label]_
#TODO """,
#TODO """\
#TODO [#label]_
#TODO """],
#TODO ["""\
#TODO [*]_
#TODO """,
#TODO """\
#TODO [*]_
#TODO """],
#TODO ["""\
#TODO [*label]_
#TODO """,
#TODO """\
#TODO [*label]_
#TODO """],
#TODO ["""\
#TODO Back to back: [*]_ [#label]_ [#]_ [2]_ [1]_ [*label]_
#TODO """,
#TODO """\
#TODO Back to back: [*]_ [#label]_ [#]_ [2]_ [1]_ [*label]_
#TODO """],
#TODO ["""\
#TODO Adjacent footnote refs are not possible: [*]_[#label]_ [#]_[2]_ [1]_[*]_
#TODO """,
#TODO """\
#TODO Adjacent footnote refs are not possible: [*]_[#label]_ [#]_[2]_ [1]_[*]_
#TODO """],
#TODO ]


#TODO totest['citation_reference'] = [
#TODO ["""\
#TODO [citation]_
#TODO """,
#TODO """\
#TODO [citation]_
#TODO """],
#TODO ["""\
#TODO [citation]_ and [cit-ation]_ and [cit.ation]_ and [CIT1]_ but not [CIT 1]_
#TODO """,
#TODO """\
#TODO [citation]_ and [cit-ation]_ and [cit.ation]_ and [CIT1]_ but not [CIT 1]_
#TODO """],
#TODO ["""\
#TODO Adjacent citation refs are not possible: [citation]_[CIT1]_
#TODO """,
#TODO """\
#TODO Adjacent citation refs are not possible: [citation]_[CIT1]_
#TODO """],
#TODO ]


#TODO totest['substitution_references'] = [
#TODO ["""\
#TODO |subref|
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <substitution_reference refname="subref">
#TODO             subref
#TODO """],
#TODO ["""\
#TODO |subref|_ and |subref|__
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <reference refname="subref">
#TODO             <substitution_reference refname="subref">
#TODO                 subref
#TODO          and \n\
#TODO         <reference anonymous="1">
#TODO             <substitution_reference refname="subref">
#TODO                 subref
#TODO """],
#TODO ["""\
#TODO |substitution reference|
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <substitution_reference refname="substitution reference">
#TODO             substitution reference
#TODO """],
#TODO ["""\
#TODO |substitution
#TODO reference|
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <substitution_reference refname="substitution reference">
#TODO             substitution
#TODO             reference
#TODO """],
#TODO ["""\
#TODO |substitution reference without closing verbar
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <problematic ids="id2" refid="id1">
#TODO             |
#TODO         substitution reference without closing verbar
#TODO     <system_message backrefs="id2" ids="id1" level="2" line="1" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Inline substitution_reference start-string without end-string.
#TODO """],
#TODO ["""\
#TODO first | then || and finally |||
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         first | then || and finally |||
#TODO """],
#TODO ]


#TODO totest['standalone_hyperlink'] = [
#TODO ["""\
#TODO http://www.standalone.hyperlink.com
#TODO 
#TODO http:/one-slash-only.absolute.path
#TODO 
#TODO [http://example.com]
#TODO 
#TODO (http://example.com)
#TODO 
#TODO <http://example.com>
#TODO 
#TODO http://[1080:0:0:0:8:800:200C:417A]/IPv6address.html
#TODO 
#TODO http://[3ffe:2a00:100:7031::1] (the final "]" is ambiguous in text)
#TODO 
#TODO http://[3ffe:2a00:100:7031::1]/
#TODO 
#TODO mailto:someone@somewhere.com
#TODO 
#TODO news:comp.lang.python
#TODO 
#TODO An email address in a sentence: someone@somewhere.com.
#TODO 
#TODO ftp://ends.with.a.period.
#TODO 
#TODO (a.question.mark@end?)
#TODO """,
#TODO """\
#TODO http://www.standalone.hyperlink.com
#TODO 
#TODO http:/one-slash-only.absolute.path
#TODO 
#TODO [http://example.com]
#TODO 
#TODO (http://example.com)
#TODO 
#TODO <http://example.com>
#TODO 
#TODO http://[1080:0:0:0:8:800:200C:417A]/IPv6address.html
#TODO 
#TODO http://[3ffe:2a00:100:7031::1] (the final "]" is ambiguous in text)
#TODO 
#TODO http://[3ffe:2a00:100:7031::1]/
#TODO 
#TODO mailto:someone@somewhere.com
#TODO 
#TODO news:comp.lang.python
#TODO 
#TODO An email address in a sentence: someone@somewhere.com.
#TODO 
#TODO ftp://ends.with.a.period.
#TODO 
#TODO (a.question.mark@end?)
#TODO """],
#TODO [r"""
#TODO Valid URLs with escaped markup characters:
#TODO 
#TODO http://example.com/\*content\*/whatever
#TODO 
#TODO http://example.com/\*content*/whatever
#TODO """,
#TODO """\
#TODO Valid URLs with escaped markup characters:
#TODO 
#TODO http://example.com/*content*/whatever
#TODO 
#TODO http://example.com/*content*/whatever
#TODO """],
#TODO ["""\
#TODO Valid URLs may end with punctuation inside "<>":
#TODO 
#TODO <http://example.org/ends-with-dot.>
#TODO """,
#TODO """\
#TODO Valid URLs may end with punctuation inside "<>":
#TODO 
#TODO <http://example.org/ends-with-dot.>
#TODO """],
#TODO ["""\
#TODO Valid URLs with interesting endings:
#TODO 
#TODO http://example.org/ends-with-pluses++
#TODO """,
#TODO """\
#TODO Valid URLs with interesting endings:
#TODO 
#TODO http://example.org/ends-with-pluses++
#TODO """],
#TODO ["""\
#TODO None of these are standalone hyperlinks (their "schemes"
#TODO are not recognized): signal:noise, a:b.
#TODO """,
#TODO """\
#TODO None of these are standalone hyperlinks (their "schemes"
#TODO are not recognized): signal:noise, a:b.
#TODO """],
#TODO ["""\
#TODO Escaped email addresses are not recognized: test\\@example.org
#TODO """,
#TODO """\
#TODO Escaped email addresses are not recognized: test@example.org
#TODO """],
#TODO ]

#TODO totest['markup recognition rules'] = [
#TODO ["""\
#TODO __This__ should be left alone.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         __This__ should be left alone.
#TODO """],
#TODO [r"""
#TODO Character-level m\ *a*\ **r**\ ``k``\ `u`:title:\p
#TODO with backslash-escaped whitespace, including new\
#TODO lines.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Character-level m
#TODO         <emphasis>
#TODO             a
#TODO         <strong>
#TODO             r
#TODO         <literal>
#TODO             k
#TODO         <title_reference>
#TODO             u
#TODO         p
#TODO         with backslash-escaped whitespace, including newlines.
#TODO """],
#TODO [u"""\
#TODO text-*separated*\u2010*by*\u2011*various*\u2012*dashes*\u2013*and*\u2014*hyphens*.
#TODO \u00bf*punctuation*? \u00a1*examples*!\u00a0*no-break-space*\u00a0.
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         text-
#TODO         <emphasis>
#TODO             separated
#TODO         \u2010
#TODO         <emphasis>
#TODO             by
#TODO         \u2011
#TODO         <emphasis>
#TODO             various
#TODO         \u2012
#TODO         <emphasis>
#TODO             dashes
#TODO         \u2013
#TODO         <emphasis>
#TODO             and
#TODO         \u2014
#TODO         <emphasis>
#TODO             hyphens
#TODO         .
#TODO         \xbf
#TODO         <emphasis>
#TODO             punctuation
#TODO         ? \xa1
#TODO         <emphasis>
#TODO             examples
#TODO         !\xa0
#TODO         <emphasis>
#TODO             no-break-space
#TODO         \u00a0.
#TODO """],
#TODO # Whitespace characters:
#TODO #  \u180e*MONGOLIAN VOWEL SEPARATOR*\u180e,   fails in Python 2.6
#TODO [u"""\
#TODO text separated by
#TODO *newline*
#TODO or *space* or one of
#TODO \xa0*NO-BREAK SPACE*\xa0,
#TODO \u1680*OGHAM SPACE MARK*\u1680,
#TODO \u2000*EN QUAD*\u2000,
#TODO \u2001*EM QUAD*\u2001,
#TODO \u2002*EN SPACE*\u2002,
#TODO \u2003*EM SPACE*\u2003,
#TODO \u2004*THREE-PER-EM SPACE*\u2004,
#TODO \u2005*FOUR-PER-EM SPACE*\u2005,
#TODO \u2006*SIX-PER-EM SPACE*\u2006,
#TODO \u2007*FIGURE SPACE*\u2007,
#TODO \u2008*PUNCTUATION SPACE*\u2008,
#TODO \u2009*THIN SPACE*\u2009,
#TODO \u200a*HAIR SPACE*\u200a,
#TODO \u202f*NARROW NO-BREAK SPACE*\u202f,
#TODO \u205f*MEDIUM MATHEMATICAL SPACE*\u205f,
#TODO \u3000*IDEOGRAPHIC SPACE*\u3000,
#TODO \u2028*LINE SEPARATOR*\u2028
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         text separated by
#TODO         <emphasis>
#TODO             newline
#TODO         \n\
#TODO         or \n\
#TODO         <emphasis>
#TODO             space
#TODO          or one of
#TODO         \xa0
#TODO         <emphasis>
#TODO             NO-BREAK SPACE
#TODO         \xa0,
#TODO         \u1680
#TODO         <emphasis>
#TODO             OGHAM SPACE MARK
#TODO         \u1680,
#TODO         \u2000
#TODO         <emphasis>
#TODO             EN QUAD
#TODO         \u2000,
#TODO         \u2001
#TODO         <emphasis>
#TODO             EM QUAD
#TODO         \u2001,
#TODO         \u2002
#TODO         <emphasis>
#TODO             EN SPACE
#TODO         \u2002,
#TODO         \u2003
#TODO         <emphasis>
#TODO             EM SPACE
#TODO         \u2003,
#TODO         \u2004
#TODO         <emphasis>
#TODO             THREE-PER-EM SPACE
#TODO         \u2004,
#TODO         \u2005
#TODO         <emphasis>
#TODO             FOUR-PER-EM SPACE
#TODO         \u2005,
#TODO         \u2006
#TODO         <emphasis>
#TODO             SIX-PER-EM SPACE
#TODO         \u2006,
#TODO         \u2007
#TODO         <emphasis>
#TODO             FIGURE SPACE
#TODO         \u2007,
#TODO         \u2008
#TODO         <emphasis>
#TODO             PUNCTUATION SPACE
#TODO         \u2008,
#TODO         \u2009
#TODO         <emphasis>
#TODO             THIN SPACE
#TODO         \u2009,
#TODO         \u200a
#TODO         <emphasis>
#TODO             HAIR SPACE
#TODO         \u200a,
#TODO         \u202f
#TODO         <emphasis>
#TODO             NARROW NO-BREAK SPACE
#TODO         \u202f,
#TODO         \u205f
#TODO         <emphasis>
#TODO             MEDIUM MATHEMATICAL SPACE
#TODO         \u205f,
#TODO         \u3000
#TODO         <emphasis>
#TODO             IDEOGRAPHIC SPACE
#TODO         \u3000,
#TODO     <paragraph>
#TODO         <emphasis>
#TODO             LINE SEPARATOR
#TODO """],
#TODO [u"""\
#TODO inline markup separated by non-ASCII whitespace
#TODO \xa0**NO-BREAK SPACE**\xa0, \xa0``NO-BREAK SPACE``\xa0, \xa0`NO-BREAK SPACE`\xa0,
#TODO \u2000**EN QUAD**\u2000, \u2000``EN QUAD``\u2000, \u2000`EN QUAD`\u2000,
#TODO \u202f**NARROW NBSP**\u202f, \u202f``NARROW NBSP``\u202f, \u202f`NARROW NBSP`\u202f,
#TODO """,                                      
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         inline markup separated by non-ASCII whitespace
#TODO         \xa0
#TODO         <strong>
#TODO             NO-BREAK SPACE
#TODO         \xa0, \xa0
#TODO         <literal>
#TODO             NO-BREAK SPACE
#TODO         \xa0, \xa0
#TODO         <title_reference>
#TODO             NO-BREAK SPACE
#TODO         \xa0,
#TODO         \u2000
#TODO         <strong>
#TODO             EN QUAD
#TODO         \u2000, \u2000
#TODO         <literal>
#TODO             EN QUAD
#TODO         \u2000, \u2000
#TODO         <title_reference>
#TODO             EN QUAD
#TODO         \u2000,
#TODO         \u202f
#TODO         <strong>
#TODO             NARROW NBSP
#TODO         \u202f, \u202f
#TODO         <literal>
#TODO             NARROW NBSP
#TODO         \u202f, \u202f
#TODO         <title_reference>
#TODO             NARROW NBSP
#TODO         \u202f,
#TODO """],
#TODO [u"""\
#TODO no inline markup due to whitespace inside and behind: *
#TODO newline
#TODO *
#TODO * space * or one of
#TODO *\xa0NO-BREAK SPACE\xa0*
#TODO *\u1680OGHAM SPACE MARK\u1680*
#TODO *\u2000EN QUAD\u2000*
#TODO *\u2001EM QUAD\u2001*
#TODO *\u2002EN SPACE\u2002*
#TODO *\u2003EM SPACE\u2003*
#TODO *\u2004THREE-PER-EM SPACE\u2004*
#TODO *\u2005FOUR-PER-EM SPACE\u2005*
#TODO *\u2006SIX-PER-EM SPACE\u2006*
#TODO *\u2007FIGURE SPACE\u2007*
#TODO *\u2008PUNCTUATION SPACE\u2008*
#TODO *\u2009THIN SPACE\u2009*
#TODO *\u200aHAIR SPACE\u200a*
#TODO *\u202fNARROW NO-BREAK SPACE\u202f*
#TODO *\u205fMEDIUM MATHEMATICAL SPACE\u205f*
#TODO *\u3000IDEOGRAPHIC SPACE\u3000*
#TODO *\u2028LINE SEPARATOR\u2028*
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         no inline markup due to whitespace inside and behind: *
#TODO         newline
#TODO         *
#TODO         * space * or one of
#TODO         *\xa0NO-BREAK SPACE\xa0*
#TODO         *\u1680OGHAM SPACE MARK\u1680*
#TODO         *\u2000EN QUAD\u2000*
#TODO         *\u2001EM QUAD\u2001*
#TODO         *\u2002EN SPACE\u2002*
#TODO         *\u2003EM SPACE\u2003*
#TODO         *\u2004THREE-PER-EM SPACE\u2004*
#TODO         *\u2005FOUR-PER-EM SPACE\u2005*
#TODO         *\u2006SIX-PER-EM SPACE\u2006*
#TODO         *\u2007FIGURE SPACE\u2007*
#TODO         *\u2008PUNCTUATION SPACE\u2008*
#TODO         *\u2009THIN SPACE\u2009*
#TODO         *\u200aHAIR SPACE\u200a*
#TODO         *\u202fNARROW NO-BREAK SPACE\u202f*
#TODO         *\u205fMEDIUM MATHEMATICAL SPACE\u205f*
#TODO         *\u3000IDEOGRAPHIC SPACE\u3000*
#TODO         *
#TODO         LINE SEPARATOR
#TODO         *"""],
#TODO [u"""\
#TODO no inline markup because of non-ASCII whitespace following /preceding the markup
#TODO **\xa0NO-BREAK SPACE\xa0** ``\xa0NO-BREAK SPACE\xa0`` `\xa0NO-BREAK SPACE\xa0`
#TODO **\u2000EN QUAD\u2000** ``\u2000EN QUAD\u2000`` `\u2000EN QUAD\u2000`
#TODO **\u202fNARROW NBSP\u202f** ``\u202fNARROW NBSP\u202f`` `\u202fNARROW NBSP\u202f`
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         no inline markup because of non-ASCII whitespace following /preceding the markup
#TODO         **\xa0NO-BREAK SPACE\xa0** ``\xa0NO-BREAK SPACE\xa0`` `\xa0NO-BREAK SPACE\xa0`
#TODO         **\u2000EN QUAD\u2000** ``\u2000EN QUAD\u2000`` `\u2000EN QUAD\u2000`
#TODO         **\u202fNARROW NBSP\u202f** ``\u202fNARROW NBSP\u202f`` `\u202fNARROW NBSP\u202f`\
#TODO """],
#TODO # « * » ‹ * › « * » ‹ * › « * » ‹ * › French,
#TODO [u"""\
#TODO "Quoted" markup start-string (matched openers & closers) -> no markup:
#TODO 
#TODO '*' "*" (*) <*> [*] {*}
#TODO ⁅*⁆
#TODO 
#TODO Some international quoting styles:
#TODO ‘*’ “*” English, ...,
#TODO „*“ ‚*‘ »*« ›*‹ German, Czech, ...,
#TODO „*” «*» Romanian,
#TODO “*„ ‘*‚ Greek,
#TODO 「*」 『*』traditional Chinese,
#TODO ”*” ’*’ »*» ›*› Swedish, Finnish,
#TODO „*” ‚*’ Polish,
#TODO „*” »*« ’*’ Hungarian,
#TODO 
#TODO But this is „*’ emphasized »*‹.
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         "Quoted" markup start-string (matched openers & closers) -> no markup:
#TODO     <paragraph>
#TODO         '*' "*" (*) <*> [*] {*}
#TODO         ⁅*⁆
#TODO     <paragraph>
#TODO         Some international quoting styles:
#TODO         ‘*’ “*” English, ...,
#TODO         „*“ ‚*‘ »*« ›*‹ German, Czech, ...,
#TODO         „*” «*» Romanian,
#TODO         “*„ ‘*‚ Greek,
#TODO         「*」 『*』traditional Chinese,
#TODO         ”*” ’*’ »*» ›*› Swedish, Finnish,
#TODO         „*” ‚*’ Polish,
#TODO         „*” »*« ’*’ Hungarian,
#TODO     <paragraph>
#TODO         But this is „
#TODO         <emphasis>
#TODO             ’ emphasized »
#TODO         ‹.
#TODO """],
#TODO ]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

