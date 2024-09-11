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

"""This test suite aggregates miscellaneous cases that were once incorrectly handled."""

from __future__ import absolute_import

import RstWriterTestUtils
import docutils
import docutils.core

def suite():
    s = RstWriterTestUtils.PublishTestSuite(writer_name='docutils-rstwriter')
    s.generateTests(totest)
    return s

totest = {}

totest['misc'] = [
# a table node as a 2nd+ node under a list item node
["""\
* item

  +--------------------+
  | table              |
  +--------------------+
""",
"""\
* item

  +--------------------+
  | table              |
  +--------------------+
"""],
# a table node as the 1st node under a list item node
["""\
* +--------------------+
  | table              |
  +--------------------+
""",
"""\
* +--------------------+
  | table              |
  +--------------------+
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
