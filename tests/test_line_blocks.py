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

totest['line_blocks'] = [
["""\
| This is a line block.
| Line breaks are *preserved*.

| This is a second line block.

| This is a third.
""",
"""\
| This is a line block.
| Line breaks are *preserved*.

| This is a second line block.

| This is a third.
"""],
["""\
| In line blocks,
|     Initial indentation is *also* preserved.
""",
"""\
| In line blocks,
|   Initial indentation is *also* preserved.
"""],
["""\
| Individual lines in line blocks
  *may* wrap, as indicated by the lack of a vertical bar prefix.
  There may be more of these.
| These are called "continuation lines".
""",
"""\
| Individual lines in line blocks
  *may* wrap, as indicated by the lack of a vertical bar prefix.
  There may be more of these.
| These are called "continuation lines".
"""],
["""\
| Inline markup in line blocks may also wrap *to
  continuation lines*.
| But not to following lines.
""",
"""\
| Inline markup in line blocks may also wrap *to
  continuation lines*.
| But not to following lines.
"""],
["""\
\\| This is not a line block.
The vertical bar is simply part of a paragraph.
""",
"""\
\\| This is not a line block.
The vertical bar is simply part of a paragraph.
"""],
["""\
| This line block is incomplete.
There should be a blank line before this paragraph.
""",
"""\
| This line block is incomplete.

There should be a blank line before this paragraph.
"""],
["""\
| This line block contains
|
| blank lines.
""",
"""\
| This line block contains
| \n\
| blank lines.
"""],
["""\
| The blank lines in this block
|   \n\
|       \n\
| have bogus spaces.
""",
"""\
| The blank lines in this block
| \n\
| \n\
| have bogus spaces.
"""],
["""\
| Initial indentation is also significant and preserved:
|
|     Indented 4 spaces
| Not indented
|   Indented 2 spaces
|     Indented 4 spaces
|  Only one space
|
|     Continuation lines may be indented less
  than their base lines.
""",
"""\
| Initial indentation is also significant and preserved:
| \n\
|   Indented 4 spaces
| Not indented
|     Indented 2 spaces
|       Indented 4 spaces
|   Only one space
|   \n\
|     Continuation lines may be indented less
      than their base lines.
"""],
["""\
|
| This block begins and ends with blank lines.
|
""",
"""\
| \n\
| This block begins and ends with blank lines.
| \n\
"""],
["""\
This is not
| a line block.
""",
"""\
This is not
\\| a line block.
"""],
["""\
|   The first line is indented.
|     The second line is more indented.
""",
"""\
| The first line is indented.
|   The second line is more indented.
"""],
["""\
|     The first line is indented.
|   The second line is less indented.
""",
"""\
|   The first line is indented.
| The second line is less indented.
"""],
["""\
|This is not
|a line block

| This is an
|incomplete line block.
""",
"""\
|This is not
|a line block

| This is an

|incomplete line block.
"""],
["""\
| Inline markup *may not
| wrap* over several lines.
""",
"""\
| Inline markup *may not
| wrap* over several lines.
"""],
["""\
| * Block level markup
| * is not recognized.
""",
"""\
| * Block level markup
| * is not recognized.
"""],
["""\
System messages can appear in place of lines:

| `uff <test1>`_
| `uff <test2>`_
""",
"""\
System messages can appear in place of lines:

| `uff <test1>`_
| `uff <test2>`_
"""],
]



def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
