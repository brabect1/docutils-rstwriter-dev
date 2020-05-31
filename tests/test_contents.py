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

totest['contents'] = [
["""\
.. contents::
""",
# Empty contents gets removed by transforms
"""\
"""],
["""\
.. contents::

Title
=====
""",
# Empty contents gets removed by transforms
"""\
.. contents::

Title
=====
"""],
["""\
.. contents:: Table of Contents

Title
=====
""",
"""\
.. contents:: Table of Contents

Title
=====
"""],
["""\
.. contents::
   Table of Contents

Title
=====
""",
"""\
.. contents:: Table of Contents

Title
=====
"""],
["""\
.. contents:: Table
     of
     Contents

Title
=====
""",
"""\
.. contents:: Table
   of
   Contents

Title
=====
"""],
#TODO ["""\
#TODO .. contents:: *Table* of ``Contents``
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <topic classes="contents" ids="table-of-contents" names="table\\ of\\ contents">
#TODO         <title>
#TODO             <emphasis>
#TODO                 Table
#TODO              of 
#TODO             <literal>
#TODO                 Contents
#TODO         <pending>
#TODO             .. internal attributes:
#TODO                  .transform: docutils.transforms.parts.Contents
#TODO                  .details:
#TODO """],
#TODO ["""\
#TODO .. contents::
#TODO    :depth: 2
#TODO    :local:
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <topic classes="contents local" ids="contents" names="contents">
#TODO         <pending>
#TODO             .. internal attributes:
#TODO                  .transform: docutils.transforms.parts.Contents
#TODO                  .details:
#TODO                    depth: 2
#TODO                    local: None
#TODO """],
#TODO ["""\
#TODO .. contents::
#TODO    :local: arg
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "contents" directive:
#TODO             invalid option value: (option: "local"; value: 'arg')
#TODO             no argument is allowed; "arg" supplied.
#TODO         <literal_block xml:space="preserve">
#TODO             .. contents::
#TODO                :local: arg
#TODO """],
#TODO ["""\
#TODO .. contents:: Table of Contents
#TODO    :local:
#TODO    :depth: 2
#TODO    :backlinks: none
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <topic classes="contents local" ids="table-of-contents" names="table\\ of\\ contents">
#TODO         <title>
#TODO             Table of Contents
#TODO         <pending>
#TODO             .. internal attributes:
#TODO                  .transform: docutils.transforms.parts.Contents
#TODO                  .details:
#TODO                    backlinks: None
#TODO                    depth: 2
#TODO                    local: None
#TODO """],
#TODO ["""\
#TODO .. contents::
#TODO    :depth: two
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "contents" directive:
#TODO             invalid option value: (option: "depth"; value: 'two')
#TODO             %s.
#TODO         <literal_block xml:space="preserve">
#TODO             .. contents::
#TODO                :depth: two
#TODO """ % DocutilsTestSupport.exception_data(int, "two")[1][0]],
#TODO ["""\
#TODO .. contents::
#TODO    :width: 2
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "contents" directive:
#TODO             unknown option: "width".
#TODO         <literal_block xml:space="preserve">
#TODO             .. contents::
#TODO                :width: 2
#TODO """],
#TODO ["""\
#TODO .. contents::
#TODO    :backlinks: no way!
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "contents" directive:
#TODO             invalid option value: (option: "backlinks"; value: 'no way!')
#TODO             "no way!" unknown; choose from "top", "entry", or "none".
#TODO         <literal_block xml:space="preserve">
#TODO             .. contents::
#TODO                :backlinks: no way!
#TODO """],
#TODO ["""\
#TODO .. contents::
#TODO    :backlinks:
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "contents" directive:
#TODO             invalid option value: (option: "backlinks"; value: None)
#TODO             must supply an argument; choose from "top", "entry", or "none".
#TODO         <literal_block xml:space="preserve">
#TODO             .. contents::
#TODO                :backlinks:
#TODO """],
#TODO ["""\
#TODO * .. contents::
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <bullet_list bullet="*">
#TODO         <list_item>
#TODO             <system_message level="3" line="1" source="test data" type="ERROR">
#TODO                 <paragraph>
#TODO                     The "contents" directive may not be used within topics or body elements.
#TODO                 <literal_block xml:space="preserve">
#TODO                     .. contents::
#TODO """],
#TODO ["""\
#TODO .. sidebar:: containing contents
#TODO 
#TODO    .. contents::
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <sidebar>
#TODO         <title>
#TODO             containing contents
#TODO         <topic classes="contents" ids="contents" names="contents">
#TODO             <title>
#TODO                 Contents
#TODO             <pending>
#TODO                 .. internal attributes:
#TODO                      .transform: docutils.transforms.parts.Contents
#TODO                      .details:
#TODO """],
]

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
