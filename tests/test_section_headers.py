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
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter')
    s.generateTests(totest)
    return s

totest = {}

totest['section_headers'] = [
["""\
Title
=====

Paragraph.
""",
"""\
Title
=====

Paragraph.
"""],
["""\
Title
=====
Paragraph (no blank line).
""",
"""\
Title
=====

Paragraph (no blank line).
"""],
["""\
Paragraph.

Title
=====

Paragraph.
""",
"""\
Paragraph.

Title
=====

Paragraph.
"""],
#TODO ["""\
#TODO Test unexpected section titles.
#TODO 
#TODO     Title
#TODO     =====
#TODO     Paragraph.
#TODO 
#TODO     -----
#TODO     Title
#TODO     -----
#TODO     Paragraph.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Test unexpected section titles.
#TODO     <block_quote>
#TODO         <system_message level="4" line="4" source="test data" type="SEVERE">
#TODO             <paragraph>
#TODO                 Unexpected section title.
#TODO             <literal_block xml:space="preserve">
#TODO                 Title
#TODO                 =====
#TODO         <paragraph>
#TODO             Paragraph.
#TODO         <system_message level="4" line="7" source="test data" type="SEVERE">
#TODO             <paragraph>
#TODO                 Unexpected section title or transition.
#TODO             <literal_block xml:space="preserve">
#TODO                 -----
#TODO         <system_message level="4" line="9" source="test data" type="SEVERE">
#TODO             <paragraph>
#TODO                 Unexpected section title.
#TODO             <literal_block xml:space="preserve">
#TODO                 Title
#TODO                 -----
#TODO         <paragraph>
#TODO             Paragraph.
#TODO """],
["""\
Title
====

Test short underline.
""",
"""\
Title
=====

Test short underline.
"""],
[u"""\
à with combining varia
======================

Do not count combining chars in title column width.
""",
u"""\
à with combining varia
=======================

Do not count combining chars in title column width.
"""],
["""\
=====
Title
=====

Test overline title.
""",
"""\
Title
=====

Test overline title.
"""],
["""\
=======
 Title
=======

Test overline title with inset.
""",
"""\
Title
=====

Test overline title with inset.
"""],
#TODO ["""\
#TODO ========================
#TODO  Test Missing Underline
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO         <paragraph>
#TODO             Incomplete section title.
#TODO         <literal_block xml:space="preserve">
#TODO             ========================
#TODO              Test Missing Underline
#TODO """],
#TODO ["""\
#TODO ========================
#TODO  Test Missing Underline
#TODO 
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO         <paragraph>
#TODO             Missing matching underline for section title overline.
#TODO         <literal_block xml:space="preserve">
#TODO             ========================
#TODO              Test Missing Underline
#TODO """],
#TODO ["""\
#TODO =======
#TODO  Title
#TODO 
#TODO Test missing underline, with paragraph.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO         <paragraph>
#TODO             Missing matching underline for section title overline.
#TODO         <literal_block xml:space="preserve">
#TODO             =======
#TODO              Title
#TODO     <paragraph>
#TODO         Test missing underline, with paragraph.
#TODO """],
["""\
=======
 Long    Title
=======

Test long title and space normalization.
""",
"""\
Long    Title
=============

Test long title and space normalization.
"""],
#TODO ["""\
#TODO =======
#TODO  Title
#TODO -------
#TODO 
#TODO Paragraph.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO         <paragraph>
#TODO             Title overline & underline mismatch.
#TODO         <literal_block xml:space="preserve">
#TODO             =======
#TODO              Title
#TODO             -------
#TODO     <paragraph>
#TODO         Paragraph.
#TODO """],
#TODO ["""\
#TODO ========================
#TODO 
#TODO ========================
#TODO 
#TODO Test missing titles; blank line in-between.
#TODO 
#TODO ========================
#TODO 
#TODO ========================
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <transition>
#TODO     <transition>
#TODO     <paragraph>
#TODO         Test missing titles; blank line in-between.
#TODO     <transition>
#TODO     <transition>
#TODO """],
#TODO ["""\
#TODO ========================
#TODO ========================
#TODO 
#TODO Test missing titles; nothing in-between.
#TODO 
#TODO ========================
#TODO ========================
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Invalid section title or transition marker.
#TODO         <literal_block xml:space="preserve">
#TODO             ========================
#TODO             ========================
#TODO     <paragraph>
#TODO         Test missing titles; nothing in-between.
#TODO     <system_message level="3" line="6" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Invalid section title or transition marker.
#TODO         <literal_block xml:space="preserve">
#TODO             ========================
#TODO             ========================
#TODO """],
["""\
.. Test return to existing, highest-level section (Title 3).

Title 1
=======
Paragraph 1.

Title 2
-------
Paragraph 2.

Title 3
=======
Paragraph 3.

Title 4
-------
Paragraph 4.
""",
"""\
.. Test return to existing, highest-level section (Title 3).

Title 1
=======

Paragraph 1.

Title 2
-------

Paragraph 2.

Title 3
=======

Paragraph 3.

Title 4
-------

Paragraph 4.
"""],
["""\
Test return to existing, highest-level section (Title 3, with overlines).

=======
Title 1
=======
Paragraph 1.

-------
Title 2
-------
Paragraph 2.

=======
Title 3
=======
Paragraph 3.

-------
Title 4
-------
Paragraph 4.
""",
"""\
Test return to existing, highest-level section (Title 3, with overlines).

Title 1
=======

Paragraph 1.

Title 2
-------

Paragraph 2.

Title 3
=======

Paragraph 3.

Title 4
-------

Paragraph 4.
"""],
["""\
Test return to existing, higher-level section (Title 4).

Title 1
=======
Paragraph 1.

Title 2
-------
Paragraph 2.

Title 3
```````
Paragraph 3.

Title 4
-------
Paragraph 4.
""",
"""\
Test return to existing, higher-level section (Title 4).

Title 1
=======

Paragraph 1.

Title 2
-------

Paragraph 2.

Title 3
.......

Paragraph 3.

Title 4
-------

Paragraph 4.
"""],
#TODO ["""\
#TODO Test bad subsection order (Title 4).
#TODO 
#TODO Title 1
#TODO =======
#TODO Paragraph 1.
#TODO 
#TODO Title 2
#TODO -------
#TODO Paragraph 2.
#TODO 
#TODO Title 3
#TODO =======
#TODO Paragraph 3.
#TODO 
#TODO Title 4
#TODO ```````
#TODO Paragraph 4.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Test bad subsection order (Title 4).
#TODO     <section ids="title-1" names="title\\ 1">
#TODO         <title>
#TODO             Title 1
#TODO         <paragraph>
#TODO             Paragraph 1.
#TODO         <section ids="title-2" names="title\\ 2">
#TODO             <title>
#TODO                 Title 2
#TODO             <paragraph>
#TODO                 Paragraph 2.
#TODO     <section ids="title-3" names="title\\ 3">
#TODO         <title>
#TODO             Title 3
#TODO         <paragraph>
#TODO             Paragraph 3.
#TODO         <system_message level="4" line="15" source="test data" type="SEVERE">
#TODO             <paragraph>
#TODO                 Title level inconsistent:
#TODO             <literal_block xml:space="preserve">
#TODO                 Title 4
#TODO                 ```````
#TODO         <paragraph>
#TODO             Paragraph 4.
#TODO """],
#TODO ["""\
#TODO Test bad subsection order (Title 4, with overlines).
#TODO 
#TODO =======
#TODO Title 1
#TODO =======
#TODO Paragraph 1.
#TODO 
#TODO -------
#TODO Title 2
#TODO -------
#TODO Paragraph 2.
#TODO 
#TODO =======
#TODO Title 3
#TODO =======
#TODO Paragraph 3.
#TODO 
#TODO ```````
#TODO Title 4
#TODO ```````
#TODO Paragraph 4.
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Test bad subsection order (Title 4, with overlines).
#TODO     <section ids="title-1" names="title\\ 1">
#TODO         <title>
#TODO             Title 1
#TODO         <paragraph>
#TODO             Paragraph 1.
#TODO         <section ids="title-2" names="title\\ 2">
#TODO             <title>
#TODO                 Title 2
#TODO             <paragraph>
#TODO                 Paragraph 2.
#TODO     <section ids="title-3" names="title\\ 3">
#TODO         <title>
#TODO             Title 3
#TODO         <paragraph>
#TODO             Paragraph 3.
#TODO         <system_message level="4" line="19" source="test data" type="SEVERE">
#TODO             <paragraph>
#TODO                 Title level inconsistent:
#TODO             <literal_block xml:space="preserve">
#TODO                 ```````
#TODO                 Title 4
#TODO                 ```````
#TODO         <paragraph>
#TODO             Paragraph 4.
#TODO """],
["""\
Title containing *inline* ``markup``
====================================

Paragraph.
""",
"""\
Title containing *inline* ``markup``
====================================

Paragraph.
"""],
["""\
1. Numbered Title
=================

Paragraph.
""",
"""\
1. Numbered Title
=================

Paragraph.
"""],
["""\
1. Item 1.
2. Item 2.
3. Numbered Title
=================

Paragraph.
""",
"""\
1. Item 1.
2. Item 2.

3. Numbered Title
=================

Paragraph.
"""],
["""\
ABC
===

Short title.
""",
"""\
ABC
===

Short title.
"""],
["""\
ABC
==

Underline too short.
""",
"""\
ABC
==

Underline too short.
"""],
["""\
==
ABC
==

Over & underline too short.
""",
"""\
==
ABC
==

Over & underline too short.
"""],
["""\
==
ABC

Overline too short, no underline.
""",
"""\
==
ABC

Overline too short, no underline.
"""],
["""\
==
ABC
""",
"""\
==
ABC
"""],
["""\
==
  Not a title: a definition list item.
""",
"""\
==
  Not a title: a definition list item.
"""],
["""\
==
  Not a title: a definition list item.
--
  Another definition list item.  It's in a different list,
  but that's an acceptable limitation given that this will
  probably never happen in real life.

  The next line will trigger a warning:
==
""",
"""\
==
  Not a title: a definition list item.

--
  Another definition list item.  It's in a different list,
  but that's an acceptable limitation given that this will
  probably never happen in real life.

  The next line will trigger a warning:

==
"""],
["""\
Paragraph

    ==
    ABC
    ==

    Over & underline too short.
""",
"""\
Paragraph

  ==
  ABC
  ==

  Over & underline too short.
"""],
["""\
Paragraph

    ABC
    ==

    Underline too short.
""",
"""\
Paragraph

  ABC
  ==

  Underline too short.
"""],
["""\
...
...

...
---

...
...
...
""",
"""\
...
===

...
---

...
===

...
"""],
["""\
..
Hi
..

...
Yo
...

Ho
""",
"""\
Hi
==

Yo
----

Ho
"""],
["""\
Empty Section
=============
""",
"""\
Empty Section
=============
"""],
["""\
===
One
===

The bubble-up parser strategy conflicts with short titles
(<= 3 char-long over- & underlines).

===
Two
===

The parser currently contains a work-around kludge.
Without it, the parser ends up in an infinite loop.
""",
"""\
One
===

The bubble-up parser strategy conflicts with short titles
(<= 3 char-long over- & underlines).

Two
===

The parser currently contains a work-around kludge.
Without it, the parser ends up in an infinite loop.
"""],
["""\
""",
"""\
"""],
]

totest['section_headers_extra'] = [
["""\
Title
=====

Subtitle
--------

Subtitle underline will be twice that long due to its missing 'node.rawsource'.
""",
"""\
Title
=====

Subtitle
----------------

Subtitle underline will be twice that long due to its missing 'node.rawsource'.
"""],
["""\
Title
=====

Subtitle 1
----------

Subtitle 2
----------
""",
"""\
Title
=====

Subtitle 1
----------

Subtitle 2
----------
"""],
["""\
Title 1
=======

Subtitle
--------

Title 2
=======
""",
"""\
Title 1
=======

Subtitle
--------

Title 2
=======
"""],
["""\
Title
=====

----------
Subtitle 1
----------

While the two subtitles are equal, the 1st will
get promoted to '<subtitle>'.

Subtitle 2
----------
""",
"""\
Title
=====

Subtitle 1
--------------------

While the two subtitles are equal, the 1st will
get promoted to '<subtitle>'.

Subtitle 2
----------
"""],
["""\
Title
=====

Subtitle 1
----------

While the two subtitles are equal, the 1st will
get promoted to '<subtitle>'.

----------
Subtitle 2
----------
""",
"""\
Title
=====

Subtitle 1
--------------------

While the two subtitles are equal, the 1st will
get promoted to '<subtitle>'.

Subtitle 2
----------
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
