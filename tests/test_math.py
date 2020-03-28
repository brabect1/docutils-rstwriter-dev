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

#TODO totest['content'] = [
#TODO ["""\
#TODO .. math::
#TODO 
#TODO   1+1=2
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <math_block xml:space="preserve">
#TODO         1+1=2
#TODO """],
#TODO ]

#TODO totest['options'] = [
#TODO ["""\
#TODO .. math::
#TODO   :class: new
#TODO   :name: eq:Eulers law
#TODO 
#TODO   e^i*2*\\pi = 1
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <math_block classes="new" ids="eq-eulers-law" names="eq:eulers\\ law" xml:space="preserve">
#TODO         e^i*2*\\pi = 1
#TODO """],
#TODO ["""\
#TODO .. math:: z = x+y
#TODO   :class: new
#TODO   :name: eq:Eulers law
#TODO 
#TODO   e^i*2*\\pi = 1
#TODO   a = B + c
#TODO """,
#TODO """\
#TODO """],
#TODO ["""\
#TODO .. math:: z = x+y
#TODO   :class: new
#TODO   :name: eq:z
#TODO .. math:: a = b *c* d
#TODO   :class: new
#TODO   :name: eq:a
#TODO """,
#TODO """\
#TODO """],
#TODO ]

#TODO totest['argument_and_content'] = [
#TODO ["""\
#TODO .. math:: y = f(x)
#TODO 
#TODO   1+1=2
#TODO 
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <math_block xml:space="preserve">
#TODO         y = f(x)
#TODO     <math_block xml:space="preserve">
#TODO         1+1=2
#TODO """],
#TODO ]

#TODO totest['content with blank line'] = [
#TODO ["""\
#TODO .. math::
#TODO 
#TODO   1+1=2
#TODO   
#TODO   E = mc^2
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <math_block xml:space="preserve">
#TODO         1+1=2
#TODO     <math_block xml:space="preserve">
#TODO         E = mc^2
#TODO """],
#TODO ]

#TODO totest['math_role'] = [
#TODO ["""\
#TODO The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
#TODO """,
#TODO """\
#TODO The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
#TODO """],
#TODO ]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
