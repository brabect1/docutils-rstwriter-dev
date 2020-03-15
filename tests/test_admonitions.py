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
.. note:: some note
""",
"""\
.. note:: some note
"""],
["""\
Some paragraph.

.. note:: some note

Another paragraph.
""",
"""\
Some paragraph.

.. note:: some note

Another paragraph.
"""],
["""\
Some paragraph.
.. note:: Not a note but 2nd line of the paragraph.
""",
"""\
Some paragraph.
.. note:: Not a note but 2nd line of the paragraph.
"""],
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
["""\
.. note::
   :name: some name

   Some text.
""",
"""\
.. note::
   :name: some name

   Some text.
"""],
["""\
.. note::
   :class: some class

   Some text.
""",
"""\
.. note::
   :class: some class

   Some text.
"""],
["""\
.. note::
   :name: some name
   :class: some class

   Some text.
""",
"""\
.. note::
   :name: some name
   :class: some class

   Some text.
"""],
["""\
.. note::
   :class: some class
   :name: some name

   The output will have "name" first, then "class".
""",
"""\
.. note::
   :name: some name
   :class: some class

   The output will have "name" first, then "class".
"""],
["""\
.. note:: This text will be moved after attribute defs.
   :name: some name
   :class: some class
""",
"""\
.. note::
   :name: some name
   :class: some class

   This text will be moved after attribute defs.
"""],
["""\
.. note:: This text will be moved
   after attribute defs.
   :name: some name
   :class: some class
""",
"""\
.. note::
   :name: some name
   :class: some class

   This text will be moved
   after attribute defs.
"""],
["""\
.. Attention:: Directives at large.

.. Note:: :name: mynote
   :class: testnote

   Admonitions support the generic "name" and "class" options.

.. Tip:: 15% if the
   service is good.

.. Hint:: It's bigger than a bread box.

- .. WARNING:: Strong prose may provoke extreme mental exertion.
     Reader discretion is strongly advised.
- .. Error:: Does not compute.

.. Caution::

   Don't take any wooden nickels.

.. DANGER:: Mad scientist at work!

.. Important::
   - Wash behind your ears.
   - Clean up your room.
   - Call your mother.
   - Back up your data.
""",
"""\
.. attention:: Directives at large.

.. note::
   :name: mynote
   :class: testnote

   Admonitions support the generic "name" and "class" options.

.. tip:: 15% if the
   service is good.

.. hint:: It's bigger than a bread box.

- .. warning:: Strong prose may provoke extreme mental exertion.
     Reader discretion is strongly advised.
- .. error:: Does not compute.

.. caution:: Don't take any wooden nickels.

.. danger:: Mad scientist at work!

.. important::
   - Wash behind your ears.
   - Clean up your room.
   - Call your mother.
   - Back up your data.
"""],
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
["""\
Testing admonitions in other environments.

  .. note:: note in a block quote

- .. note:: note in a list item

+------------------------------+
| .. note:: note in a table    |
+------------------------------+
""",
"""\
Testing admonitions in other environments.

  .. note:: note in a block quote

- .. note:: note in a list item

+------------------------------+
| .. note:: note in a table    |
+------------------------------+
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
["""\
.. admonition:: Admonition
   :class: emergency
   :name: reference name

   Test the "class" override.
""",
"""\
.. admonition:: Admonition
   :name: reference name
   :class: emergency

   Test the "class" override.
"""],
["""\
.. admonition::

   Generic admonitions require a title.
""",
"""\
"""],
]



def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
