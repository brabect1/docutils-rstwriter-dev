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

totest['admonitions'] = [
["""\
.. attention:: attention text

.. note:: note text

.. tip:: tip text

.. hint:: hint text

.. warning:: warning text

.. error:: error text

.. caution:: caution text

.. danger:: danger text

.. important:: important text
""",
"""\
.. attention:: attention text

.. note:: note text

.. tip:: tip text

.. hint:: hint text

.. warning:: warning text

.. error:: error text

.. caution:: caution text

.. danger:: danger text

.. important:: important text
"""],
["""\
.. Attention:: attention text

.. nOTE:: note text

.. Tip:: tip text

.. Hint:: hint text

.. WARNING:: warning text

.. ERROR:: error text

.. Caution:: caution text

.. Danger:: danger text

.. IMPORTANT:: important text
""",
"""\
.. attention:: attention text

.. note:: note text

.. tip:: tip text

.. hint:: hint text

.. warning:: warning text

.. error:: error text

.. caution:: caution text

.. danger:: danger text

.. important:: important text
"""],
["""\
.. attention:: 1st line of a multiline admnotion.
   This is 2nd line.

   This is 1st line of a 2nd paragraph.
""",
"""\
.. attention:: 1st line of a multiline admnotion.
   This is 2nd line.

   This is 1st line of a 2nd paragraph.
"""],
["""\
.. note:: 1st note
.. note:: 2nd note
""",
"""\
.. note:: 1st note

.. note:: 2nd note
"""],
["""\
.. Tip::

   If text starts in the 2nd paragraph,
   it'll get promoted to the 1st paragraph.
""",
"""\
.. tip:: If text starts in the 2nd paragraph,
   it'll get promoted to the 1st paragraph.
"""],
["""\
.. tip:: \n
   some text
""",
"""\
.. tip:: some text
"""],
["""\
..  tip::   some text
""",
"""\
.. tip:: some text
"""],
["""\
.. note:: 2nd+ line alignment
     does not matter.
""",
"""\
.. note:: 2nd+ line alignment
   does not matter.
"""],
["""\
.. note:: some text

     Other paragraphs need not
     align too.
""",
"""\
.. note:: some text

   Other paragraphs need not
   align too.
"""],
#TODO ["""\
#TODO .. Attention:: Directives at large.
#TODO 
#TODO .. Note:: :name: mynote
#TODO    :class: testnote
#TODO 
#TODO    Admonitions support the generic "name" and "class" options.
#TODO 
#TODO .. Tip:: 15% if the
#TODO    service is good.
#TODO 
#TODO .. Hint:: It's bigger than a bread box.
#TODO 
#TODO - .. WARNING:: Strong prose may provoke extreme mental exertion.
#TODO      Reader discretion is strongly advised.
#TODO - .. Error:: Does not compute.
#TODO 
#TODO .. Caution::
#TODO 
#TODO    Don't take any wooden nickels.
#TODO 
#TODO .. DANGER:: Mad scientist at work!
#TODO 
#TODO .. Important::
#TODO    - Wash behind your ears.
#TODO    - Clean up your room.
#TODO    - Call your mother.
#TODO    - Back up your data.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <attention>
#TODO         <paragraph>
#TODO             Directives at large.
#TODO     <note classes="testnote" ids="mynote" names="mynote">
#TODO         <paragraph>
#TODO             Admonitions support the generic "name" and "class" options.
#TODO     <tip>
#TODO         <paragraph>
#TODO             15% if the
#TODO             service is good.
#TODO     <hint>
#TODO         <paragraph>
#TODO             It's bigger than a bread box.
#TODO     <bullet_list bullet="-">
#TODO         <list_item>
#TODO             <warning>
#TODO                 <paragraph>
#TODO                     Strong prose may provoke extreme mental exertion.
#TODO                     Reader discretion is strongly advised.
#TODO         <list_item>
#TODO             <error>
#TODO                 <paragraph>
#TODO                     Does not compute.
#TODO     <caution>
#TODO         <paragraph>
#TODO             Don't take any wooden nickels.
#TODO     <danger>
#TODO         <paragraph>
#TODO             Mad scientist at work!
#TODO     <important>
#TODO         <bullet_list bullet="-">
#TODO             <list_item>
#TODO                 <paragraph>
#TODO                     Wash behind your ears.
#TODO             <list_item>
#TODO                 <paragraph>
#TODO                     Clean up your room.
#TODO             <list_item>
#TODO                 <paragraph>
#TODO                     Call your mother.
#TODO             <list_item>
#TODO                 <paragraph>
#TODO                     Back up your data.
#TODO """],
["""\
.. note:: One-line notes.
.. note:: One after the other.
.. note:: No blank lines in-between.
""",
"""\
.. note:: One-line notes.

.. note:: One after the other.

.. note:: No blank lines in-between.
"""],
#TODO ["""\
#TODO .. note:: Content before options
#TODO    is possible too.
#TODO    :class: mynote
#TODO 
#TODO .. note:: :strong:`a role is not an option`.
#TODO    :name: role not option
#TODO 
#TODO .. note:: a role is
#TODO    :strong:`not an option`, even if its starts a line.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <note classes="mynote">
#TODO         <paragraph>
#TODO             Content before options
#TODO             is possible too.
#TODO     <note ids="role-not-option" names="role\\ not\\ option">
#TODO         <paragraph>
#TODO             <strong>
#TODO                 a role is not an option
#TODO             .
#TODO     <note>
#TODO         <paragraph>
#TODO             a role is
#TODO             <strong>
#TODO                 not an option
#TODO             , even if its starts a line.
#TODO """],
["""\
.. note::
""",
"""\
"""],
["""\
.. admonition:: Admonition

   This is a generic admonition.
""",
"""\
.. admonition:: Admonition

   This is a generic admonition.
"""],
["""\
.. admonition:: And, by the way...

   You can make up your own admonition too.
""",
"""\
.. admonition:: And, by the way...

   You can make up your own admonition too.
"""],
["""\
.. admonition:: 1st title line
   2nd title line

   Admonition 1st paragraph.

   Admonition 2nd multi
   line paragraph.
""",
"""\
.. admonition:: 1st title line
   2nd title line

   Admonition 1st paragraph.

   Admonition 2nd multi
   line paragraph.
"""],
#TODO ["""\
#TODO .. admonition:: Admonition
#TODO    :class: emergency
#TODO    :name: reference name
#TODO 
#TODO    Test the "class" override.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <admonition classes="emergency" ids="reference-name" names="reference\\ name">
#TODO         <title>
#TODO             Admonition
#TODO         <paragraph>
#TODO             Test the "class" override.
#TODO """],
#TODO ["""\
#TODO .. admonition::
#TODO 
#TODO    Generic admonitions require a title.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "admonition" directive:
#TODO             1 argument(s) required, 0 supplied.
#TODO         <literal_block xml:space="preserve">
#TODO             .. admonition::
#TODO             
#TODO                Generic admonitions require a title.
#TODO """],
]



def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
