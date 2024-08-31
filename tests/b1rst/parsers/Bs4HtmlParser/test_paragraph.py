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

totest['paragraphs'] = [
["""\
<p>A paragraph.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - A paragraph.
"""],
["""\
<p>Paragraph 1.</p>
<p>Paragraph 2.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - Paragraph 1.
  - paragraph:
      children:
      - Paragraph 2.
"""],
["""\
<p>Line 1.
Line 2.
Line 3.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - 'Line 1.

        Line 2.

        Line 3.'
"""],
["""\
<p>Paragraph 1, Line 1.
Line 2.
Line 3.</p>

<p>Paragraph 2, Line 1.
Line 2.
Line 3.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - 'Paragraph 1, Line 1.

        Line 2.

        Line 3.'
  - paragraph:
      children:
      - 'Paragraph 2, Line 1.

        Line 2.

        Line 3.'
"""],
# Without the 2nd line, the 'A. ...' would have turned into
# an enumerated item.
["""\
<p>A. Einstein was a really
smart dude.</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - 'A. Einstein was a really

        smart dude.'
"""],
]


## totest['paragraphs_odd_starts'] = [
## # Aliasing with a line block
## ["""\
## \\| This is not a line block.
## | The vertical bar is simply part of a paragraph.
## """,
## """\
## document:
##   attrs:
##     source: <string>
##   children:
##   - paragraph:
##       children:
##       - '| This is not a line block.
## 
##         | The vertical bar is simply part of a paragraph.'
## """],
## # Aliasing with a block quote
## [r"""\ This is not a block quote
## \ with multiple lines.
## 
## \  This is not a block quote
## \  with multiple lines.
## 
## \   This is not a block quote
## \   with multiple lines.
## """,
## r"""document:
##   attrs:
##     source: <string>
##   children:
##   - paragraph:
##       children:
##       - 'This is not a block quote
## 
##         with multiple lines.'
##   - paragraph:
##       children:
##       - " This is not a block quote\n with multiple lines."
##   - paragraph:
##       children:
##       - "  This is not a block quote\n  with multiple lines."
## """],
## # Aliasing with a bullet list item
## ["""\
## \\- This is not a bullet list.
## 
## \\* This is not a bullet list.
## """,
## """\
## document:
##   attrs:
##     source: <string>
##   children:
##   - paragraph:
##       children:
##       - '- This is not a bullet list.'
##   - paragraph:
##       children:
##       - '* This is not a bullet list.'
## """],
## ]


totest['odd_paragraphs'] = [
# Double colon may alias with literal block start.
["""\
<p>A paragraph :: some text</p>

<p>A paragraph::
some text</p>

<p>A paragraph\\::</p>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - paragraph:
      children:
      - 'A paragraph :: some text'
  - paragraph:
      children:
      - 'A paragraph::

        some text'
  - paragraph:
      children:
      - 'A paragraph::'
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

