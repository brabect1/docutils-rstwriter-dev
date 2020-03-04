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

totest['block_quotes'] = [
["""\
Line 1.
Line 2.

   Indented.
""",
"""\
Line 1.
Line 2.

  Indented.
"""],
["""\
Line 1.
Line 2.

   Indented 1.

      Indented 2.
""",
"""\
Line 1.
Line 2.

  Indented 1.

    Indented 2.
"""],
["""\
Line 1.
Line 2.
    Unexpectedly indented.
""",
"""\
Line 1.
Line 2.

  Unexpectedly indented.
"""],
["""\
Line 1.
Line 2.

   Indented.
no blank line
""",
"""\
Line 1.
Line 2.

  Indented.

no blank line
"""],
["""\
Here is a paragraph.

        Indent 8 spaces.

    Indent 4 spaces.

Is this correct? Should it generate a warning?
Yes, it is correct, no warning necessary.
""",
"""\
Here is a paragraph.

    Indent 8 spaces.

  Indent 4 spaces.

Is this correct? Should it generate a warning?
Yes, it is correct, no warning necessary.
"""],
["""\
Paragraph.

   Block quote.

   -- Attribution

Paragraph.

   Block quote.

   --Attribution
""",
"""\
Paragraph.

  Block quote.

  -- Attribution

Paragraph.

  Block quote.

  -- Attribution
"""],
[u"""\
Alternative: true em-dash.

   Block quote.

   \u2014 Attribution

Alternative: three hyphens.

   Block quote.

   --- Attribution
""",
"""\
Alternative: true em-dash.

  Block quote.

  -- Attribution

Alternative: three hyphens.

  Block quote.

  -- Attribution
"""],
["""\
Paragraph.

   Block quote.

   -- Attribution line one
   and line two

Paragraph.

   Block quote.

   -- Attribution line one
      and line two

Paragraph.
""",
"""\
Paragraph.

  Block quote.

  -- Attribution line one
  and line two

Paragraph.

  Block quote.

  -- Attribution line one
  and line two

Paragraph.
"""],
["""\
Paragraph.

   Block quote 1.

   -- Attribution 1

   Block quote 2.

   --Attribution 2
""",
"""\
Paragraph.

  Block quote 1.

  -- Attribution 1

  Block quote 2.

  -- Attribution 2
"""],
["""\
Paragraph.

   Block quote 1.

   -- Attribution 1

   Block quote 2.
""",
"""\
Paragraph.

  Block quote 1.

  -- Attribution 1

  Block quote 2.
"""],
["""\
Unindented paragraph.

    Block quote 1.

    -- Attribution 1

    Block quote 2.

..

    Block quote 3.
""",
"""\
Unindented paragraph.

  Block quote 1.

  -- Attribution 1

  Block quote 2.

.. 

  Block quote 3.
"""],
["""\
Paragraph.

   -- Not an attribution

Paragraph.

   Block quote.

   \\-- Not an attribution

Paragraph.

   Block quote.

   -- Not an attribution line one
      and line two
          and line three
""",
"""\
Paragraph.

  -- Not an attribution

Paragraph.

  Block quote.

  -- Not an attribution

Paragraph.

  Block quote.

  -- Not an attribution line one
    and line two
      and line three
"""],
["""\
Paragraph.

   -- Not a valid attribution

   Block quote 1.

   --Attribution 1

   --Invalid attribution

   Block quote 2.

   --Attribution 2
""",
"""\
Paragraph.

  -- Not a valid attribution

  Block quote 1.

  -- Attribution 1

  --Invalid attribution

  Block quote 2.

  -- Attribution 2
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
