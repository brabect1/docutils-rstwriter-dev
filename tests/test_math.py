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

totest['argument'] = [
["""\
.. math:: y = f(x)
""",
"""\
.. math:: y = f(x)
"""],
]

totest['content'] = [
["""\
.. math::

  1+1=2
""",
"""\
.. math:: 1+1=2
"""],
]

totest['options'] = [
["""\
.. math::
  :name: eq:Eulers law
  :class: new

  e^i*2*\\pi = 1
""",
"""\
.. math::
   :name: eq:eulers law
   :class: new

   e^i*2*\\pi = 1
"""],
["""\
.. math:: z = x+y
  :name: eq:Eulers law

  e^i*2*\\pi = 1
  a = B + c
""",
"""\
.. math::
   :name: eq:eulers law

   z = x+y

   e^i*2*\\pi = 1
   a = B + c
"""],
["""\
.. math:: z = x+y
  :class: new
  :name: eq:Eulers law

  e^i*2*\\pi = 1
  a = B + c
""",
"""\
.. math::
   :name: eq:eulers law
   :class: new

   z = x+y

.. math::
   :class: new

   e^i*2*\\pi = 1
   a = B + c
"""],
["""\
.. math:: z = x+y
   :class: new
   :name: eq:z
.. math:: a = b *c* d
  :class: new
  :name: eq:a
""",
"""\
.. math::
   :name: eq:z
   :class: new

   z = x+y

.. math::
   :name: eq:a
   :class: new

   a = b *c* d
"""],
]

totest['argument_and_content'] = [
["""\
.. math:: y = f(x)

  1+1=2

""",
"""\
.. math:: y = f(x)

   1+1=2
"""],
]

totest['content with blank line'] = [
["""\
.. math::

  1+1=2
  \n\
  E = mc^2

  a = b * c
""",
"""\
.. math:: 1+1=2

   E = mc^2

   a = b * c
"""],
]

totest['math_role'] = [
[r"""The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
""",
r"""The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
"""],
[r"""The area of a circle is `A_\text{c} = (\pi/4) d^2`:math:.
""",
r"""The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
