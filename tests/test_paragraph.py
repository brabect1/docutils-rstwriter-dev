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

totest['paragraphs'] = [
["""\
A paragraph.
""",
"""\
A paragraph.
"""],
["""\
Paragraph 1.

Paragraph 2.
""",
"""\
Paragraph 1.

Paragraph 2.
"""],
["""\
Line 1.
Line 2.
Line 3.
""",
"""\
Line 1.
Line 2.
Line 3.
"""],
["""\
Paragraph 1, Line 1.
Line 2.
Line 3.

Paragraph 2, Line 1.
Line 2.
Line 3.
""",
"""\
Paragraph 1, Line 1.
Line 2.
Line 3.

Paragraph 2, Line 1.
Line 2.
Line 3.
"""],
["""\
A. Einstein was a really
smart dude.
""",
"""\
\\A. Einstein was a really
smart dude.
"""],
]

totest['paragraphs_odd_starts'] = [
# Aliasing with a line block
["""\
\\| This is not a line block.
| The vertical bar is simply part of a paragraph.
""",
"""\
\\| This is not a line block.
\\| The vertical bar is simply part of a paragraph.
"""],
# Aliasing with a block quote
["""\
\\ This is not a block quote
\\ with multiple lines.

\\  This is not a block quote
\\  with multiple lines.

\\   This is not a block quote
\\   with multiple lines.
""",
"""\
This is not a block quote
with multiple lines.

\\  This is not a block quote
\\  with multiple lines.

\\   This is not a block quote
\\   with multiple lines.
"""],
# Aliasing with a bullet list item
["""\
\\- This is not a bullet list.

\\* This is not a bullet list.
""",
"""\
\\- This is not a bullet list.

\\* This is not a bullet list.
"""],
]

totest['odd_paragraphs'] = [
# Double colon may alias with literal block start.
["""\
A paragraph :: some text

A paragraph::
some text

A paragraph\\::
""",
"""\
A paragraph :: some text

A paragraph::
some text

A paragraph\\::
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

