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

totest['indented_literal_blocks'] = [
["""\
A paragraph::

    A literal block.
""",
"""\
A paragraph::

    A literal block.
"""],
["""\
::

    A literal block.
""",
"""\
::

    A literal block.
"""],
["""\
A paragraph

::

    A literal block.
""",
"""\
A paragraph

::

    A literal block.
"""],
["""\
A paragraph with a space after the colons:: \n\

    A literal block.
""",
"""\
A paragraph with a space after the colons::

    A literal block.
"""],
["""\
A paragraph ::

    A literal block.
""",
"""\
A paragraph

::

    A literal block.
"""],
["""\
A literal block with spaces (leading and trailing "empty lines" get ignored)::

    \n\
    A literal block.
    \n\
    Another line
    \n\
""",
"""\
A literal block with spaces (leading and trailing "empty lines" get ignored)::

    A literal block.
    \n\
    Another line
"""],
["""\
A paragraph::

    A literal block.

Another paragraph::

    Another literal block.
    With two blank lines following.


A final paragraph.
""",
"""\
A paragraph::

    A literal block.

Another paragraph::

    Another literal block.
    With two blank lines following.

A final paragraph.
"""],
["""\
A paragraph
on more than
one line::

    A literal block.
""",
"""\
A paragraph
on more than
one line::

    A literal block.
"""],
["""\
A paragraph
on more than
one line::
    A literal block
    with no blank line above.
""",
"""\
A paragraph
on more than
one line::

    A literal block
    with no blank line above.
"""],
["""\
A paragraph::

    A literal block.
no blank line
""",
"""\
A paragraph::

    A literal block.

no blank line
"""],
["""\
::

    A literal block.
no blank line
""",
"""\
::

    A literal block.

no blank line
"""],
[r"""
A paragraph\\::

    A literal block.

A paragraph:::

    A literal block.

A paragraph\::

    Not a literal block.
""",
r"""A paragraph\\::

    A literal block.

A paragraph\:::

    A literal block.

A paragraph\::

  Not a literal block.
"""],
[r"""
\\::

    A literal block.

\::

    Not a literal block.
""",
r"""\\::

    A literal block.

\::

  Not a literal block.
"""],
["""\
A paragraph: ::

    A literal block.
""",
"""\
A paragraph::

    A literal block.
"""],
["""\
A paragraph:

::

    A literal block.
""",
"""\
A paragraph::

    A literal block.
"""],
["""\
A paragraph:
::

    A literal block.
""",
"""\
A paragraph::

    A literal block.
"""],
["""\
A paragraph::

Not a literal block.
""",
"""\
A paragraph:

Not a literal block.
"""],
["""\
A paragraph::

    A wonky literal block.
  Literal line 2.

    Literal line 3.
""",
"""\
A paragraph::

      A wonky literal block.
    Literal line 2.
    \n\
      Literal line 3.
"""],
["""\
EOF, even though a literal block is indicated::
""",
"""\
EOF, even though a literal block is indicated:
"""],
]

totest['quoted_literal_blocks'] = [
["""\
A paragraph::

> A literal block.
""",
"""\
A paragraph::

    > A literal block.
"""],
["""\
A paragraph::


> A literal block.
""",
"""\
A paragraph::

    > A literal block.
"""],
["""\
A paragraph::

> A literal block.
> Line 2.
""",
"""\
A paragraph::

    > A literal block.
    > Line 2.
"""],
["""\
A paragraph::

> A literal block.
  Indented line.
""",
"""\
A paragraph::

    > A literal block.

  Indented line.
"""],
["""\
A paragraph::

> A literal block.
Text.
""",
"""\
A paragraph::

    > A literal block.

Text.
"""],
["""\
A paragraph::

> A literal block.
$ Inconsistent line.
""",
"""\
A paragraph::

    > A literal block.

$ Inconsistent line.
"""],
["""\
A paragraph::

  > A literal block.
  $ Inconsistent line.
""",
"""\
A paragraph::

    > A literal block.
    $ Inconsistent line.
"""],
["""\
Para::

# literal ln1
# literal ln2

Para::

$ literal ln1
$ literal ln2
""",
"""\
Para::

    # literal ln1
    # literal ln2

Para::

    $ literal ln1
    $ literal ln2
"""],
]

totest['literal_block_indentation'] = [
["""\
Para 1::

  literal ln1
  literal ln2

Para 2::

      literal ln1
      literal ln2
""",
"""\
Para 1::

    literal ln1
    literal ln2

Para 2::

    literal ln1
    literal ln2
"""],
["""\
::

  literal ln1
  literal ln2

::

      literal ln1
      literal ln2
""",
"""\
::

    literal ln1
    literal ln2

::

    literal ln1
    literal ln2
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
