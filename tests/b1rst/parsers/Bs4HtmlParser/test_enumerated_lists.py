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

totest['enumerated_lists'] = [
["""\
<ol><li>item</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ol>
  <li>item 1</li>
  <li>item 2</li>
</ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
"""],
# empty list item
["""\
<ol><li/></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children: []
"""],
["""\
<ol><li><p>item</p></li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ol>
  <li><p>item 1, para 1</p><p>item 1, para 2</p></li>
  <li>item 2</li>
</ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1, para 1
          - paragraph:
              children:
              - item 1, para 2
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
"""],
["""\
        <ol style="bgcolor: red; list-style-type:lower-roman; color: green"><li>item</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: lowerroman
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ol type="A">
<li>item</li>
</ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: upperalpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ol style="list-style-type:lower-alpha"><li>item 1</li></ol>
<ol style="list-style-type:upper-alpha"><li>item 2</li></ol>
<ol style="list-style-type:decimal"><li>item 3</li></ol>
<ol style="list-style-type:lower-roman"><li>item 4</li></ol>
<ol style="list-style-type:unknown"><li>item 5</li></ol>
<ol style="list-style-type:upper-roman"><li>item 6</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: loweralpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
  - enumerated_list:
      attrs:
        enumtype: upperalpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 3
  - enumerated_list:
      attrs:
        enumtype: lowerroman
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 4
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 5
  - enumerated_list:
      attrs:
        enumtype: upperroman
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 6
"""],
["""\
<ol type="a"><li>item 1</li></ol>
<ol type="A"><li>item 2</li></ol>
<ol type="1"><li>item 3</li></ol>
<ol type="i"><li>item 4</li></ol>
<ol type="X"><li>item 5</li></ol>
<ol type="I"><li>item 6</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: loweralpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
  - enumerated_list:
      attrs:
        enumtype: upperalpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 3
  - enumerated_list:
      attrs:
        enumtype: lowerroman
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 4
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 5
  - enumerated_list:
      attrs:
        enumtype: upperroman
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 6
"""],
# combinations of free-text blocks and paragraphed blocks
["""\
<ol><li>Some <b>bold</b> free text.
<p>Followed by <i>paragraphed</i> text.</p>
More <tt>free</tt> text.
</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - 'Some '
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
"""],
# non-default start number
["""\
<ol start="10"><li>item</li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        start: '10'
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
]


#
# nested lists
#
totest['multilevel_bullet_lists'] = [
["""\
<ol><li>item<ol><li>subitem</li></ol></li></ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
          - enumerated_list:
              attrs:
                enumtype: arabic
                prefix: ''
                suffix: .
              children:
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem
"""],
["""\
<ol>
  <li>item 1<ol><li>subitem a</li><li>subitem b</li></ol></li>
  <li>item 2<ol><li>subitem c</li><li>subitem d</li></ol></li>
</ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: arabic
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
          - enumerated_list:
              attrs:
                enumtype: arabic
                prefix: ''
                suffix: .
              children:
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem a
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem b
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
          - enumerated_list:
              attrs:
                enumtype: arabic
                prefix: ''
                suffix: .
              children:
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem c
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem d
"""],
["""\
<ol style="list-style-type: upper-alpha">
  <li><p>item</p>
    <ol type="i"><li>subitem</li></ol>
  </li>
</ol>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - enumerated_list:
      attrs:
        enumtype: upperalpha
        prefix: ''
        suffix: .
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
          - enumerated_list:
              attrs:
                enumtype: lowerroman
                prefix: ''
                suffix: .
              children:
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

