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

totest['line_block_with_inlines'] = [
["""\
| *Initial* indentation is **also** significant and ``preserved:``
|
|     **Indented** 4 spaces
| *Not* indented
|   ``Indented`` 2 ``spaces``
|     Indented 4 spaces
|  Only one space
|
|     *Continuation* lines may be indented less
  *than* their *base* lines.
""",
"""\
| *Initial* indentation is **also** significant and ``preserved:``
| \n\
|   **Indented** 4 spaces
| *Not* indented
|     ``Indented`` 2 ``spaces``
|       Indented 4 spaces
|   Only one space
|   \n\
|     *Continuation* lines may be indented less
      *than* their *base* lines.
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
