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

totest['enumerated_lists'] = [
["""\
1. Item one.

2. Item two.

3. Item three.
""",
"""\
1. Item one.
2. Item two.
3. Item three.
"""],
["""\
No blank lines betwen items:

1. Item one.
2. Item two.
3. Item three.
""",
"""\
No blank lines betwen items:

1. Item one.
2. Item two.
3. Item three.
"""],
["""\
1.
empty item above, no blank line
""",
"""\
\\1.
empty item above, no blank line
"""],
["""\
Scrambled:

3. Item three.

2. Item two.

1. Item one.

3. Item three.
2. Item two.
1. Item one.
""",
"""\
Scrambled:

3. Item three.

2. Item two.

1. Item one.

\\3. Item three.
2. Item two.
1. Item one.
"""],
["""\
Skipping item 3:

1. Item 1.
2. Item 2.
4. Item 4.
""",
"""\
Skipping item 3:

1. Item 1.

\\2. Item 2.
4. Item 4.
"""],
["""\
Start with non-ordinal-1:

0. Item zero.
1. Item one.
2. Item two.
3. Item three.

And again:

2. Item two.
3. Item three.
""",
"""\
Start with non-ordinal-1:

0. Item zero.
1. Item one.
2. Item two.
3. Item three.

And again:

2. Item two.
3. Item three.
"""],
["""\
1. Item one: line 1,
   line 2.
2. Item two: line 1,
   line 2.
3. Item three: paragraph 1, line 1,
   line 2.

   Paragraph 2.
""",
"""\
1. Item one: line 1,
   line 2.
2. Item two: line 1,
   line 2.
3. Item three: paragraph 1, line 1,
   line 2.

   Paragraph 2.
"""],
["""\
Different enumeration sequences:

1. Item 1.
2. Item 2.
3. Item 3.

A. Item A.
B. Item B.
C. Item C.

a. Item a.
b. Item b.
c. Item c.

I. Item I.
II. Item II.
III. Item III.

i. Item i.
ii. Item ii.
iii. Item iii.
""",
"""\
Different enumeration sequences:

1. Item 1.
2. Item 2.
3. Item 3.

A. Item A.
B. Item B.
C. Item C.

a. Item a.
b. Item b.
c. Item c.

I. Item I.
II. Item II.
III. Item III.

i. Item i.
ii. Item ii.
iii. Item iii.
"""],
["""\
Multiline roman:

i. 1st line i
   2nd line i

ii. 1st line ii
    2nd line ii

iii. 1st line iii
  not a 2nd line iii due to wrong indent
""",
"""\
Multiline roman:

i. 1st line i
   2nd line i
ii. 1st line ii
    2nd line ii
iii. 1st line iii

  not a 2nd line iii due to wrong indent
"""],
["""\
Bad Roman numerals:

i. i

ii. ii

iii. iii

iiii. iiii
      second line

(LCD) is an acronym made up of Roman numerals

(livid) is a word made up of Roman numerals

(CIVIL) is another such word

(I) I

(IVXLCDM) IVXLCDM
""",
"""\
Bad Roman numerals:

i. i
ii. ii
iii. iii

iiii. iiii
  second line

\\(LCD) is an acronym made up of Roman numerals

\\(livid) is a word made up of Roman numerals

\\(CIVIL) is another such word

(I) I

\\(IVXLCDM) IVXLCDM
"""],
["""\
Potentially ambiguous cases:

A. Item A.
B. Item B.
C. Item C.

I. Item I.
II. Item II.
III. Item III.

a. Item a.
b. Item b.
c. Item c.

i. Item i.
ii. Item ii.
iii. Item iii.

Phew! Safe!
""",
"""\
Potentially ambiguous cases:

A. Item A.
B. Item B.
C. Item C.

I. Item I.
II. Item II.
III. Item III.

a. Item a.
b. Item b.
c. Item c.

i. Item i.
ii. Item ii.
iii. Item iii.

Phew! Safe!
"""],
["""\
Definitely ambiguous:

G. Item G.
H. Item H.
I. Item I.
II. Item II.
III. Item III.

g. Item g.
h. Item h.
i. Item i.
ii. Item ii.
iii. Item iii.
""",
"""\
Definitely ambiguous:

G. Item G.
H. Item H.

I. Item I.
II. Item II.
III. Item III.

g. Item g.
h. Item h.

i. Item i.
ii. Item ii.
iii. Item iii.
"""],
["""\
Different enumeration formats:

1. Item 1.
2. Item 2.
3. Item 3.

1) Item 1).
2) Item 2).
3) Item 3).

(1) Item (1).
(2) Item (2).
(3) Item (3).
""",
"""\
Different enumeration formats:

1. Item 1.
2. Item 2.
3. Item 3.

1) Item 1).
2) Item 2).
3) Item 3).

(1) Item (1).
(2) Item (2).
(3) Item (3).
"""],
["""\
Nested enumerated lists:

1. Item 1.

   A) Item A).
   B) Item B).
   C) Item C).

2. Item 2.

   (a) Item (a).

       I) Item I).
       II) Item II).
       III) Item III).

   (b) Item (b).

   (c) Item (c).

       (i) Item (i).
       (ii) Item (ii).
       (iii) Item (iii).

3. Item 3.
""",
"""\
Nested enumerated lists:

1. Item 1.

   A) Item A).
   B) Item B).
   C) Item C).
2. Item 2.

   (a) Item (a).

       I) Item I).
       II) Item II).
       III) Item III).
   (b) Item (b).
   (c) Item (c).

       (i) Item (i).
       (ii) Item (ii).
       (iii) Item (iii).
3. Item 3.
"""],
[u"""\
A. Einstein was a great influence on
B. Physicist, who was a colleague of
C. Chemist.  They all worked in
Princeton, NJ.

Using a non-breaking space as a workaround:

A.\u00a0Einstein was a great influence on
B. Physicist, who was a colleague of
C. Chemist.  They all worked in
Princeton, NJ.
""",
u"""\
A. Einstein was a great influence on
B. Physicist, who was a colleague of

\\C. Chemist.  They all worked in
Princeton, NJ.

Using a non-breaking space as a workaround:

A.\u00a0Einstein was a great influence on
B. Physicist, who was a colleague of
C. Chemist.  They all worked in
Princeton, NJ.
"""],
["""\
1. Item one: line 1,
   line 2.
2. Item two: line 1,
  line 2.
3. Item three: paragraph 1, line 1,
 line 2.

   Paragraph 2.
""",
"""\
1. Item one: line 1,
   line 2.
2. Item two: line 1,

  line 2.

3. Item three: paragraph 1, line 1,

  line 2.

    Paragraph 2.
"""],
["""\
1. Item one.

#. Item two.

#. Item three.
""",
"""\
1. Item one.
2. Item two.
3. Item three.
"""],
["""\
a. Item one.
#. Item two.
#. Item three.
""",
"""\
a. Item one.
b. Item two.
c. Item three.
"""],
["""\
i. Item one.
ii. Item two.
#. Item three.
""",
"""\
i. Item one.
ii. Item two.
iii. Item three.
"""],
["""\
#. Item one.
#. Item two.
#. Item three.
""",
"""\
1. Item one.
2. Item two.
3. Item three.
"""],
["""\
1. Item one.
#. Item two.
3. Item three.
""",
"""\
1. Item one.

\\#. Item two.
3. Item three.
"""],
["""\
z.
x
""",
"""\
\\z.
x
"""],
["""\
3-space indent, with a trailing space:

1. \n\
   foo

3-space indent, no trailing space:

1.
   foo

2-space indent:

1.
  foo

1-space indent:

1.
 foo

0-space indent, not a list item:

1.
foo

No item content:

1.
""",
"""\
3-space indent, with a trailing space:

1. foo

3-space indent, no trailing space:

1. foo

2-space indent:

1. foo

1-space indent:

1. foo

0-space indent, not a list item:

\\1.
foo

No item content:

1. 
"""],
]

def load_tests(loader, tests, pattern):
    return suite()


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
