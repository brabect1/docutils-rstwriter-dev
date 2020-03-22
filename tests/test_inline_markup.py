#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2020 Tomas Brabec
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

def suite():
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter',
            test_class=RstWriterTestUtils.WriterNoTransformTestCase)
    s.generateTests(totest)
    return s

totest = {}

totest['emphasis'] = [
["""\
*emphasis*
""",
"""\
*emphasis*
"""],
[u"""\
l'*emphasis* with the *emphasis*' apostrophe.
l\u2019*emphasis* with the *emphasis*\u2019 apostrophe.
""",
u"""\
l'*emphasis* with the *emphasis*' apostrophe.
l\u2019*emphasis* with the *emphasis*\u2019 apostrophe.
"""],
["""\
*emphasized sentence
across lines*
""",
"""\
*emphasized sentence
across lines*
"""],
["""\
*emphasis without closing asterisk
""",
"""\
*emphasis without closing asterisk
"""],
[r"""some punctuation is allowed around inline markup, e.g.
/*emphasis*/, -*emphasis*-, and :*emphasis*: (delimiters),
(*emphasis*), [*emphasis*], <*emphasis*>, {*emphasis*} (open/close pairs)
*emphasis*., *emphasis*,, *emphasis*!, and *emphasis*\ (closing delimiters),

but not
)*emphasis*(, ]*emphasis*[, >*emphasis*>, }*emphasis*{ (close/open pairs),
(*), [*], '*' or '"*"' ("quoted" start-string),
x*2* or 2*x* (alphanumeric char before),
\*args or * (escaped, whitespace behind start-string),
or *the\* *stars\* *inside* (escaped, whitespace before end-string).

However, '*args' will trigger a warning and may be problematic.

what about *this**?
""",
"""\
some punctuation is allowed around inline markup, e.g.
/*emphasis*/, -*emphasis*-, and :*emphasis*: (delimiters),
(*emphasis*), [*emphasis*], <*emphasis*>, {*emphasis*} (open/close pairs)
*emphasis*., *emphasis*,, *emphasis*!, and *emphasis*(closing delimiters),

but not
)*emphasis*(, ]*emphasis*[, >*emphasis*>, }*emphasis*{ (close/open pairs),
(*), [*], '*' or '"*"' ("quoted" start-string),
x*2* or 2*x* (alphanumeric char before),
*args or * (escaped, whitespace behind start-string),
or *the* *stars* *inside* (escaped, whitespace before end-string).

However, '*args' will trigger a warning and may be problematic.

what about *this**?
"""],
[u"""\
Quotes around inline markup:

'*emphasis*' "*emphasis*" Straight,
‘*emphasis*’ “*emphasis*” English, ...,
« *emphasis* » ‹ *emphasis* › « *emphasis* » ‹ *emphasis* ›
« *emphasis* » ‹ *emphasis* › French,
„*emphasis*“ ‚*emphasis*‘ »*emphasis*« ›*emphasis*‹ German, Czech, ...,
„*emphasis*” «*emphasis*» Romanian,
“*emphasis*„ ‘*emphasis*‚ Greek,
「*emphasis*」 『*emphasis*』traditional Chinese,
”*emphasis*” ’*emphasis*’ »*emphasis*» ›*emphasis*› Swedish, Finnish,
„*emphasis*” ‚*emphasis*’ Polish,
„*emphasis*” »*emphasis*« ’*emphasis*’ Hungarian,
""",
u"""\
Quotes around inline markup:

'*emphasis*' "*emphasis*" Straight,
‘*emphasis*’ “*emphasis*” English, ...,
« *emphasis* » ‹ *emphasis* › « *emphasis* » ‹ *emphasis* ›
« *emphasis* » ‹ *emphasis* › French,
„*emphasis*“ ‚*emphasis*‘ »*emphasis*« ›*emphasis*‹ German, Czech, ...,
„*emphasis*” «*emphasis*» Romanian,
“*emphasis*„ ‘*emphasis*‚ Greek,
「*emphasis*」 『*emphasis*』traditional Chinese,
”*emphasis*” ’*emphasis*’ »*emphasis*» ›*emphasis*› Swedish, Finnish,
„*emphasis*” ‚*emphasis*’ Polish,
„*emphasis*” »*emphasis*« ’*emphasis*’ Hungarian,
"""],
[r"""
Emphasized asterisk: *\**

Emphasized double asterisk: *\***
""",
"""\
Emphasized asterisk: ***

Emphasized double asterisk: ****
"""],
]

totest['strong'] = [
["""\
**strong**
""",
"""\
**strong**
"""],
[u"""\
l'**strong** and l\u2019**strong** with apostrophe
""",
u"""\
l'**strong** and l\u2019**strong** with apostrophe
"""],
[u"""\
quoted '**strong**', quoted "**strong**",
quoted \u2018**strong**\u2019, quoted \u201c**strong**\u201d,
quoted \xab**strong**\xbb
""",
u"""\
quoted '**strong**', quoted "**strong**",
quoted \u2018**strong**\u2019, quoted \u201c**strong**\u201d,
quoted \xab**strong**\xbb
"""],
[r"""
(**strong**) but not (**) or '(** ' or x**2 or \**kwargs or **

(however, '**kwargs' will trigger a warning and may be problematic)
""",
"""\
(**strong**) but not (**) or '(** ' or x**2 or **kwargs or **

(however, '**kwargs' will trigger a warning and may be problematic)
"""],
["""\
Strong asterisk: *****

Strong double asterisk: ******
""",
"""\
Strong asterisk: *****

Strong double asterisk: ******
"""],
["""\
**strong without closing asterisks
""",
"""\
**strong without closing asterisks
"""],
]

#
# literal
#
totest['literal'] = [
["""\
``literal``
""",
"""\
``literal``
"""],
[r"""
``\literal``
""",
"""\
``\\literal``
"""],
[r"""
``lite\ral``
""",
"""\
``lite\\ral``
"""],
[r"""
``literal\``
""",
"""\
``literal\\``
"""],
[u"""\
l'``literal`` and l\u2019``literal`` with apostrophe
""",
u"""\
l'``literal`` and l\u2019``literal`` with apostrophe
"""],
[u"""\
quoted '``literal``', quoted "``literal``",
quoted \u2018``literal``\u2019, quoted \u201c``literal``\u201d,
quoted \xab``literal``\xbb
""",
u"""\
quoted '``literal``', quoted "``literal``",
quoted \u2018``literal``\u2019, quoted \u201c``literal``\u201d,
quoted \xab``literal``\xbb
"""],
[u"""\
``'literal'`` with quotes, ``"literal"`` with quotes,
``\u2018literal\u2019`` with quotes, ``\u201cliteral\u201d`` with quotes,
``\xabliteral\xbb`` with quotes
""",
u"""\
``'literal'`` with quotes, ``"literal"`` with quotes,
``\u2018literal\u2019`` with quotes, ``\u201cliteral\u201d`` with quotes,
``\xabliteral\xbb`` with quotes
"""],
[r"""
``literal ``TeX quotes'' & \backslash`` but not "``" or ``

(however, ``standalone TeX quotes'' will trigger a warning
and may be problematic)
""",
"""\
``literal ``TeX quotes'' & \\backslash`` but not "``" or ``

(however, ``standalone TeX quotes'' will trigger a warning
and may be problematic)
"""],
["""\
Find the ```interpreted text``` in this paragraph!
""",
"""\
Find the ```interpreted text``` in this paragraph!
"""],
["""\
``literal without closing backquotes
""",
"""\
``literal without closing backquotes
"""],
[r"""
Python ``list``\s use square bracket syntax.
""",
"""\
Python ``list``s use square bracket syntax.
"""],
[r"""
Blank after opening `` not allowed.
""",
"""\
Blank after opening `` not allowed.
"""],
[r"""
no blank ``after closing``continues`` literal.
""",
"""\
no blank ``after closing``continues`` literal.
"""],
[r"""
dot ``after closing``. is possible.
""",
"""\
dot ``after closing``. is possible.
"""],
]

#
# reference
#
totest['references'] = [
["""\
ref_
""",
"""\
ref_
"""],
[u"""\
l'ref_ and l\u2019ref_ with apostrophe
""",
u"""\
l'ref_ and l\u2019ref_ with apostrophe
"""],
[u"""\
quoted 'ref_', quoted "ref_",
quoted \u2018ref_\u2019, quoted \u201cref_\u201d,
quoted \xabref_\xbb,
but not 'ref ref'_, "ref ref"_, \u2018ref ref\u2019_,
\u201cref ref\u201d_, or \xabref ref\xbb_
""",
u"""\
quoted 'ref_', quoted "ref_",
quoted \u2018ref_\u2019, quoted \u201cref_\u201d,
quoted \xabref_\xbb,
but not 'ref ref'_, "ref ref"_, \u2018ref ref\u2019_,
\u201cref ref\u201d_, or \xabref ref\xbb_
"""],
["""\
ref__
""",
"""\
ref__
"""],
[u"""\
l'ref__ and l\u2019ref__ with apostrophe
""",
u"""\
l'ref__ and l\u2019ref__ with apostrophe
"""],
[u"""\
quoted 'ref__', quoted "ref__",
quoted \u2018ref__\u2019, quoted \u201cref__\u201d,
quoted \xabref__\xbb,
but not 'ref ref'__, "ref ref"__, \u2018ref ref\u2019__,
\u201cref ref\u201d__, or \xabref ref\xbb__
""",
u"""\
quoted 'ref__', quoted "ref__",
quoted \u2018ref__\u2019, quoted \u201cref__\u201d,
quoted \xabref__\xbb,
but not 'ref ref'__, "ref ref"__, \u2018ref ref\u2019__,
\u201cref ref\u201d__, or \xabref ref\xbb__
"""],
["""\
ref_, r_, r_e-f_, -ref_, and anonymousref__,
but not _ref_ or __attr__ or object.__attr__
""",
"""\
ref_, r_, r_e-f_, -ref_, and anonymousref__,
but not _ref_ or __attr__ or object.__attr__
"""],
]

totest['phrase_references'] = [
["""\
`phrase reference`_
""",
"""\
`phrase reference`_
"""],
[u"""\
l'`phrase reference`_ and l\u2019`phrase reference`_ with apostrophe
""",
u"""\
l'`phrase reference`_ and l\u2019`phrase reference`_ with apostrophe
"""],
[u"""\
quoted '`phrase reference`_', quoted "`phrase reference`_",
quoted \u2018`phrase reference`_\u2019,
quoted \u201c`phrase reference`_\u201d,
quoted \xab`phrase reference`_\xbb
""",
u"""\
quoted '`phrase reference`_', quoted "`phrase reference`_",
quoted \u2018`phrase reference`_\u2019,
quoted \u201c`phrase reference`_\u201d,
quoted \xab`phrase reference`_\xbb
"""],
[u"""\
`'phrase reference'`_ with quotes, `"phrase reference"`_ with quotes,
`\u2018phrase reference\u2019`_ with quotes,
`\u201cphrase reference\u201d`_ with quotes,
`\xabphrase reference\xbb`_ with quotes
""",
u"""\
`'phrase reference'`_ with quotes, `"phrase reference"`_ with quotes,
`\u2018phrase reference\u2019`_ with quotes,
`\u201cphrase reference\u201d`_ with quotes,
`\xabphrase reference\xbb`_ with quotes
"""],
["""\
`anonymous reference`__
""",
"""\
`anonymous reference`__
"""],
[u"""\
l'`anonymous reference`__ and l\u2019`anonymous reference`__ with apostrophe
""",
u"""\
l'`anonymous reference`__ and l\u2019`anonymous reference`__ with apostrophe
"""],
[u"""\
quoted '`anonymous reference`__', quoted "`anonymous reference`__",
quoted \u2018`anonymous reference`__\u2019,
quoted \u201c`anonymous reference`__\u201d,
quoted \xab`anonymous reference`__\xbb
""",
u"""\
quoted '`anonymous reference`__', quoted "`anonymous reference`__",
quoted \u2018`anonymous reference`__\u2019,
quoted \u201c`anonymous reference`__\u201d,
quoted \xab`anonymous reference`__\xbb
"""],
[u"""\
`'anonymous reference'`__ with quotes, `"anonymous reference"`__ with quotes,
`\u2018anonymous reference\u2019`__ with quotes,
`\u201canonymous reference\u201d`__ with quotes,
`\xabanonymous reference\xbb`__ with quotes
""",
u"""\
`'anonymous reference'`__ with quotes, `"anonymous reference"`__ with quotes,
`\u2018anonymous reference\u2019`__ with quotes,
`\u201canonymous reference\u201d`__ with quotes,
`\xabanonymous reference\xbb`__ with quotes
"""],
["""\
`phrase reference
across lines`_
""",
"""\
`phrase reference
across lines`_
"""],
["""\
`phrase\\`_ reference`_
""",
"""\
`phrase\\`_ reference`_
"""],
["""\
Invalid phrase reference:

:role:`phrase reference`_
""",
"""\
Invalid phrase reference:

:role:`phrase reference`_
"""],
["""\
Invalid phrase reference:

`phrase reference`:role:_
""",
"""\
Invalid phrase reference:

`phrase reference`:role:_
"""],
["""\
`phrase reference_ without closing backquote
""",
"""\
`phrase reference_ without closing backquote
"""],
["""\
`anonymous phrase reference__ without closing backquote
""",
"""\
`anonymous phrase reference__ without closing backquote
"""],
]

totest['embedded_URIs'] = [
["""\
`phrase reference <http://example.com>`_
""",
"""\
`phrase reference <http://example.com>`_
"""],
["""\
`anonymous reference <http://example.com>`__
""",
# Anonymous URI references resolve to normal ones!
"""\
`anonymous reference <http://example.com>`_
"""],
["""\
`embedded URI on next line
<http://example.com>`__
""",
"""\
`embedded URI on next line <http://example.com>`_
"""],
["""\
`embedded URI across lines <http://example.com/
long/path>`__
""",
"""\
`embedded URI across lines <http://example.com/long/path>`_
"""],
["""\
`embedded URI with whitespace <http://example.com/
long/path /and  /whitespace>`__
""",
"""\
`embedded URI with whitespace <http://example.com/long/path/and/whitespace>`_
"""],
[r"""
`embedded URI with escaped whitespace <http://example.com/a\
long/path\ and/some\ escaped\ whitespace>`__

`<omitted\ reference\ text\ with\ escaped\ whitespace>`__
""",
"""\
`embedded URI with escaped whitespace <http://example.com/a\ long/path\ and/some\ escaped\ whitespace>`_

`<omitted\ reference\ text\ with\ escaped\ whitespace>`_
"""],
["""\
`embedded email address <jdoe@example.com>`__

`embedded email address <mailto:jdoe@example.com>`__

`embedded email address broken across lines <jdoe
@example.com>`__
""",
"""\
`embedded email address <mailto:jdoe@example.com>`_

`embedded email address <mailto:jdoe@example.com>`_

`embedded email address broken across lines <mailto:jdoe@example.com>`_
"""],
[r"""`embedded URI with too much whitespace < http://example.com/
long/path /and  /whitespace >`__

`embedded URI with too much whitespace at end <http://example.com/
long/path /and  /whitespace >`__

`embedded URI with no preceding whitespace<http://example.com>`__

`escaped URI \<http://example.com>`__

See `HTML Anchors: \<a>`_.
""",
r"""`embedded URI with too much whitespace \< http://example.com/
long/path /and  /whitespace >`__

`embedded URI with too much whitespace at end \<http://example.com/
long/path /and  /whitespace >`__

`embedded URI with no preceding whitespace\<http://example.com>`__

`escaped URI \<http://example.com>`__

See `HTML Anchors: \<a>`_.
"""],
["""\
Relative URIs' reference text can be omitted:

`<reference>`_

`<anonymous>`__
""",
# A relative anonymous reference aliases with a normal relative reference
"""\
Relative URIs' reference text can be omitted:

`<reference>`_

`<anonymous>`_
"""],
[r"""
Escape trailing low-line char in URIs:

`<reference\_>`_

`<anonymous\_>`__
""",
"""\
Escape trailing low-line char in URIs:

`<reference\_>`_

`<anonymous\_>`_
"""],
["""\
Escape other char in URIs:

`<reference\\:1>`_

`<anonymous\\call>`__
""",
"""\
Escape other char in URIs:

`<reference:1>`_

`<anonymouscall>`_
"""],
["""\
`reference_`_

`reference\\_`_

`<reference\\_>`_

`<reference_>`_

`<reference_name>`_

`<reference\\_name>`_
""",
"""\
`reference\\_`_

`reference\\_`_

`<reference\\_>`_

reference_

`<reference\\_name>`_

`<reference\\_name>`_
"""],
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

totest['inline_targets'] = [
["""\
_`target`

Here is _`another target` in some text. And _`yet
another target`, spanning lines.

_`Here is  a    TaRgeT` with case and spacial difficulties.
""",
"""\
_`target`

Here is _`another target` in some text. And _`yet
another target`, spanning lines.

_`Here is  a    TaRgeT` with case and spacial difficulties.
"""],
[u"""\
l'_`target1` and l\u2019_`target2` with apostrophe
""",
u"""\
l'_`target1` and l\u2019_`target2` with apostrophe
"""],
[u"""\
quoted '_`target1`', quoted "_`target2`",
quoted \u2018_`target3`\u2019, quoted \u201c_`target4`\u201d,
quoted \xab_`target5`\xbb
""",
u"""\
quoted '_`target1`', quoted "_`target2`",
quoted \u2018_`target3`\u2019, quoted \u201c_`target4`\u201d,
quoted \xab_`target5`\xbb
"""],
[u"""\
_`'target1'` with quotes, _`"target2"` with quotes,
_`\u2018target3\u2019` with quotes, _`\u201ctarget4\u201d` with quotes,
_`\xabtarget5\xbb` with quotes
""",
u"""\
_`'target1'` with quotes, _`"target2"` with quotes,
_`\u2018target3\u2019` with quotes, _`\u201ctarget4\u201d` with quotes,
_`\xabtarget5\xbb` with quotes
"""],
["""\
But this isn't a _target; targets require backquotes.

And _`this`_ is just plain confusing.
""",
"""\
But this isn't a _target; targets require backquotes.

And _`this`_ is just plain confusing.
"""],
["""\
_`inline target without closing backquote
""",
"""\
_`inline target without closing backquote
"""],
]

totest['footnote_reference'] = [
["""\
[1]_
""",
"""\
[1]_
"""],
["""\
[#]_
""",
"""\
[#]_
"""],
["""\
[#label]_
""",
"""\
[#label]_
"""],
["""\
[*]_
""",
"""\
[*]_
"""],
["""\
[*label]_
""",
"""\
[*label]_
"""],
["""\
Back to back: [*]_ [#label]_ [#]_ [2]_ [1]_ [*label]_
""",
"""\
Back to back: [*]_ [#label]_ [#]_ [2]_ [1]_ [*label]_
"""],
["""\
Adjacent footnote refs are not possible: [*]_[#label]_ [#]_[2]_ [1]_[*]_
""",
"""\
Adjacent footnote refs are not possible: [*]_[#label]_ [#]_[2]_ [1]_[*]_
"""],
]

#TODO totest['citation_reference'] = [
#TODO ["""\
#TODO [citation]_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <citation_reference ids="id1" refname="citation">
#TODO             citation
#TODO """],
#TODO ["""\
#TODO [citation]_ and [cit-ation]_ and [cit.ation]_ and [CIT1]_ but not [CIT 1]_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         <citation_reference ids="id1" refname="citation">
#TODO             citation
#TODO          and \n\
#TODO         <citation_reference ids="id2" refname="cit-ation">
#TODO             cit-ation
#TODO          and \n\
#TODO         <citation_reference ids="id3" refname="cit.ation">
#TODO             cit.ation
#TODO          and \n\
#TODO         <citation_reference ids="id4" refname="cit1">
#TODO             CIT1
#TODO          but not [CIT 1]_
#TODO """],
#TODO ["""\
#TODO Adjacent citation refs are not possible: [citation]_[CIT1]_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Adjacent citation refs are not possible: [citation]_[CIT1]_
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

totest['standalone_hyperlink'] = [
["""\
http://www.standalone.hyperlink.com

http:/one-slash-only.absolute.path

[http://example.com]

(http://example.com)

<http://example.com>

http://[1080:0:0:0:8:800:200C:417A]/IPv6address.html

http://[3ffe:2a00:100:7031::1] (the final "]" is ambiguous in text)

http://[3ffe:2a00:100:7031::1]/

mailto:someone@somewhere.com

news:comp.lang.python

An email address in a sentence: someone@somewhere.com.

ftp://ends.with.a.period.

(a.question.mark@end?)
""",
"""\
http://www.standalone.hyperlink.com

http:/one-slash-only.absolute.path

[http://example.com]

(http://example.com)

<http://example.com>

http://[1080:0:0:0:8:800:200C:417A]/IPv6address.html

http://[3ffe:2a00:100:7031::1] (the final "]" is ambiguous in text)

http://[3ffe:2a00:100:7031::1]/

mailto:someone@somewhere.com

news:comp.lang.python

An email address in a sentence: someone@somewhere.com.

ftp://ends.with.a.period.

(a.question.mark@end?)
"""],
[r"""
Valid URLs with escaped markup characters:

http://example.com/\*content\*/whatever

http://example.com/\*content*/whatever
""",
"""\
Valid URLs with escaped markup characters:

http://example.com/*content*/whatever

http://example.com/*content*/whatever
"""],
["""\
Valid URLs may end with punctuation inside "<>":

<http://example.org/ends-with-dot.>
""",
"""\
Valid URLs may end with punctuation inside "<>":

<http://example.org/ends-with-dot.>
"""],
["""\
Valid URLs with interesting endings:

http://example.org/ends-with-pluses++
""",
"""\
Valid URLs with interesting endings:

http://example.org/ends-with-pluses++
"""],
["""\
None of these are standalone hyperlinks (their "schemes"
are not recognized): signal:noise, a:b.
""",
"""\
None of these are standalone hyperlinks (their "schemes"
are not recognized): signal:noise, a:b.
"""],
["""\
Escaped email addresses are not recognized: test\\@example.org
""",
"""\
Escaped email addresses are not recognized: test@example.org
"""],
]

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

