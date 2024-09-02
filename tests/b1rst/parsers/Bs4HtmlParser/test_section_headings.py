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

totest['section_headers'] = [
["""\
<h1>Title</h1>

<p>Paragraph.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - section:
      children:
      - title:
          children:
          - Title
      - paragraph:
          children:
          - Paragraph.
"""],
#TODO ["""\
#TODO Title
#TODO =====
#TODO Paragraph (no blank line).
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Paragraph (no blank line).
#TODO """],
#TODO ["""\
#TODO Paragraph.
#TODO 
#TODO Title
#TODO =====
#TODO 
#TODO Paragraph.
#TODO """,
#TODO """\
#TODO Paragraph.
#TODO 
#TODO Title
#TODO =====
#TODO 
#TODO Paragraph.
#TODO """],
#TODO #TODO ["""\
#TODO #TODO Test unexpected section titles.
#TODO #TODO 
#TODO #TODO     Title
#TODO #TODO     =====
#TODO #TODO     Paragraph.
#TODO #TODO 
#TODO #TODO     -----
#TODO #TODO     Title
#TODO #TODO     -----
#TODO #TODO     Paragraph.
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <paragraph>
#TODO #TODO         Test unexpected section titles.
#TODO #TODO     <block_quote>
#TODO #TODO         <system_message level="4" line="4" source="test data" type="SEVERE">
#TODO #TODO             <paragraph>
#TODO #TODO                 Unexpected section title.
#TODO #TODO             <literal_block xml:space="preserve">
#TODO #TODO                 Title
#TODO #TODO                 =====
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph.
#TODO #TODO         <system_message level="4" line="7" source="test data" type="SEVERE">
#TODO #TODO             <paragraph>
#TODO #TODO                 Unexpected section title or transition.
#TODO #TODO             <literal_block xml:space="preserve">
#TODO #TODO                 -----
#TODO #TODO         <system_message level="4" line="9" source="test data" type="SEVERE">
#TODO #TODO             <paragraph>
#TODO #TODO                 Unexpected section title.
#TODO #TODO             <literal_block xml:space="preserve">
#TODO #TODO                 Title
#TODO #TODO                 -----
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph.
#TODO #TODO """],
#TODO ["""\
#TODO Title
#TODO ====
#TODO 
#TODO Test short underline.
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Test short underline.
#TODO """],
#TODO [u"""\
#TODO à with combining varia
#TODO ======================
#TODO 
#TODO Do not count combining chars in title column width.
#TODO """,
#TODO u"""\
#TODO à with combining varia
#TODO =======================
#TODO 
#TODO Do not count combining chars in title column width.
#TODO """],
#TODO ["""\
#TODO =====
#TODO Title
#TODO =====
#TODO 
#TODO Test overline title.
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Test overline title.
#TODO """],
#TODO ["""\
#TODO =======
#TODO  Title
#TODO =======
#TODO 
#TODO Test overline title with inset.
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Test overline title with inset.
#TODO """],
#TODO #TODO ["""\
#TODO #TODO ========================
#TODO #TODO  Test Missing Underline
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO #TODO         <paragraph>
#TODO #TODO             Incomplete section title.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             ========================
#TODO #TODO              Test Missing Underline
#TODO #TODO """],
#TODO #TODO ["""\
#TODO #TODO ========================
#TODO #TODO  Test Missing Underline
#TODO #TODO 
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO #TODO         <paragraph>
#TODO #TODO             Missing matching underline for section title overline.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             ========================
#TODO #TODO              Test Missing Underline
#TODO #TODO """],
#TODO #TODO ["""\
#TODO #TODO =======
#TODO #TODO  Title
#TODO #TODO 
#TODO #TODO Test missing underline, with paragraph.
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO #TODO         <paragraph>
#TODO #TODO             Missing matching underline for section title overline.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             =======
#TODO #TODO              Title
#TODO #TODO     <paragraph>
#TODO #TODO         Test missing underline, with paragraph.
#TODO #TODO """],
#TODO ["""\
#TODO =======
#TODO  Long    Title
#TODO =======
#TODO 
#TODO Test long title and space normalization.
#TODO """,
#TODO """\
#TODO Long    Title
#TODO =============
#TODO 
#TODO Test long title and space normalization.
#TODO """],
#TODO #TODO ["""\
#TODO #TODO =======
#TODO #TODO  Title
#TODO #TODO -------
#TODO #TODO 
#TODO #TODO Paragraph.
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <system_message level="4" line="1" source="test data" type="SEVERE">
#TODO #TODO         <paragraph>
#TODO #TODO             Title overline & underline mismatch.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             =======
#TODO #TODO              Title
#TODO #TODO             -------
#TODO #TODO     <paragraph>
#TODO #TODO         Paragraph.
#TODO #TODO """],
#TODO #TODO ["""\
#TODO #TODO ========================
#TODO #TODO 
#TODO #TODO ========================
#TODO #TODO 
#TODO #TODO Test missing titles; blank line in-between.
#TODO #TODO 
#TODO #TODO ========================
#TODO #TODO 
#TODO #TODO ========================
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <transition>
#TODO #TODO     <transition>
#TODO #TODO     <paragraph>
#TODO #TODO         Test missing titles; blank line in-between.
#TODO #TODO     <transition>
#TODO #TODO     <transition>
#TODO #TODO """],
#TODO #TODO ["""\
#TODO #TODO ========================
#TODO #TODO ========================
#TODO #TODO 
#TODO #TODO Test missing titles; nothing in-between.
#TODO #TODO 
#TODO #TODO ========================
#TODO #TODO ========================
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO #TODO         <paragraph>
#TODO #TODO             Invalid section title or transition marker.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             ========================
#TODO #TODO             ========================
#TODO #TODO     <paragraph>
#TODO #TODO         Test missing titles; nothing in-between.
#TODO #TODO     <system_message level="3" line="6" source="test data" type="ERROR">
#TODO #TODO         <paragraph>
#TODO #TODO             Invalid section title or transition marker.
#TODO #TODO         <literal_block xml:space="preserve">
#TODO #TODO             ========================
#TODO #TODO             ========================
#TODO #TODO """],
#TODO ["""\
#TODO .. Test return to existing, highest-level section (Title 3).
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
#TODO -------
#TODO Paragraph 4.
#TODO """,
#TODO """\
#TODO .. Test return to existing, highest-level section (Title 3).
#TODO 
#TODO Title 1
#TODO =======
#TODO 
#TODO Paragraph 1.
#TODO 
#TODO Title 2
#TODO -------
#TODO 
#TODO Paragraph 2.
#TODO 
#TODO Title 3
#TODO =======
#TODO 
#TODO Paragraph 3.
#TODO 
#TODO Title 4
#TODO -------
#TODO 
#TODO Paragraph 4.
#TODO """],
#TODO ["""\
#TODO Test return to existing, highest-level section (Title 3, with overlines).
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
#TODO -------
#TODO Title 4
#TODO -------
#TODO Paragraph 4.
#TODO """,
#TODO """\
#TODO Test return to existing, highest-level section (Title 3, with overlines).
#TODO 
#TODO Title 1
#TODO =======
#TODO 
#TODO Paragraph 1.
#TODO 
#TODO Title 2
#TODO -------
#TODO 
#TODO Paragraph 2.
#TODO 
#TODO Title 3
#TODO =======
#TODO 
#TODO Paragraph 3.
#TODO 
#TODO Title 4
#TODO -------
#TODO 
#TODO Paragraph 4.
#TODO """],
#TODO ["""\
#TODO Test return to existing, higher-level section (Title 4).
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
#TODO ```````
#TODO Paragraph 3.
#TODO 
#TODO Title 4
#TODO -------
#TODO Paragraph 4.
#TODO """,
#TODO """\
#TODO Test return to existing, higher-level section (Title 4).
#TODO 
#TODO Title 1
#TODO =======
#TODO 
#TODO Paragraph 1.
#TODO 
#TODO Title 2
#TODO -------
#TODO 
#TODO Paragraph 2.
#TODO 
#TODO Title 3
#TODO .......
#TODO 
#TODO Paragraph 3.
#TODO 
#TODO Title 4
#TODO -------
#TODO 
#TODO Paragraph 4.
#TODO """],
#TODO #TODO ["""\
#TODO #TODO Test bad subsection order (Title 4).
#TODO #TODO 
#TODO #TODO Title 1
#TODO #TODO =======
#TODO #TODO Paragraph 1.
#TODO #TODO 
#TODO #TODO Title 2
#TODO #TODO -------
#TODO #TODO Paragraph 2.
#TODO #TODO 
#TODO #TODO Title 3
#TODO #TODO =======
#TODO #TODO Paragraph 3.
#TODO #TODO 
#TODO #TODO Title 4
#TODO #TODO ```````
#TODO #TODO Paragraph 4.
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <paragraph>
#TODO #TODO         Test bad subsection order (Title 4).
#TODO #TODO     <section ids="title-1" names="title\\ 1">
#TODO #TODO         <title>
#TODO #TODO             Title 1
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 1.
#TODO #TODO         <section ids="title-2" names="title\\ 2">
#TODO #TODO             <title>
#TODO #TODO                 Title 2
#TODO #TODO             <paragraph>
#TODO #TODO                 Paragraph 2.
#TODO #TODO     <section ids="title-3" names="title\\ 3">
#TODO #TODO         <title>
#TODO #TODO             Title 3
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 3.
#TODO #TODO         <system_message level="4" line="15" source="test data" type="SEVERE">
#TODO #TODO             <paragraph>
#TODO #TODO                 Title level inconsistent:
#TODO #TODO             <literal_block xml:space="preserve">
#TODO #TODO                 Title 4
#TODO #TODO                 ```````
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 4.
#TODO #TODO """],
#TODO #TODO ["""\
#TODO #TODO Test bad subsection order (Title 4, with overlines).
#TODO #TODO 
#TODO #TODO =======
#TODO #TODO Title 1
#TODO #TODO =======
#TODO #TODO Paragraph 1.
#TODO #TODO 
#TODO #TODO -------
#TODO #TODO Title 2
#TODO #TODO -------
#TODO #TODO Paragraph 2.
#TODO #TODO 
#TODO #TODO =======
#TODO #TODO Title 3
#TODO #TODO =======
#TODO #TODO Paragraph 3.
#TODO #TODO 
#TODO #TODO ```````
#TODO #TODO Title 4
#TODO #TODO ```````
#TODO #TODO Paragraph 4.
#TODO #TODO """,
#TODO #TODO """\
#TODO #TODO <document source="test data">
#TODO #TODO     <paragraph>
#TODO #TODO         Test bad subsection order (Title 4, with overlines).
#TODO #TODO     <section ids="title-1" names="title\\ 1">
#TODO #TODO         <title>
#TODO #TODO             Title 1
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 1.
#TODO #TODO         <section ids="title-2" names="title\\ 2">
#TODO #TODO             <title>
#TODO #TODO                 Title 2
#TODO #TODO             <paragraph>
#TODO #TODO                 Paragraph 2.
#TODO #TODO     <section ids="title-3" names="title\\ 3">
#TODO #TODO         <title>
#TODO #TODO             Title 3
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 3.
#TODO #TODO         <system_message level="4" line="19" source="test data" type="SEVERE">
#TODO #TODO             <paragraph>
#TODO #TODO                 Title level inconsistent:
#TODO #TODO             <literal_block xml:space="preserve">
#TODO #TODO                 ```````
#TODO #TODO                 Title 4
#TODO #TODO                 ```````
#TODO #TODO         <paragraph>
#TODO #TODO             Paragraph 4.
#TODO #TODO """],
#TODO ["""\
#TODO Title containing *inline* ``markup``
#TODO ====================================
#TODO 
#TODO Paragraph.
#TODO """,
#TODO """\
#TODO Title containing *inline* ``markup``
#TODO ====================================
#TODO 
#TODO Paragraph.
#TODO """],
#TODO ["""\
#TODO 1. Numbered Title
#TODO =================
#TODO 
#TODO Paragraph.
#TODO """,
#TODO """\
#TODO 1. Numbered Title
#TODO =================
#TODO 
#TODO Paragraph.
#TODO """],
#TODO ["""\
#TODO 1. Item 1.
#TODO 2. Item 2.
#TODO 3. Numbered Title
#TODO =================
#TODO 
#TODO Paragraph.
#TODO """,
#TODO """\
#TODO 1. Item 1.
#TODO 2. Item 2.
#TODO 
#TODO 3. Numbered Title
#TODO =================
#TODO 
#TODO Paragraph.
#TODO """],
#TODO ["""\
#TODO ABC
#TODO ===
#TODO 
#TODO Short title.
#TODO """,
#TODO """\
#TODO ABC
#TODO ===
#TODO 
#TODO Short title.
#TODO """],
#TODO ["""\
#TODO ABC
#TODO ==
#TODO 
#TODO Underline too short.
#TODO """,
#TODO """\
#TODO ABC
#TODO ==
#TODO 
#TODO Underline too short.
#TODO """],
#TODO ["""\
#TODO ==
#TODO ABC
#TODO ==
#TODO 
#TODO Over & underline too short.
#TODO """,
#TODO """\
#TODO ==
#TODO ABC
#TODO ==
#TODO 
#TODO Over & underline too short.
#TODO """],
#TODO ["""\
#TODO ==
#TODO ABC
#TODO 
#TODO Overline too short, no underline.
#TODO """,
#TODO """\
#TODO ==
#TODO ABC
#TODO 
#TODO Overline too short, no underline.
#TODO """],
#TODO ["""\
#TODO ==
#TODO ABC
#TODO """,
#TODO """\
#TODO ==
#TODO ABC
#TODO """],
#TODO ["""\
#TODO ==
#TODO   Not a title: a definition list item.
#TODO """,
#TODO """\
#TODO ==
#TODO   Not a title: a definition list item.
#TODO """],
#TODO ["""\
#TODO ==
#TODO   Not a title: a definition list item.
#TODO --
#TODO   Another definition list item.  It's in a different list,
#TODO   but that's an acceptable limitation given that this will
#TODO   probably never happen in real life.
#TODO 
#TODO   The next line will trigger a warning:
#TODO ==
#TODO """,
#TODO """\
#TODO ==
#TODO   Not a title: a definition list item.
#TODO 
#TODO --
#TODO   Another definition list item.  It's in a different list,
#TODO   but that's an acceptable limitation given that this will
#TODO   probably never happen in real life.
#TODO 
#TODO   The next line will trigger a warning:
#TODO 
#TODO ==
#TODO """],
#TODO ["""\
#TODO Paragraph
#TODO 
#TODO     ==
#TODO     ABC
#TODO     ==
#TODO 
#TODO     Over & underline too short.
#TODO """,
#TODO """\
#TODO Paragraph
#TODO 
#TODO   ==
#TODO   ABC
#TODO   ==
#TODO 
#TODO   Over & underline too short.
#TODO """],
#TODO ["""\
#TODO Paragraph
#TODO 
#TODO     ABC
#TODO     ==
#TODO 
#TODO     Underline too short.
#TODO """,
#TODO """\
#TODO Paragraph
#TODO 
#TODO   ABC
#TODO   ==
#TODO 
#TODO   Underline too short.
#TODO """],
#TODO ["""\
#TODO ...
#TODO ...
#TODO 
#TODO ...
#TODO ---
#TODO 
#TODO ...
#TODO ...
#TODO ...
#TODO """,
#TODO """\
#TODO ...
#TODO ===
#TODO 
#TODO ...
#TODO ---
#TODO 
#TODO ...
#TODO ===
#TODO 
#TODO ...
#TODO """],
#TODO ["""\
#TODO ..
#TODO Hi
#TODO ..
#TODO 
#TODO ...
#TODO Yo
#TODO ...
#TODO 
#TODO Ho
#TODO """,
#TODO # Two notes about the reference output:
#TODO # # The first `..` in the `Ho` heading gets interpretted as a comment. Because of (default)
#TODO #   document transforms, this comment record gets pushed down under the `Yo` heading.
#TODO # # Also, because of document transforms, the `Yo` heading gets transformed into a sub-title
#TODO #   node with an empty `rawsource` attribute. Hence the underline of the `Yo` heading becomes
#TODO #   twice the length of the simple text representation of that heading.
#TODO """\
#TODO Hi
#TODO ==
#TODO 
#TODO Yo
#TODO ----
#TODO 
#TODO .. 
#TODO 
#TODO Ho
#TODO """],
#TODO ["""\
#TODO Empty Section
#TODO =============
#TODO """,
#TODO """\
#TODO Empty Section
#TODO =============
#TODO """],
#TODO ["""\
#TODO ===
#TODO One
#TODO ===
#TODO 
#TODO The bubble-up parser strategy conflicts with short titles
#TODO (<= 3 char-long over- & underlines).
#TODO 
#TODO ===
#TODO Two
#TODO ===
#TODO 
#TODO The parser currently contains a work-around kludge.
#TODO Without it, the parser ends up in an infinite loop.
#TODO """,
#TODO """\
#TODO One
#TODO ===
#TODO 
#TODO The bubble-up parser strategy conflicts with short titles
#TODO (<= 3 char-long over- & underlines).
#TODO 
#TODO Two
#TODO ===
#TODO 
#TODO The parser currently contains a work-around kludge.
#TODO Without it, the parser ends up in an infinite loop.
#TODO """],
#TODO ["""\
#TODO """,
#TODO """\
#TODO """],
]


#TODO totest['section_headers_extra'] = [
#TODO ["""\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle
#TODO --------
#TODO 
#TODO Subtitle underline will be twice that long due to its missing 'node.rawsource'.
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle
#TODO ----------------
#TODO 
#TODO Subtitle underline will be twice that long due to its missing 'node.rawsource'.
#TODO """],
#TODO ["""\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle 1
#TODO ----------
#TODO 
#TODO Subtitle 2
#TODO ----------
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle 1
#TODO ----------
#TODO 
#TODO Subtitle 2
#TODO ----------
#TODO """],
#TODO ["""\
#TODO Title 1
#TODO =======
#TODO 
#TODO Subtitle
#TODO --------
#TODO 
#TODO Title 2
#TODO =======
#TODO """,
#TODO """\
#TODO Title 1
#TODO =======
#TODO 
#TODO Subtitle
#TODO --------
#TODO 
#TODO Title 2
#TODO =======
#TODO """],
#TODO ["""\
#TODO Title
#TODO =====
#TODO 
#TODO ----------
#TODO Subtitle 1
#TODO ----------
#TODO 
#TODO While the two subtitles are equal, the 1st will
#TODO get promoted to '<subtitle>'.
#TODO 
#TODO Subtitle 2
#TODO ----------
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle 1
#TODO --------------------
#TODO 
#TODO While the two subtitles are equal, the 1st will
#TODO get promoted to '<subtitle>'.
#TODO 
#TODO Subtitle 2
#TODO ----------
#TODO """],
#TODO ["""\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle 1
#TODO ----------
#TODO 
#TODO While the two subtitles are equal, the 1st will
#TODO get promoted to '<subtitle>'.
#TODO 
#TODO ----------
#TODO Subtitle 2
#TODO ----------
#TODO """,
#TODO """\
#TODO Title
#TODO =====
#TODO 
#TODO Subtitle 1
#TODO --------------------
#TODO 
#TODO While the two subtitles are equal, the 1st will
#TODO get promoted to '<subtitle>'.
#TODO 
#TODO Subtitle 2
#TODO ----------
#TODO """],
#TODO ]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
