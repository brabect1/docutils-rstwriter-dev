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

totest['images'] = [
["""\
.. image:: picture.png
""",
"""\
.. image:: picture.png
"""],
["""\
.. image::
""",
"""\
"""],
["""\
.. image:: one two three.png
""",
"""\
.. image:: onetwothree.png
"""],
["""\
.. image:: picture.png
   :height: 100
   :width: 200
   :scale: 50
""",
"""\
.. image:: picture.png
   :width: 200
   :height: 100
   :scale: 50
"""],
["""\
.. image::
   picture.png
   :height: 100
   :width: 200
   :scale: 50
""",
"""\
.. image:: picture.png
   :width: 200
   :height: 100
   :scale: 50
"""],
["""\
.. image::
   :height: 100
   :width: 200
   :scale: 50
""",
"""\
"""],
# If there are multiple lines in the link block, they are stripped of
# leading and trailing whitespace and joined together:
["""\
.. image:: a/very/long/path/to/
   picture.png
   :height: 100
   :width: 200
   :scale: 50
""",
"""\
.. image:: a/very/long/path/to/picture.png
   :width: 200
   :height: 100
   :scale: 50
"""],
# The following two misspellings were detected in Docutils <= 0.8
# (the option block was started by any line starting with a colon
# which led to problems with named roles in other directives):
["""\
.. image:: picture.png
   :scale 50
""",
"""\
.. image:: picture.png:scale50
"""],
["""\
.. image:: picture.png
   :: 50
""",
"""\
.. image:: picture.png::50
"""],
# a missing leading colon went undetected also in Docutils <= 0.8:
["""\
.. image:: picture.png
   scale: 50
""",
"""\
.. image:: picture.pngscale:50
"""],
["""\
.. image:: picture.png
   :width: 200px
   :height: 100 em
""",
"""\
.. image:: picture.png
   :width: 200px
   :height: 100em
"""],
["""\
.. image:: picture.png
   :width: 50%
   :height: 10mm
""",
"""\
.. image:: picture.png
   :width: 50%
   :height: 10mm
"""],
["""\
.. image:: picture.png
   :width: 50%
   :height: 40%
""",
"""\
"""],
["""\
.. image:: picture.png
   :width: 20mc
""",
"""\
"""],
["""\
.. image:: picture.png
   :height: 100
   :width: 200
   :scale: 50
   :alt: Alternate text for the picture
""",
"""\
.. image:: picture.png
   :width: 200
   :height: 100
   :scale: 50
   :alt: Alternate text for the picture
"""],
["""\
.. image:: picture.png
   :scale: -50
""",
"""\
"""],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :scale:
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "image" directive:
#TODO             invalid option value: (option: "scale"; value: None)
#TODO             %s.
#TODO         <literal_block xml:space="preserve">
#TODO             .. image:: picture.png
#TODO                :scale:
#TODO """ % DocutilsTestSupport.exception_data(int, None)[1][0]],
["""\
.. image:: picture.png
   :height: 100
   :scale 50
""",
"""\
"""],
["""\
.. image:: picture.png
   :sale: 50
""",
"""\
"""],
["""\
.. image:: picture.png
   :scale is: 50
""",
"""\
"""],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :scale: fifty
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "image" directive:
#TODO             invalid option value: (option: "scale"; value: 'fifty')
#TODO             %s.
#TODO         <literal_block xml:space="preserve">
#TODO             .. image:: picture.png
#TODO                :scale: fifty
#TODO """ % DocutilsTestSupport.exception_data(int, u"fifty")[1][0]],
["""\
.. image:: picture.png
   :scale: 50
   :scale: 50
""",
"""\
"""],
["""\
.. image:: picture.png
   :alt:

(Empty "alt" option.)
""",
"""\
.. image:: picture.png
   :alt:

(Empty "alt" option.)
"""],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :target: bigpicture.png
#TODO    :name: fig:pix
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <reference refuri="bigpicture.png">
#TODO         <image ids="fig-pix" names="fig:pix" uri="picture.png">
#TODO """],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :target: indirect_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <reference name="indirect" refname="indirect">
#TODO         <image uri="picture.png">
#TODO """],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :target: a/multi/
#TODO             line/uri
#TODO 
#TODO .. image:: picture.png
#TODO    :target: `a multi line
#TODO             internal reference`_
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <reference refuri="a/multi/line/uri">
#TODO         <image uri="picture.png">
#TODO     <reference name="a multi line internal reference" refname="a multi line internal reference">
#TODO         <image uri="picture.png">
#TODO """],
#TODO ["""\
#TODO .. image:: picture.png
#TODO    :target:
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "image" directive:
#TODO             invalid option value: (option: "target"; value: None)
#TODO             argument required but none supplied.
#TODO         <literal_block xml:space="preserve">
#TODO             .. image:: picture.png
#TODO                :target:
#TODO """],
["""\
.. image:: picture.png
   :align: left
""",
"""\
.. image:: picture.png
   :align: left
"""],
["""\
.. image:: picture.png
   :align: top
""",
"""\
"""],
#TODO ["""\
#TODO .. |img| image:: picture.png
#TODO    :align: top
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <substitution_definition names="img">
#TODO         <image align="top" alt="img" uri="picture.png">
#TODO """],
#TODO ["""\
#TODO .. |img| image:: picture.png
#TODO    :align: left
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "image" directive: "left" is not a valid value for the "align" option within a substitution definition.  Valid values for "align" are: "top", "middle", "bottom".
#TODO         <literal_block xml:space="preserve">
#TODO             image:: picture.png
#TODO                :align: left
#TODO     <system_message level="2" line="1" source="test data" type="WARNING">
#TODO         <paragraph>
#TODO             Substitution definition "img" empty or invalid.
#TODO         <literal_block xml:space="preserve">
#TODO             .. |img| image:: picture.png
#TODO                :align: left
#TODO """],
#TODO [u"""\
#TODO .. image:: picture.png
#TODO    :align: \xe4
#TODO """,
#TODO u"""\
#TODO <document source="test data">
#TODO     <system_message level="3" line="1" source="test data" type="ERROR">
#TODO         <paragraph>
#TODO             Error in "image" directive:
#TODO             invalid option value: (option: "align"; value: %s)
#TODO             "\xe4" unknown; choose from "top", "middle", "bottom", "left", "center", or "right".
#TODO         <literal_block xml:space="preserve">
#TODO             .. image:: picture.png
#TODO                :align: \xe4
#TODO """ % repr(reprunicode(u'\xe4'))],
#TODO ["""
#TODO .. image:: test.png
#TODO    :target: Uppercase_
#TODO 
#TODO .. _Uppercase: http://docutils.sourceforge.net/
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <reference name="Uppercase" refname="uppercase">
#TODO         <image uri="test.png">
#TODO     <target ids="uppercase" names="uppercase" refuri="http://docutils.sourceforge.net/">
#TODO """],
#TODO [r"""
#TODO .. image:: path\ with\ spaces/name\ with\ spaces.png
#TODO    :target: path\ with\ spaces/
#TODO             target\ with\ spaces\ across\ lines.html
#TODO """,
#TODO """\
#TODO <document source="test data">
#TODO     <reference refuri="path with spaces/target with spaces across lines.html">
#TODO         <image uri="path with spaces/name with spaces.png">
#TODO """],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
