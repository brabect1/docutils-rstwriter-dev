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

totest['grid_tables'] = [
["""\
+-------------------------------------+
| A table with one cell and one line. |
+-------------------------------------+
""",
"""\
+-------------------------------------+
| A table with one cell and one line. |
+-------------------------------------+
"""],
["""\
Para before.

+-------------------------------------+
| A table with one cell and one line. |
+-------------------------------------+

Para after.
""",
"""\
Para before.

+-------------------------------------+
| A table with one cell and one line. |
+-------------------------------------+

Para after.
"""],
["""\
+-----------------------+
| A table with one cell |
| and two lines.        |
+-----------------------+
""",
"""\
+-----------------------+
| A table with one cell |
| and two lines.        |
+-----------------------+
"""],
["""\
+-----------------------+
| A malformed table. |
+-----------------------+
""",
"""\
"""],
["""\
+------------------------+
| A well-formed | table. |
+------------------------+

+------------------------+
| This +----------+ too! |
+------------------------+
""",
"""\
+------------------------+
| A well-formed | table. |
+------------------------+

+------------------------+
| This +----------+ too! |
+------------------------+
"""],
["""\
+--------------+--------------+
| A table with | two columns. |
+--------------+--------------+
""",
"""\
+--------------+--------------+
| A table with | two columns. |
+--------------+--------------+
"""],
["""\
+--------------+
| A table with |
+--------------+
| two rows.    |
+--------------+
""",
"""\
+--------------+
| A table with |
+--------------+
| two rows.    |
+--------------+
"""],
["""\
+--------------+-------------+
| A table with | two columns |
+--------------+-------------+
| and          | two rows.   |
+--------------+-------------+
""",
"""\
+--------------+-------------+
| A table with | two columns |
+--------------+-------------+
| and          | two rows.   |
+--------------+-------------+
"""],
["""\
+--------------+---------------+
| A table with | two columns,  |
+--------------+---------------+
| two rows, and a column span. |
+------------------------------+
""",
"""\
+--------------+---------------+
| A table with | two columns,  |
+--------------+---------------+
| two rows, and a column span. |
+------------------------------+
"""],
["""\
+--------------------------+
| A table with three rows, |
+------------+-------------+
| and two    | columns.    |
+------------+-------------+
| First and last rows      |
| contains column spans.   |
+--------------------------+
""",
"""\
+--------------------------+
| A table with three rows, |
+------------+-------------+
| and two    | columns.    |
+------------+-------------+
| First and last rows      |
| contains column spans.   |
+--------------------------+
"""],
["""\
+--------------+--------------+
| A table with | two columns, |
+--------------+ and a row    |
| two rows,    | span.        |
+--------------+--------------+
""",
"""\
+--------------+--------------+
| A table with | two columns, |
+--------------+ and a row    |
| two rows,    | span.        |
+--------------+--------------+
"""],
["""\
+------------+-------------+---------------+
| A table    | two rows in | and row spans |
| with three +-------------+ to left and   |
| columns,   | the middle, | right.        |
+------------+-------------+---------------+
""",
"""\
+------------+-------------+---------------+
| A table    | two rows in | and row spans |
| with three +-------------+ to left and   |
| columns,   | the middle, | right.        |
+------------+-------------+---------------+
"""],
["""\
Complex spanning pattern (no edge knows all rows/cols):

+-----------+-------------------------+
| W/NW cell | N/NE cell               |
|           +-------------+-----------+
|           | Middle cell | E/SE cell |
+-----------+-------------+           |
| S/SE cell               |           |
+-------------------------+-----------+
""",
"""\
Complex spanning pattern (no edge knows all rows/cols):

+-----------+-------------------------+
| W/NW cell | N/NE cell               |
|           +-------------+-----------+
|           | Middle cell | E/SE cell |
+-----------+-------------+           |
| S/SE cell               |           |
+-------------------------+-----------+
"""],
["""\
+--------------+
| Header       |
+==============+
| Normal cell. |
+--------------+
""",
"""\
+--------------+
| Header       |
+==============+
| Normal cell. |
+--------------+
"""],
["""\
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+
""",
"""\
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+
"""],
["""\
+-----------------+--------+
| A simple table  | cell 2 |
+-----------------+--------+
| cell 3          | cell 4 |
+-----------------+--------+
No blank line after table.
""",
"""\
+-----------------+--------+
| A simple table  | cell 2 |
+-----------------+--------+
| cell 3          | cell 4 |
+-----------------+--------+

No blank line after table.
"""],
["""\
+-----------------+--------+
| A simple table  | cell 2 |
+-----------------+--------+
| cell 3          | cell 4 |
+-----------------+--------+
    Unexpected indent and no blank line after table.
""",
"""\
+-----------------+--------+
| A simple table  | cell 2 |
+-----------------+--------+
| cell 3          | cell 4 |
+-----------------+--------+

  Unexpected indent and no blank line after table.
"""],
["""\
+--------------+-------------+
| A bad table. |             |
+--------------+             |
| Cells must be rectangles.  |
+----------------------------+
""",
"""\
"""],
["""\
+------------------------------+
| This table contains another. |
|                              |
| +-------------------------+  |
| | A table within a table. |  |
| +-------------------------+  |
+------------------------------+
""",
"""\
+------------------------------+
| This table contains another. |
|                              |
| +-------------------------+  |
| | A table within a table. |  |
| +-------------------------+  |
+------------------------------+
"""],
["""\
+------------------+--------+
| A simple table   |        |
+------------------+--------+
| with empty cells |        |
+------------------+--------+
""",
"""\
+------------------+--------+
| A simple table   |        |
+------------------+--------+
| with empty cells |        |
+------------------+--------+
"""],
#TODO [("""\
#TODO +------------------------------------------------------------------------------+
#TODO | .. include::                                                                 |
#TODO %s
#TODO +------------------------------------------------------------------------------+
#TODO | (The first cell of this table may expand                                     |
#TODO | to accommodate long filesystem paths.)                                       |
#TODO +------------------------------------------------------------------------------+
#TODO """) % ('\n'.join(['|    %-70s    |' % include2[part * 70 : (part + 1) * 70]
#TODO                    for part in range(len(include2) // 70 + 1)])),
#TODO """\
#TODO <document source="test data">
#TODO     <table>
#TODO         <tgroup cols="1">
#TODO             <colspec colwidth="78">
#TODO             <tbody>
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             Here are some paragraphs
#TODO                             that can appear at any level.
#TODO                         <paragraph>
#TODO                             This file (include2.txt) is used by
#TODO                             <literal>
#TODO                                 test_include.py
#TODO                             .
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             (The first cell of this table may expand
#TODO                             to accommodate long filesystem paths.)
#TODO """],
#TODO [("""\
#TODO Something before.
#TODO 
#TODO +------------------------------------------------------------------------------+
#TODO | .. include::                                                                 |
#TODO %s
#TODO +------------------------------------------------------------------------------+
#TODO 
#TODO Something afterwards.
#TODO 
#TODO And more.
#TODO """) % ('\n'.join(['|    %-70s    |' % include2[part * 70 : (part + 1) * 70]
#TODO                    for part in range(len(include2) // 70 + 1)])),
#TODO """\
#TODO <document source="test data">
#TODO     <paragraph>
#TODO         Something before.
#TODO     <table>
#TODO         <tgroup cols="1">
#TODO             <colspec colwidth="78">
#TODO             <tbody>
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             Here are some paragraphs
#TODO                             that can appear at any level.
#TODO                         <paragraph>
#TODO                             This file (include2.txt) is used by
#TODO                             <literal>
#TODO                                 test_include.py
#TODO                             .
#TODO     <paragraph>
#TODO         Something afterwards.
#TODO     <paragraph>
#TODO         And more.
#TODO """],
]

totest['simple_tables'] = [
["""\
============  ============
A table with  two columns.
============  ============

Paragraph.
""",
"""\
+--------------+--------------+
| A table with | two columns. |
+--------------+--------------+

Paragraph.
"""],
["""\
============  ============
A table with  two columns
and           two rows.
============  ============
""",
"""\
+--------------+-------------+
| A table with | two columns |
+--------------+-------------+
| and          | two rows.   |
+--------------+-------------+
"""],
["""\
============  ==============
A table with  two columns,
two rows, and a column span.
============================
""",
"""\
+--------------+---------------+
| A table with | two columns,  |
+--------------+---------------+
| two rows, and a column span. |
+------------------------------+
"""],
["""\
==  ===========  ===========
1   A table with three rows,
--  ------------------------
2   and three    columns.
3   First and third rows
    contain column spans.

    This row is a multi-line row, and overflows to the right.
--  ------------------------
4   One last     row.
==  ===========  ===========
""",
"""\
+---+-----------------------------------------------------------+
| 1 | A table with three rows,                                  |
+---+-----------+-----------------------------------------------+
| 2 | and three | columns.                                      |
+---+-----------+-----------------------------------------------+
| 3 | First and third rows                                      |
|   | contain column spans.                                     |
|   |                                                           |
|   | This row is a multi-line row, and overflows to the right. |
+---+-----------+-----------------------------------------------+
| 4 | One last  | row.                                          |
+---+-----------+-----------------------------------------------+
"""],
["""\
=======  =========  ========
A table with three  columns.
==================  ========
""",
"""\
+--------------------+----------+
| A table with three | columns. |
+--------------------+----------+
"""],
["""\
==============  ======
A simple table  this text extends to the right
cell 3          as does this text
==============  ======
""",
"""\
+----------------+--------------------------------+
| A simple table | this text extends to the right |
+----------------+--------------------------------+
| cell 3         | as does this text              |
+----------------+--------------------------------+
"""],
["""\
==============  ======
A simple table  this text extends to the right
                continuation of cell 2
==============  ======
""",
"""\
+----------------+--------------------------------+
| A simple table | this text extends to the right |
|                | continuation of cell 2         |
+----------------+--------------------------------+
"""],
["""\
==============  ======
A simple table  with
no bottom       border
""",
"""\
"""],
["""\
==============  ======
A simple table  cell 2
cell 3          cell 4
==============  ======
No blank line after table.
""",
"""\
No blank line after table.
"""],
["""\
==============  ======
A simple table  cell 2
==============  ======
cell 3          cell 4
==============  ======
No blank line after table.
""",
"""\
+----------------+--------+
| A simple table | cell 2 |
+================+========+
| cell 3         | cell 4 |
+----------------+--------+

No blank line after table.
"""],
["""\
==============  ======
A simple table  cell 2
cell 3          cell 4
==============  ======
    Unexpected indent and no blank line after table.
""",
"""\
  Unexpected indent and no blank line after table.
"""],
["""\
==============  ======
A bad table     cell 2
cell 3          cell 4
============  ========
""",
"""\
"""],
["""\
========  =========
A bad table  cell 2
cell 3       cell 4
========  =========
""",
"""\
"""],
["""\
==  ============================
1   This table contains another.
2   =======  ======  ========
    A table  within  a table.
    =======  ======  ========

    The outer table does have to
    have at least two columns
    though.
==  ============================
""",
"""\
+---+---------------------------------+
| 1 | This table contains another.    |
+---+---------------------------------+
| 2 | +---------+--------+----------+ |
|   | | A table | within | a table. | |
|   | +---------+--------+----------+ |
|   |                                 |
|   | The outer table does have to    |
|   | have at least two columns       |
|   | though.                         |
+---+---------------------------------+
"""],
["""\
================  ======
A simple table
with empty cells
================  ======
""",
"""\
+------------------+------+
| A simple table   |      |
+------------------+------+
| with empty cells |      |
+------------------+------+
"""],
["""\
Table cells support no alignment, hence text centering is lost.

==============  ========
   A table        with
==============  ========
   centered      cells.

==============  ========
""",
"""\
Table cells support no alignment, hence text centering is lost.

+--------------+--------+
| A table      | with   |
+==============+========+
| centered     | cells. |
+--------------+--------+
"""],
["""\
==============  ======
A simple table  this text extends to the right
cell 3          the bottom border below is too long
==============  ========
""",
"""\
"""],
["""\
Blank lines are ignored.

============  =================
A table with  row separators.
------------  -----------------

Blank line    before.
------------  -----------------

Blank lines   before and after.

------------  -----------------
Blank line    after.

============  =================
""",
"""\
Blank lines are ignored.

+--------------+-------------------+
| A table with | row separators.   |
+--------------+-------------------+
| Blank line   | before.           |
+--------------+-------------------+
| Blank lines  | before and after. |
+--------------+-------------------+
| Blank line   | after.            |
+--------------+-------------------+
"""],
["""\
============  ====================
A table with  many row separators.
------------  --------------------
------------  --------------------

------------  --------------------
============  ====================
""",
"""\
+--------------+----------------------+
| A table with | many row separators. |
+--------------+----------------------+
+--------------+----------------------+
+--------------+----------------------+
+--------------+----------------------+
"""],
#TODO ["""\
#TODO ==  ===========  ===========
#TODO 1   Span columns 2 & 3
#TODO --  ------------------------
#TODO 2   Span columns 2 & 3
#TODO     ------------------------
#TODO 3
#TODO ==  ===========  ===========
#TODO 
#TODO ==  ===========  ===========
#TODO 1 Span cols 1&2  but not 3
#TODO ---------------  -----------
#TODO 2 Span cols 1&2  but not 3
#TODO ---------------
#TODO 3   no spans     here
#TODO ==  ===========  ===========
#TODO 
#TODO ==  ===========  ===========
#TODO 1   Not a span   Not a span
#TODO     -----------  -----------
#TODO 2
#TODO ==  ===========  ===========
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="4" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Malformed table.
#TODO             Text in column margin in table line 4.
#TODO         <literal_block xml:space="preserve">
#TODO             ==  ===========  ===========
#TODO             1   Span columns 2 & 3
#TODO             --  ------------------------
#TODO             2   Span columns 2 & 3
#TODO                 ------------------------
#TODO             3
#TODO             ==  ===========  ===========
#TODO     <system_message level="3" line="13" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Malformed table.
#TODO             Column span incomplete in table line 5.
#TODO         <literal_block xml:space="preserve">
#TODO             ==  ===========  ===========
#TODO             1 Span cols 1&2  but not 3
#TODO             ---------------  -----------
#TODO             2 Span cols 1&2  but not 3
#TODO             ---------------
#TODO             3   no spans     here
#TODO             ==  ===========  ===========
#TODO     <table>
#TODO         <tgroup cols="3">
#TODO             <colspec colwidth="2">
#TODO             <colspec colwidth="11">
#TODO             <colspec colwidth="11">
#TODO             <tbody>
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             1
#TODO                     <entry>
#TODO                         <system_message level="4" line="19" source="test data" type="SEVERE">
#TODO                             <paragraph>
#TODO                                 Unexpected section title.
#TODO                             <literal_block xml:space="preserve">
#TODO                                 Not a span
#TODO                                 -----------
#TODO                     <entry>
#TODO                         <system_message level="4" line="19" source="test data" type="SEVERE">
#TODO                             <paragraph>
#TODO                                 Unexpected section title.
#TODO                             <literal_block xml:space="preserve">
#TODO                                 Not a span
#TODO                                 -----------
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             2
#TODO                     <entry>
#TODO                     <entry>
#TODO """],
#TODO ["""\
#TODO =========  =====================================================================
#TODO Inclusion  .. include::
#TODO %s
#TODO Note       The first row of this table may expand
#TODO            to accommodate long filesystem paths.
#TODO =========  =====================================================================
#TODO """ % ('\n'.join(['              %-65s' % include2[part * 65 : (part + 1) * 65]
#TODO                   for part in range(len(include2) // 65 + 1)])),
#TODO """\
#TODO <document source="test data">
#TODO     <table>
#TODO         <tgroup cols="2">
#TODO             <colspec colwidth="9">
#TODO             <colspec colwidth="69">
#TODO             <tbody>
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             Inclusion
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             Here are some paragraphs
#TODO                             that can appear at any level.
#TODO                         <paragraph>
#TODO                             This file (include2.txt) is used by
#TODO                             <literal>
#TODO                                 test_include.py
#TODO                             .
#TODO                 <row>
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             Note
#TODO                     <entry>
#TODO                         <paragraph>
#TODO                             The first row of this table may expand
#TODO                             to accommodate long filesystem paths.
#TODO """],
]



def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
