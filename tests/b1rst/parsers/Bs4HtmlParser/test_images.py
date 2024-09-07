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

totest['images'] = [
["""\
<img src="picture.png"/>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        uri: picture.png
      children: []
"""],
["""\
<img/>
""",
"""\
document:
  attrs:
    source: <string>
  children: []
"""],
["""\
<img src="one two three.png"/>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        uri: one two three.png
      children: []
"""],
["""\
<img src="picture.png" height="100" width="200" scale="50"></img>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        height: '100'
        scale: '50'
        uri: picture.png
        width: '200'
      children: []
"""],
["""\
<img src="picture.png" height="100" height="200"></img>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        height: '200'
        uri: picture.png
      children: []
"""],
["""\
<img src="picture.png" alt="My description."></img>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        alt: My description.
        uri: picture.png
      children: []
"""],
["""\
<img src="picture.png" style="vertical-align:top"></img>
<img src="picture.jpg" style="text-align: left ; "/>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - image:
      attrs:
        align: top
        uri: picture.png
      children: []
  - image:
      attrs:
        align: left
        uri: picture.jpg
      children: []
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
