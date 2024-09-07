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
# simple table structures to test columns and rows
#
totest['tables_simple'] = [
# 1x1 table
["""\
<table><tbody><tr><td>Cell.</td></tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - Cell.
"""],
# 1x2 table
["""\
<table>
<tbody>
<tr><td>r1c1</td><td>r1c2</td></tr>
</tbody>
</table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '2'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r1c1
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r1c2
"""],
# 1x1 table
["""\
<table><tbody>
<tr><td>r1c1</td></tr>
<tr><td>r2c1</td></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r1c1
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r2c1
"""],
# 2x2 table
["""\
<table>
<tbody>
<tr><td>r1c1</td><td>r1c2</td></tr>
<tr>
  <td>r2c1</td>
  <td>r2c2</td>
</tr>
</tbody>
</table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '2'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r1c1
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r1c2
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r2c1
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - r2c2
"""],
]


#
# simple table structures with column and/or row spans
#
totest['tables_spans'] = [
# colspan in 1st row and 2nd column
["""\
<table><tbody>
<tr><td/><td colspan="3"/><td/></tr>
<tr><td/><td/><td/><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '5'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      attrs:
                        morecols: '2'
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
# colspan in 2nd row and 1st column
["""\
<table><tbody>
<tr><td/><td/><td/><td/><td/></tr>
<tr><td colspan="3"/><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '5'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      attrs:
                        morecols: '2'
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
# colspan in 1st header/row and last column
["""\
<table><tbody>
<tr><th/><th/><th colspan="3"/></tr>
<tr><td/><td/><td/><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '5'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      attrs:
                        morecols: '2'
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
# rowspan in 1st row and 2nd column
["""\
<table><tbody>
<tr><td/><td rowspan="2"/><td/></tr>
<tr><td/><td/></tr>
<tr><td/><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '3'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      attrs:
                        morerows: '1'
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
# rowspan in 2nd row and 1st column
["""\
<table><tbody>
<tr><td/><td/><td/></tr>
<tr><td rowspan="2"/><td/><td/></tr>
<tr><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '3'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      attrs:
                        morerows: '1'
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
# rowspan and colspan in last row and last column
["""\
<table><tbody>
<tr><td/><td/><td/><td/><td/></tr>
<tr><td/><td/><td rowspan="2" colspan="3"/></tr>
<tr><td/><td/></tr>
</tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '5'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
                  - entry:
                      attrs:
                        morecols: '2'
                        morerows: '1'
                      children: []
              - row:
                  children:
                  - entry:
                      children: []
                  - entry:
                      children: []
"""],
]


#
# Simple tables to test inline markup in cells
#
totest['tables_inline_markup'] = [
# sole paragraph
["""\
<table><tbody><tr>
<td><p>Paragraph.</p></td>
</tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - Paragraph.
"""],
# two paragraphs
["""\
<table><tbody><tr>
<td>
  <p>1st paragraph.</p>

<p>2nd paragraph.</p>
</td>
</tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - 1st paragraph.
                      - paragraph:
                          children:
                          - 2nd paragraph.
"""],
# various text style markups (with explicit paragraph)
["""\
<table><tbody><tr>
<td><p>This is wrapped <b>bold, incl. <i>emphasis</i></b> and <tt>literal</tt>.</p></td>
</tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - 'This is wrapped '
                          - strong:
                              children:
                              - 'bold, incl. '
                              - emphasis:
                                  children:
                                  - emphasis
                          - ' and '
                          - literal:
                              children:
                              - literal
                          - .
"""],
# various text style markups (without explicit paragraph)
["""\
<table><tbody><tr>
<td>This is unwrapped <b>bold, incl. <i>emphasis</i></b> and <tt>literal</tt>.</td>
</tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - 'This is unwrapped '
                          - strong:
                              children:
                              - 'bold, incl. '
                              - emphasis:
                                  children:
                                  - emphasis
                          - ' and '
                          - literal:
                              children:
                              - literal
                          - .
"""],
# combinations of free-text blocks and paragraphed blocks
["""\
<table><tbody><tr>
<td>
Some <b>bold</b> free text.
<p>Followed by <i>paragraphed</i> text.</p>
More <tt>free</tt> text.
<p>And another paragraph.</p>
</td>
</tr></tbody></table>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - table:
      attrs:
        classes:
        - colwidths-auto
      children:
      - tgroup:
          attrs:
            cols: '1'
          children:
          - colspec:
              attrs:
                colwidth: '20'
              children: []
          - tbody:
              children:
              - row:
                  children:
                  - entry:
                      children:
                      - paragraph:
                          children:
                          - '

                            Some '
                          - strong:
                              children:
                              - bold
                          - ' free text.'
                      - paragraph:
                          children:
                          - 'Followed by '
                          - emphasis:
                              children:
                              - paragraphed
                          - ' text.'
                      - paragraph:
                          children:
                          - '

                            More '
                          - literal:
                              children:
                              - free
                          - ' text.'
                      - paragraph:
                          children:
                          - And another paragraph.
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

