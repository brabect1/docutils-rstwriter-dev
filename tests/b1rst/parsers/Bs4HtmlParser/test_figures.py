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

    # reduce details of `system_messge` nodes
    writer_class = b1rst.writers.YamlWriter.YamlWriter
    writer_class.sysmsg_handling = writer_class.SYSMSG_ATTRS

    s = RstWriterTestUtils.PublishTestSuite(
        test_class=RstWriterTestUtils.WriterNoTransformTestCase,
        writer_name='',
        writer_class=writer_class,
        parser_class=b1rst.parsers.html.Bs4HtmlParser.Bs4HtmlParser)
    s.generateTests(totest)
    return s

totest = {}

totest['figures'] = [
["""\
<figure><img src="picture.png"/></figure>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - figure:
      children:
      - image:
          attrs:
            uri: picture.png
          children: []
"""],
["""\
<figure/>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - system_message:
      attrs:
        level: '2'
        line: '1'
        source: <string>
        type: WARNING
      children: []
"""],
["""\
<figure>
<img src="picture.png">
<figcaption>My caption.</figcaption>
</figure>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - figure:
      children:
      - image:
          attrs:
            uri: picture.png
          children: []
      - caption:
          children:
          - My caption.
"""],
["""\
<figure>
  <figcaption>My caption.</figcaption>
  <img src="picture.png">
</figure>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - figure:
      children:
      - caption:
          children:
          - My caption.
      - image:
          attrs:
            uri: picture.png
          children: []
"""],
["""\
<figure><img src="picture.png" height="100" width="200" scale="50"></figure>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - figure:
      children:
      - image:
          attrs:
            height: '100'
            scale: '50'
            uri: picture.png
            width: '200'
          children: []
"""],
#TODO <figure> parsing does not presently constrain number of underneath <img> elements
["""\
<figure>
<img src="picture.png" style="vertical-align:top">
<img src="picture.jpg" style="text-align: left ; ">
</figure>
""",
"""\
document:
  attrs:
    source: <string>
  children:
  - figure:
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
