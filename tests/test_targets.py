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
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter')
    s.generateTests(totest)
    return s

totest = {}

totest['targets'] = [
["""\
.. _target:

(Internal hyperlink target.)
""",
"""\
.. _target:

(Internal hyperlink target.)
"""],
["""\
.. _optional space before colon :
""",
"""\
.. _optional space before colon:
"""],
[r"""
External hyperlink targets:

.. _one-liner: http://structuredtext.sourceforge.net

.. _starts-on-this-line: http://
                         structuredtext.
                         sourceforge.net

.. _entirely-below:
   http://structuredtext.
   sourceforge.net

.. _escaped-whitespace: http://example.org/a\ path\ with\
   spaces.html

.. _not-indirect: uri\_
""",
"""\
External hyperlink targets:

.. _one-liner: http://structuredtext.sourceforge.net

.. _starts-on-this-line: http://structuredtext.sourceforge.net

.. _entirely-below: http://structuredtext.sourceforge.net

.. _escaped-whitespace: http://example.org/a path with spaces.html

.. _not-indirect: uri_
"""],
#TODO ["""\
#TODO Indirect hyperlink targets:
#TODO 
#TODO .. _target1: reference_
#TODO 
#TODO .. _target2: `phrase-link reference`_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Indirect hyperlink targets:
#TODO     <target ids="target1" names="target1" refname="reference">
#TODO     <target ids="target2" names="target2" refname="phrase-link reference">
#TODO """],
#TODO ["""\
#TODO .. _a long target name:
#TODO 
#TODO .. _`a target name: including a colon (quoted)`:
#TODO 
#TODO .. _a target name\\: including a colon (escaped):
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <target ids="a-long-target-name" names="a\\ long\\ target\\ name">
#TODO     <target ids="a-target-name-including-a-colon-quoted" names="a\\ target\\ name:\\ including\\ a\\ colon\\ (quoted)">
#TODO     <target ids="a-target-name-including-a-colon-escaped" names="a\\ target\\ name:\\ including\\ a\\ colon\\ (escaped)">
#TODO """],
#TODO ["""\
#TODO .. _`target: No matching backquote.
#TODO .. _`: No matching backquote either.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <comment xml:space="preserve">
#TODO         _`target: No matching backquote.
#TODO     <system_message level="2" line="1" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             malformed hyperlink target.
#TODO     <comment xml:space="preserve">
#TODO         _`: No matching backquote either.
#TODO     <system_message level="2" line="2" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             malformed hyperlink target.
#TODO """],
["""\
.. _a very long target name,
   split across lines:
.. _`and another,
   with backquotes`:
""",
"""\
.. _a very long target name, split across lines:

.. _and another, with backquotes:
"""],
["""\
External hyperlink:

.. _target: http://www.python.org/
""",
"""\
External hyperlink:

.. _target: http://www.python.org/
"""],
["""\
.. _email: jdoe@example.com

.. _multi-line email: jdoe
   @example.com
""",
"""\
.. _email: mailto:jdoe@example.com

.. _multi-line email: mailto:jdoe@example.com
"""],
#TODO ["""\
#TODO Malformed target:
#TODO 
#TODO .. __malformed: no good
#TODO 
#TODO Target beginning with an underscore:
#TODO 
#TODO .. _`_target`: OK
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Malformed target:
#TODO     <comment xml:space="preserve">
#TODO         __malformed: no good
#TODO     <system_message level="2" line="3" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             malformed hyperlink target.
#TODO     <paragraph>
#TODO         Target beginning with an underscore:
#TODO     <target ids="target" names="_target" refuri="OK">
#TODO """],
["""\
Duplicate external targets (different URIs):

.. _target: first

.. _target: second
""",
"""\
Duplicate external targets (different URIs):

.. _target: first

.. _target: second
"""],
["""\
Duplicate external targets (same URIs):

.. _target: first

.. _target: first
""",
"""\
Duplicate external targets (same URIs):

.. _target: first

.. _target: first
"""],
["""\
Duplicate implicit targets.

Title
=====

Paragraph.

Title
=====

Paragraph.
""",
"""\
Duplicate implicit targets.

Title
=====

Paragraph.

Title
=====

Paragraph.
"""],
["""\
Duplicate implicit/explicit targets.

Title
=====

.. _title:

Paragraph.
""",
"""\
Duplicate implicit/explicit targets.

Title
=====

.. _title:

Paragraph.
"""],
#TODO ["""\
#TODO Duplicate implicit/directive targets.
#TODO 
#TODO Title
#TODO =====
#TODO 
#TODO .. target-notes::
#TODO    :name: title
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Duplicate implicit/directive targets.
#TODO     <section dupnames="title" ids="title">
#TODO         <title>
#TODO             Title
#TODO         <pending ids="id1" names="title">
#TODO             <system_message backrefs="id1" level="1" line="4" source="test data" type="INFO">
#TODO                 <paragraph>
#TODO                     Duplicate implicit target name: "title".
#TODO             .. internal attributes:
#TODO                  .transform: docutils.transforms.references.TargetNotes
#TODO                  .details:
#TODO """],
#TODO ["""\
#TODO Duplicate explicit targets.
#TODO 
#TODO .. _title:
#TODO 
#TODO First.
#TODO 
#TODO .. _title:
#TODO 
#TODO Second.
#TODO 
#TODO .. _title:
#TODO 
#TODO Third.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Duplicate explicit targets.
#TODO     <target dupnames="title" ids="title">
#TODO     <paragraph>
#TODO         First.
#TODO     <system_message backrefs="id1" level="2" line="7" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Duplicate explicit target name: "title".
#TODO     <target dupnames="title" ids="id1">
#TODO     <paragraph>
#TODO         Second.
#TODO     <system_message backrefs="id2" level="2" line="11" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Duplicate explicit target name: "title".
#TODO     <target dupnames="title" ids="id2">
#TODO     <paragraph>
#TODO         Third.
#TODO """],
#TODO ["""\
#TODO Duplicate explicit/directive targets.
#TODO 
#TODO .. _title:
#TODO 
#TODO First.
#TODO 
#TODO .. rubric:: this is a title too
#TODO    :name: title
#TODO 
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Duplicate explicit/directive targets.
#TODO     <target dupnames="title" ids="title">
#TODO     <paragraph>
#TODO         First.
#TODO     <rubric dupnames="title" ids="id1">
#TODO         this is a title too
#TODO         <system_message backrefs="id1" level="2" line="9" source="test data" type="WARNING">
#TODO             <paragraph>
#TODO                 Duplicate explicit target name: "title".
#TODO """],
#TODO ["""\
#TODO Duplicate targets:
#TODO 
#TODO Target
#TODO ======
#TODO 
#TODO Implicit section header target.
#TODO 
#TODO .. [TARGET] Citation target.
#TODO 
#TODO .. [#target] Autonumber-labeled footnote target.
#TODO 
#TODO .. _target:
#TODO 
#TODO Explicit internal target.
#TODO 
#TODO .. _target: Explicit_external_target
#TODO 
#TODO .. rubric:: directive with target
#TODO    :name: Target
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Duplicate targets:
#TODO     <section dupnames="target" ids="target">
#TODO         <title>
#TODO             Target
#TODO         <paragraph>
#TODO             Implicit section header target.
#TODO         <citation dupnames="target" ids="id1">
#TODO             <label>
#TODO                 TARGET
#TODO             <system_message backrefs="id1" level="1" line="8" source="test data" type="INFO">
#TODO                 <paragraph>
#TODO                     Duplicate implicit target name: "target".
#TODO             <paragraph>
#TODO                 Citation target.
#TODO         <footnote auto="1" dupnames="target" ids="id2">
#TODO             <system_message backrefs="id2" level="2" line="10" source="test data" type="WARNING">
#TODO                 <paragraph>
#TODO                     Duplicate explicit target name: "target".
#TODO             <paragraph>
#TODO                 Autonumber-labeled footnote target.
#TODO         <system_message backrefs="id3" level="2" line="12" source="test data" type="WARNING">
#TODO             <paragraph>
#TODO                 Duplicate explicit target name: "target".
#TODO         <target dupnames="target" ids="id3">
#TODO         <paragraph>
#TODO             Explicit internal target.
#TODO         <system_message backrefs="id4" level="2" line="16" source="test data" type="WARNING">
#TODO             <paragraph>
#TODO                 Duplicate explicit target name: "target".
#TODO         <target dupnames="target" ids="id4" refuri="Explicit_external_target">
#TODO         <rubric dupnames="target" ids="id5">
#TODO             directive with target
#TODO             <system_message backrefs="id5" level="2" line="4" source="test data" type="WARNING">
#TODO                 <paragraph>
#TODO                     Duplicate explicit target name: "target".
#TODO """],
#TODO ["""\
#TODO .. _unescaped colon at end:: no good
#TODO 
#TODO .. _:: no good either
#TODO 
#TODO .. _escaped colon\\:: OK
#TODO 
#TODO .. _`unescaped colon, quoted:`: OK
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <comment xml:space="preserve">
#TODO         _unescaped colon at end:: no good
#TODO     <system_message level="2" line="1" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             malformed hyperlink target.
#TODO     <comment xml:space="preserve">
#TODO         _:: no good either
#TODO     <system_message level="2" line="3" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             malformed hyperlink target.
#TODO     <target ids="escaped-colon" names="escaped\\ colon:" refuri="OK">
#TODO     <target ids="unescaped-colon-quoted" names="unescaped\\ colon,\\ quoted:" refuri="OK">
#TODO """],
]

totest['anonymous_targets'] = [
#TODO ["""\
#TODO Anonymous external hyperlink target:
#TODO 
#TODO .. __: http://w3c.org/
#TODO """,
#TODO """\
#TODO Anonymous external hyperlink target:
#TODO 
#TODO .. __: http://w3c.org/
#TODO """],
#TODO ["""\
#TODO Anonymous external hyperlink target:
#TODO 
#TODO __ http://w3c.org/
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Anonymous external hyperlink target:
#TODO     <target anonymous="1" ids="id1" refuri="http://w3c.org/">
#TODO """],
#TODO ["""\
#TODO Anonymous indirect hyperlink target:
#TODO 
#TODO .. __: reference_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Anonymous indirect hyperlink target:
#TODO     <target anonymous="1" ids="id1" refname="reference">
#TODO """],
#TODO ["""\
#TODO Anonymous external hyperlink target, not indirect:
#TODO 
#TODO __ uri\\_
#TODO 
#TODO __ this URI ends with an underscore_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Anonymous external hyperlink target, not indirect:
#TODO     <target anonymous="1" ids="id1" refuri="uri_">
#TODO     <target anonymous="1" ids="id2" refuri="thisURIendswithanunderscore_">
#TODO """],
#TODO ["""\
#TODO Anonymous indirect hyperlink targets:
#TODO 
#TODO __ reference_
#TODO __ `a very long
#TODO    reference`_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Anonymous indirect hyperlink targets:
#TODO     <target anonymous="1" ids="id1" refname="reference">
#TODO     <target anonymous="1" ids="id2" refname="a very long reference">
#TODO """],
#TODO ["""\
#TODO Mixed anonymous & named indirect hyperlink targets:
#TODO 
#TODO __ reference_
#TODO .. __: reference_
#TODO __ reference_
#TODO .. _target1: reference_
#TODO no blank line
#TODO 
#TODO .. _target2: reference_
#TODO __ reference_
#TODO .. __: reference_
#TODO __ reference_
#TODO no blank line
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Mixed anonymous & named indirect hyperlink targets:
#TODO     <target anonymous="1" ids="id1" refname="reference">
#TODO     <target anonymous="1" ids="id2" refname="reference">
#TODO     <target anonymous="1" ids="id3" refname="reference">
#TODO     <target ids="target1" names="target1" refname="reference">
#TODO     <system_message level="2" line="7" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Explicit markup ends without a blank line; unexpected unindent.
#TODO     <paragraph>
#TODO         no blank line
#TODO     <target ids="target2" names="target2" refname="reference">
#TODO     <target anonymous="1" ids="id4" refname="reference">
#TODO     <target anonymous="1" ids="id5" refname="reference">
#TODO     <target anonymous="1" ids="id6" refname="reference">
#TODO     <system_message level="2" line="13" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Explicit markup ends without a blank line; unexpected unindent.
#TODO     <paragraph>
#TODO         no blank line
#TODO """],
#TODO ["""\
#TODO .. _
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <comment xml:space="preserve">
#TODO         _
#TODO """],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
