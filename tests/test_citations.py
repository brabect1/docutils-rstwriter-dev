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

totest['citations'] = [
["""\
.. [citation] This is a citation.
""",
"""\
.. [citation] This is a citation.
"""],
["""\
.. [citation1234] This is a citation with year.
""",
"""\
.. [citation1234] This is a citation with year.
"""],
["""\
.. [citation] This is a citation
   on multiple lines.
""",
"""\
.. [citation] This is a citation
   on multiple lines.
"""],
["""\
.. [citation1] This is a citation
     on multiple lines with more space.

.. [citation2] This is a citation
  on multiple lines with less space.
""",
"""\
.. [citation1] This is a citation
   on multiple lines with more space.
.. [citation2] This is a citation
   on multiple lines with less space.
"""],
["""\
.. [citation]
   This is a citation on multiple lines
   whose block starts on line 2.
""",
"""\
.. [citation] This is a citation on multiple lines
   whose block starts on line 2.
"""],
["""\
.. [citation]

That was an empty citation.
""",
"""\
.. [citation]

That was an empty citation.
"""],
["""\
.. [citation]
No blank line.
""",
"""\
.. [citation]

No blank line.
"""],
["""\
.. [citation label with spaces] this isn't a citation

.. [*citationlabelwithmarkup*] this isn't a citation
""",
"""\
.. [citation label with spaces] this isn't a citation
.. [*citationlabelwithmarkup*] this isn't a citation
"""],
["""\
isolated internals : ``.-_``.

.. [citation.withdot] one dot

.. [citation-withdot] one hyphen

.. [citation_withunderscore] one underscore

.. [citation:with:colons] two colons

.. [citation+withplus] one plus
""",
"""\
isolated internals : ``.-_``.

.. [citation.withdot] one dot
.. [citation-withdot] one hyphen
.. [citation_withunderscore] one underscore
.. [citation:with:colons] two colons
.. [citation+withplus] one plus
"""],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
