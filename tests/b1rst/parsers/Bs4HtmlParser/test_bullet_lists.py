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

totest['bullet_lists'] = [
["""\
<ul><li>item</li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ul>
  <li>item 1</li>
  <li>item 2</li>
</ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
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
<ul><li/></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children: []
"""],
["""\
<ul><li><p>item</p></li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ul>
  <li><p>item 1, para 1</p><p>item 1, para 2</p></li>
  <li>item 2</li>
</ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
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
        <ul style="list-style-type:circle; color: green"><li>item</li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: +
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
"""],
["""\
<ul style="list-style-type:square"><li>item 1</li></ul>
<ul style="list-style-type:djsc"><li>item 2</li></ul>
<ul style="list-style-type:circle"><li>item 3</li></ul>
<ul style="list-style-type:none"><li>item 4</li></ul>
<ul style="list-style-type:unknown"><li>item 5</li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '-'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 2
  - bullet_list:
      attrs:
        bullet: +
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 3
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 4
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 5
"""],
# combinations of free-text blocks and paragraphed blocks
["""\
<ul><li>Some <b>bold</b> free text.
<p>Followed by <i>paragraphed</i> text.</p>
More <tt>free</tt> text.
</li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
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
]


#
# nested lists
#
totest['multilevel_bullet_lists'] = [
["""\
<ul><li>item<ul><li>subitem</li></ul></li></ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
          - bullet_list:
              attrs:
                bullet: '*'
              children:
              - list_item:
                  children:
                  - paragraph:
                      children:
                      - subitem
"""],
["""\
<ul>
  <li>item 1<ul><li>subitem a</li><li>subitem b</li></ul></li>
  <li>item 2<ul><li>subitem c</li><li>subitem d</li></ul></li>
</ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '*'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item 1
          - bullet_list:
              attrs:
                bullet: '*'
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
          - bullet_list:
              attrs:
                bullet: '*'
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
<ul style="list-style-type:square">
  <li><p>item</p>
    <ul style="list-style-type:circle"><li>subitem</li></ul>
  </li>
</ul>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - bullet_list:
      attrs:
        bullet: '-'
      children:
      - list_item:
          children:
          - paragraph:
              children:
              - item
          - bullet_list:
              attrs:
                bullet: +
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

