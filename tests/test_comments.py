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

totest['comments'] = [
["""\
.. A comment

Paragraph.
""",
"""\
.. A comment

Paragraph.
"""],
["""\
.. A comment
   block.

Paragraph.
""",
"""\
.. A comment
   block.

Paragraph.
"""],
["""\
..
   A comment consisting of multiple lines
   starting on the line after the
   explicit markup start.
""",
"""\
.. A comment consisting of multiple lines
   starting on the line after the
   explicit markup start.
"""],
["""\
.. A comment.
.. Another.

Paragraph.
""",
"""\
.. A comment.
.. Another.

Paragraph.
"""],
["""\
.. A comment.

.. Another.
""",
"""\
.. A comment.
.. Another.
"""],
["""\
.. A comment
no blank line

Paragraph.
""",
"""\
.. A comment

no blank line

Paragraph.
"""],
["""\
Paragraph.
.. Not a comment
""",
"""\
Paragraph.
.. Not a comment
"""],
["""\
.. A comment
Paragraph.
.. Not a comment
""",
"""\
.. A comment

Paragraph.
.. Not a comment
"""],
["""\
.. A comment.
.. Another.
no blank line

Paragraph.
""",
"""\
.. A comment.
.. Another.

no blank line

Paragraph.
"""],
["""\
.. A comment::

Paragraph.
""",
"""\
.. A comment::

Paragraph.
"""],
["""\
..
   comment::

The extra newline before the comment text prevents
the parser from recognizing a directive.
""",
"""\
.. comment::

The extra newline before the comment text prevents
the parser from recognizing a directive.
"""],
["""\
..
   _comment: http://example.org

The extra newline before the comment text prevents
the parser from recognizing a hyperlink target.
""",
"""\
.. _comment: http://example.org

The extra newline before the comment text prevents
the parser from recognizing a hyperlink target.
"""],
["""\
..
   [comment] Not a citation.

The extra newline before the comment text prevents
the parser from recognizing a citation.
""",
"""\
.. [comment] Not a citation.

The extra newline before the comment text prevents
the parser from recognizing a citation.
"""],
["""\
..
   |comment| image:: bogus.png

The extra newline before the comment text prevents
the parser from recognizing a substitution definition.
""",
"""\
.. |comment| image:: bogus.png

The extra newline before the comment text prevents
the parser from recognizing a substitution definition.
"""],
["""\
.. Next is an empty comment, which serves to end this comment and
   prevents the following block quote being swallowed up.

..

    A block quote.
""",
"""\
.. Next is an empty comment, which serves to end this comment and
   prevents the following block quote being swallowed up.
.. 

  A block quote.
"""],
["""\
term 1
  definition 1

  .. a comment

term 2
  definition 2
""",
"""\
term 1
  definition 1

  .. a comment
term 2
  definition 2
"""],
["""\
term 1
  definition 1

  .. a comment

  still definition 1

term 2
  definition 2
""",
"""\
term 1
  definition 1

  .. a comment

  still definition 1
term 2
  definition 2
"""],
["""\
term 1
  definition 1

.. a comment

term 2
  definition 2
""",
"""\
term 1
  definition 1

.. a comment

term 2
  definition 2
"""],
["""\
+ bullet paragraph 1

  bullet paragraph 2

  .. comment between bullet paragraphs 2 and 3

  bullet paragraph 3
""",
"""\
+ bullet paragraph 1

  bullet paragraph 2

  .. comment between bullet paragraphs 2 and 3

  bullet paragraph 3
"""],
["""\
+ bullet paragraph 1

  .. comment between bullet paragraphs 1 (leader) and 2

  bullet paragraph 2
""",
"""\
+ bullet paragraph 1

  .. comment between bullet paragraphs 1 (leader) and 2

  bullet paragraph 2
"""],
["""\
+ bullet

  .. trailing comment
""",
"""\
+ bullet

  .. trailing comment
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
