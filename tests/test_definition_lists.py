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

from __future__ import absolute_import

import RstWriterTestUtils
import docutils
import docutils.core

def suite():
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter')
    s.generateTests(totest)
    return s

totest = {}

totest['definition_lists'] = [
["""\
term
  definition
""",
"""\
term
  definition
"""],
["""\
term
    definition
""",
"""\
term
  definition
"""],
["""\
term
     multi line
     definition
""",
"""\
term
  multi line
  definition
"""],
["""\
term
     1st definition paragraph

     2nd multi line
     definition paragraph
""",
"""\
term
  1st definition paragraph

  2nd multi line
  definition paragraph
"""],
["""\
term
     1st block quote definition paragraph

   2nd multi line
   definition paragraph
""",
"""\
term
    1st block quote definition paragraph

  2nd multi line
  definition paragraph
"""],
["""\
term
  definition

paragraph
""",
"""\
term
  definition

paragraph
"""],
["""\
paragraph

term
  definition
""",
"""\
paragraph

term
  definition
"""],
["""\
term
  definition
no blank line
""",
"""\
term
  definition

no blank line
"""],
["""\
A paragraph::
    A literal block without a blank line first?
""",
"""\
A paragraph::
  A literal block without a blank line first?
"""],
["""\
this is not a term;
a term may only be one line long
  this is not a definition
""",
"""\
this is not a term;
a term may only be one line long

  this is not a definition
"""],
["""\
term 1
  definition 1

term 2
  definition 2
""",
"""\
term 1
  definition 1
term 2
  definition 2
"""],
["""\
term 1
      definition 1
term 2
  definition 2
term 3
    definition 3
""",
"""\
term 1
  definition 1
term 2
  definition 2
term 3
  definition 3
"""],
["""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2
""",
"""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2
"""],
["""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2
No blank line after the definition list.
""",
"""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2

No blank line after the definition list.
"""],
["""\
term 1
  definition 1

  term 1a
    definition 1a

  term 1b
    definition 1b

term 2
  definition 2

paragraph
""",
"""\
term 1
  definition 1

  term 1a
    definition 1a
  term 1b
    definition 1b
term 2
  definition 2

paragraph
"""],
["""\
Term : classifier
    The ' : ' indicates a classifier in
    definition list item terms only.
""",
"""\
Term : classifier
  The ' : ' indicates a classifier in
  definition list item terms only.
"""],
["""\
Term  :  classifier
  Definition
""",
"""\
Term : classifier
  Definition
"""],
["""\
Term: not a classifier
    Because there's no space before the colon.
Term :not a classifier
    Because there's no space after the colon.
Term \\: not a classifier
    Because the colon is escaped.
""",
"""\
Term: not a classifier
  Because there's no space before the colon.
Term :not a classifier
  Because there's no space after the colon.
Term \\: not a classifier
  Because the colon is escaped.
"""],
["""\
Term \\: not a classifier
  Definition (fails in docutils 0.14 due to 'node.astext' not having '\\:')
""",
"""\
Term \\: not a classifier
  Definition (fails in docutils 0.14 due to 'node.astext' not having '\\:')
"""],
["""\
Term \\: not a classifier : classifier
  Definition (ok in docutils 0.14 due to classifier presence)
""",
"""\
Term \\: not a classifier : classifier
  Definition (ok in docutils 0.14 due to classifier presence)
"""],
["""\
``Term : not a classifier``
    Because the ' : ' is inside an inline literal.
""",
"""\
``Term : not a classifier``
  Because the ' : ' is inside an inline literal.
"""],
["""\
*Term : not a classifier*
  Because the ' : ' is inside an emphasis.
""",
"""\
*Term : not a classifier*
  Because the ' : ' is inside an emphasis.
"""],
["""\
Term `with *inline ``text **errors : classifier `with *errors ``too
    Definition `with *inline ``text **markup errors.
""",
"""\
Term `with *inline ``text **errors : classifier `with *errors ``too
  Definition `with *inline ``text **markup errors.
"""],
["""\
Term : `reference`_
    classifier starting with a reference crashes from release 8197 to ...
""",
"""\
Term : `reference`_
  classifier starting with a reference crashes from release 8197 to ...
"""],
["""\
Term : a `reference`_ in text : second
    classifier with reference crashes from release 8197 to ...
""",
"""\
Term : a `reference`_ in text : second
  classifier with reference crashes from release 8197 to ...
"""],
["""\
Term : classifier one  :  classifier two
    Definition
""",
"""\
Term : classifier one : classifier two
  Definition
"""],
["""\
Term : classifier *emphasis* text
  Definition
""",
"""\
Term : classifier *emphasis* text
  Definition
"""],
["""\
Term *emphasis* text
  Definition
""",
"""\
Term *emphasis* text
  Definition
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
