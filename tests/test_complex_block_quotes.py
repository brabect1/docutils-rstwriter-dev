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

totest['block_quotes_with_inlines'] = [
["""\
Line 1.
Line 2.

  *1st* indented *text*
  *with* multiple *lines*.

  *And* with *multiple*
  *paragraphs*.

    **2nd** indented **text**
    **with** multiple **lines**.

    **And** with **multiple**
    **paragraphs**.
""",
"""\
Line 1.
Line 2.

  *1st* indented *text*
  *with* multiple *lines*.

  *And* with *multiple*
  *paragraphs*.

    **2nd** indented **text**
    **with** multiple **lines**.

    **And** with **multiple**
    **paragraphs**.
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
