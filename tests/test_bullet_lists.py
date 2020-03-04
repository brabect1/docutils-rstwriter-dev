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

totest['bullet_lists'] = [
["""\
- item
""",
"""\
- item
"""],
["""\
* item 1

* item 2
""",
"""\
* item 1
* item 2
"""],
["""\
*   item 1
* item 2
""",
"""\
* item 1
* item 2
"""],
["""\
No blank line between:

+ item 1
+ item 2
""",
"""\
No blank line between:

+ item 1
+ item 2
"""],
["""\
- item 1, para 1.

  item 1, para 2.

- item 2
""",
"""\
- item 1, para 1.

  item 1, para 2.
- item 2
"""],
["""\
- item 1, line 1
  item 1, line 2
- item 2
""",
"""\
- item 1, line 1
  item 1, line 2
- item 2
"""],
["""\
Different bullets:

- item 1

+ item 2

* item 3
- item 4
""",
"""\
Different bullets:

- item 1

+ item 2

* item 3

- item 4
"""],
["""\
- item
no blank line
""",
"""\
- item

no blank line
"""],
["""\
- 

empty item above
""",
"""\
- 

empty item above
"""],
["""\
-
empty item above, no blank line
""",
"""\
- 

empty item above, no blank line
"""],
[u"""\
Unicode bullets:

\u2022 BULLET

\u2023 TRIANGULAR BULLET

\u2043 HYPHEN BULLET
""",
u"""\
Unicode bullets:

\u2022 BULLET

\u2023 TRIANGULAR BULLET

\u2043 HYPHEN BULLET
"""],
]

totest['multilevel_bullet_lists'] = [
["""\
- item

  * subitem
""",
"""\
- item

  * subitem
"""],
["""\
- item
  * still item text
""",
"""\
- item
  * still item text
"""],
["""\
- 1st item

  * 1st subitem
  * 2nd subitem
- 2nd item
""",
"""\
- 1st item

  * 1st subitem
  * 2nd subitem
- 2nd item
"""],
["""\
- 1st item

  * 1st subitem

  * 2nd subitem

- 2nd item
""",
"""\
- 1st item

  * 1st subitem
  * 2nd subitem
- 2nd item
"""],
["""\
-   1st item

    - 1st subitem
    - 2nd subitem
""",
"""\
- 1st item

  - 1st subitem
  - 2nd subitem
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

