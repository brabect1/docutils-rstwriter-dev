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
#
#
# Some test data inputs were taken from docutils unit test `test_field_lists.py`
# originally by David Goodger <goodger@python.org>.

from __future__ import absolute_import

import RstWriterTestUtils
import docutils
import docutils.core

def suite():
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter',
            test_class=RstWriterTestUtils.WriterNoTransformTestCase)
    s.generateTests(totest)
    return s

totest = {}

totest['field_lists'] = [
["""\
:field name: field body
""",
"""\
:field name: field body
"""],
["""\
:field name:        field body
""",
"""\
:field name: field body
"""],
["""\
:field name:
  field body
""",
"""\
:field name: field body
"""],
["""\
:field name:
    field body
""",
"""\
:field name: field body
"""],
["""\
:field name:

  field body
""",
"""\
:field name: field body
"""],
["""
:field name: field body
    over multiple
    lines
""",
"""\
:field name: field body
  over multiple
  lines
"""],
# empty body
["""\
:field name:
""",
"""\
:field name:
"""],
# empty body
["""\
:field name:

Paragraph.
""",
"""\
:field name:

Paragraph.
"""],
# missing vertical space before paragraph
["""
:field name: field body
Paragraph with missing vertical space
spanning multiple lines.
""",
"""\
:field name: field body

Paragraph with missing vertical space
spanning multiple lines.
"""],
["""\
:field name: field body
    over multiple
    lines

    2nd para also over
    multiple lines
""",
"""\
:field name: field body
  over multiple
  lines

  2nd para also over
  multiple lines
"""],
["""\
:field 1: field 1 body
:field 2: field 2 body
""",
"""\
:field 1: field 1 body
:field 2: field 2 body
"""],
["""\
:field 1:
  field 1 body
:field 2: field 2 body
""",
"""\
:field 1: field 1 body
:field 2: field 2 body
"""],
["""\
:field 1:
  field 1 body
:field 2:
      field 2 body
""",
"""\
:field 1: field 1 body
:field 2: field 2 body
"""],
["""\
:field 1: field 1 body

:field 2: field 2 body
:field 3: field 3 body
""",
"""\
:field 1: field 1 body
:field 2: field 2 body
:field 3: field 3 body
"""],
]

totest['field_lists_sublists'] = [
["""\
:field list: :field sublist: field sublist body
""",
"""\
:field list:
  :field sublist: field sublist body
"""],
["""\
:field list:
  :field sublist: field sublist body
""",
"""\
:field list:
  :field sublist: field sublist body
"""],
["""\
:field list: :field sublist: :field subsublist: field subsublist body
""",
"""\
:field list:
  :field sublist:
    :field subsublist: field subsublist body
"""],
["""\
:field list item 1:
  :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body
""",
"""\
:field list item 1:
  :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body
"""],
["""\
:field list item 1: :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body
""",
"""\
:field list item 1:
  :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body
"""],
["""\
:field list item 1:

  :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body

  :field sublist item 3: field sublist item 3 body
""",
"""\
:field list item 1:
  :field sublist item 1: field sublist item 1 body
  :field sublist item 2: field sublist item 2 body
  :field sublist item 3: field sublist item 3 body
"""],
]

totest['field_lists_by_goodger'] = [
["""\
One-liners:

:Author: Me

:Version: 1

:Date: 2001-08-11

:Parameter i: integer
""",
"""\
One-liners:

:Author: Me
:Version: 1
:Date: 2001-08-11
:Parameter i: integer
"""],
["""\
One-liners, no blank lines:

:Author: Me
:Version: 1
:Date: 2001-08-11
:Parameter i: integer
""",
"""\
One-liners, no blank lines:

:Author: Me
:Version: 1
:Date: 2001-08-11
:Parameter i: integer
"""],
["""\
:field:
empty item above, no blank line
""",
"""\
:field:

empty item above, no blank line
"""],
["""\
Field bodies starting on the next line:

:Author:
  Me
:Version:
  1
:Date:
  2001-08-11
:Parameter i:
  integer
""",
"""\
Field bodies starting on the next line:

:Author: Me
:Version: 1
:Date: 2001-08-11
:Parameter i: integer
"""],
["""\
One-paragraph, multi-liners:

:Authors: Me,
          Myself,
          and I
:Version: 1
          or so
:Date: 2001-08-11
       (Saturday)
:Parameter i: counter
              (integer)
""",
"""\
One-paragraph, multi-liners:

:Authors: Me,
  Myself,
  and I
:Version: 1
  or so
:Date: 2001-08-11
  (Saturday)
:Parameter i: counter
  (integer)
"""],
["""\
One-paragraph, multi-liners, not lined up:

:Authors: Me,
  Myself,
  and I
:Version: 1
  or so
:Date: 2001-08-11
  (Saturday)
:Parameter i: counter
  (integer)
""",
"""\
One-paragraph, multi-liners, not lined up:

:Authors: Me,
  Myself,
  and I
:Version: 1
  or so
:Date: 2001-08-11
  (Saturday)
:Parameter i: counter
  (integer)
"""],
#TODO ["""\
#TODO Multiple body elements:
#TODO 
#TODO :Authors: - Me
#TODO           - Myself
#TODO           - I
#TODO 
#TODO :Abstract:
#TODO     This is a field list item's body,
#TODO     containing multiple elements.
#TODO 
#TODO     Here's a literal block::
#TODO 
#TODO         def f(x):
#TODO             return x**2 + x
#TODO 
#TODO     Even nested field lists are possible:
#TODO 
#TODO     :Date: 2001-08-11
#TODO     :Day: Saturday
#TODO     :Time: 15:07
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Multiple body elements:
#TODO     <field_list>
#TODO         <field>
#TODO             <field_name>
#TODO                 Authors
#TODO             <field_body>
#TODO                 <bullet_list bullet="-">
#TODO                     <list_item>
#TODO                         <paragraph>
#TODO                             Me
#TODO                     <list_item>
#TODO                         <paragraph>
#TODO                             Myself
#TODO                     <list_item>
#TODO                         <paragraph>
#TODO                             I
#TODO         <field>
#TODO             <field_name>
#TODO                 Abstract
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     This is a field list item's body,
#TODO                     containing multiple elements.
#TODO                 <paragraph>
#TODO                     Here's a literal block:
#TODO                 <literal_block xml:space="preserve">
#TODO                     def f(x):
#TODO                         return x**2 + x
#TODO                 <paragraph>
#TODO                     Even nested field lists are possible:
#TODO                 <field_list>
#TODO                     <field>
#TODO                         <field_name>
#TODO                             Date
#TODO                         <field_body>
#TODO                             <paragraph>
#TODO                                 2001-08-11
#TODO                     <field>
#TODO                         <field_name>
#TODO                             Day
#TODO                         <field_body>
#TODO                             <paragraph>
#TODO                                 Saturday
#TODO                     <field>
#TODO                         <field_name>
#TODO                             Time
#TODO                         <field_body>
#TODO                             <paragraph>
#TODO                                 15:07
#TODO """],
["""\
Nested field lists on one line:

:field1: :field2: :field3: body
:field4: :field5: :field6: body
                  :field7: body
         :field8: body
         :field9: body line 1
           body line 2
""",
"""\
Nested field lists on one line:

:field1:
  :field2:
    :field3: body
:field4:
  :field5:
    :field6: body
    :field7: body
  :field8: body
  :field9: body line 1
    body line 2
"""],
["""\
:Parameter i j k: multiple arguments
""",
"""\
:Parameter i j k: multiple arguments
"""],
["""\
:Field *name* `with` **inline** ``markup``: *inline* markup **in**
                                            ``field`` name is *parsed*.
""",
"""\
:Field *name* `with` **inline** ``markup``: *inline* markup **in**
  ``field`` name is *parsed*.
"""],
#TODO ["""\
#TODO :Field name with *bad inline markup: should generate warning.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <field_list>
#TODO         <field>
#TODO             <field_name>
#TODO                 Field name with \n\
#TODO                 <problematic ids="id2" refid="id1">
#TODO                     *
#TODO                 bad inline markup
#TODO             <field_body>
#TODO                 <system_message backrefs="id2" ids="id1" level="2" line="1" source="test data" type="WARNING">
#TODO                     <paragraph>
#TODO                         Inline emphasis start-string without end-string.
#TODO                 <paragraph>
#TODO                     should generate warning.
#TODO """],
#TODO [r"""Some edge cases:
#TODO 
#TODO :Empty:
#TODO :Author: Me
#TODO No blank line before this paragraph.
#TODO 
#TODO : Field: marker must not begin with whitespace.
#TODO 
#TODO :Field : marker must not end with whitespace.
#TODO 
#TODO Field: marker is missing its open-colon.
#TODO 
#TODO :Field marker is missing its close-colon.
#TODO 
#TODO :Field\: names\: with\: colons\:: are possible.
#TODO 
#TODO :\\Field\  names with backslashes\\: are possible, too.
#TODO 
#TODO :\\: A backslash.
#TODO 
#TODO :Not a\\\: field list.
#TODO 
#TODO :Not a \: field list either.
#TODO 
#TODO :\: Not a field list either.
#TODO 
#TODO :\:
#TODO     A definition list, not a field list.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Some edge cases:
#TODO     <field_list>
#TODO         <field>
#TODO             <field_name>
#TODO                 Empty
#TODO             <field_body>
#TODO         <field>
#TODO             <field_name>
#TODO                 Author
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     Me
#TODO     <system_message level="2" line="5" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Field list ends without a blank line; unexpected unindent.
#TODO     <paragraph>
#TODO         No blank line before this paragraph.
#TODO     <paragraph>
#TODO         : Field: marker must not begin with whitespace.
#TODO     <paragraph>
#TODO         :Field : marker must not end with whitespace.
#TODO     <paragraph>
#TODO         Field: marker is missing its open-colon.
#TODO     <paragraph>
#TODO         :Field marker is missing its close-colon.
#TODO     <field_list>
#TODO         <field>
#TODO             <field_name>
#TODO                 Field: names: with: colons:
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     are possible.
#TODO         <field>
#TODO             <field_name>
#TODO                 \\Field names with backslashes\\
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     are possible, too.
#TODO         <field>
#TODO             <field_name>
#TODO                 \\
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     A backslash.
#TODO     <paragraph>
#TODO         :Not a\\: field list.
#TODO     <paragraph>
#TODO         :Not a : field list either.
#TODO     <paragraph>
#TODO         :: Not a field list either.
#TODO     <definition_list>
#TODO         <definition_list_item>
#TODO             <term>
#TODO                 ::
#TODO             <definition>
#TODO                 <paragraph>
#TODO                     A definition list, not a field list.
#TODO """],
[r"""
:first: field
:field:name:with:embedded:colons: unambiguous, no need for escapes

..

:embedded:colons: in first field name
:field:\`:name: not interpreted text
:field:\`name: not interpreted text
""",
r""":first: field
:field:name:with:embedded:colons: unambiguous, no need for escapes

.. 

:embedded:colons: in first field name
:field:\`:name: not interpreted text
:field:\`name: not interpreted text
"""],
#TODO [r"""
#TODO Edge cases involving embedded colons and interpreted text.
#TODO 
#TODO Recognized as field list items:
#TODO 
#TODO :field\:`name`: interpreted text (standard role) requires
#TODO                 escaping a leading colon in a field name
#TODO 
#TODO :field:name: unambiguous, no need for escapes
#TODO 
#TODO :field::name: double colons are OK, too
#TODO 
#TODO :field:\`name`: not interpreted text
#TODO 
#TODO :`field name`:code:: interpreted text with role in the field name
#TODO                      works only when the role follows the text
#TODO 
#TODO :a `complex`:code:\  field name: field body
#TODO 
#TODO Not recognized as field list items:
#TODO 
#TODO ::code:`not a field name`: paragraph with interpreted text
#TODO 
#TODO :code:`not a field name`: paragraph with interpreted text
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Edge cases involving embedded colons and interpreted text.
#TODO     <paragraph>
#TODO         Recognized as field list items:
#TODO     <field_list>
#TODO         <field>
#TODO             <field_name>
#TODO                 field:
#TODO                 <title_reference>
#TODO                     name
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     interpreted text (standard role) requires
#TODO                     escaping a leading colon in a field name
#TODO         <field>
#TODO             <field_name>
#TODO                 field:name
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     unambiguous, no need for escapes
#TODO         <field>
#TODO             <field_name>
#TODO                 field::name
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     double colons are OK, too
#TODO         <field>
#TODO             <field_name>
#TODO                 field:`name`
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     not interpreted text
#TODO         <field>
#TODO             <field_name>
#TODO                 <literal classes="code">
#TODO                     field name
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     interpreted text with role in the field name
#TODO                     works only when the role follows the text
#TODO         <field>
#TODO             <field_name>
#TODO                 a 
#TODO                 <literal classes="code">
#TODO                     complex
#TODO                  field name
#TODO             <field_body>
#TODO                 <paragraph>
#TODO                     field body
#TODO     <paragraph>
#TODO         Not recognized as field list items:
#TODO     <paragraph>
#TODO         :
#TODO         <literal classes="code">
#TODO             not a field name
#TODO         : paragraph with interpreted text
#TODO     <paragraph>
#TODO         <literal classes="code">
#TODO             not a field name
#TODO         : paragraph with interpreted text
#TODO """],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
