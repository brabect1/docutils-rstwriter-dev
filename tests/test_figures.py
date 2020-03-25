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

totest['figures'] = [
["""\
.. figure:: picture.png
""",
"""\
.. figure:: picture.png
"""],
["""\
.. figure:: picture.png

   A picture with a caption.
""",
"""\
.. figure:: picture.png

   A picture with a caption.
"""],
["""\
.. figure:: picture.png

   - A picture with an invalid caption.
""",
"""\
.. figure:: picture.png
"""],
["""\
.. figure:: picture.png

   Figure caption.

   Figure legend.
""",
"""\
.. figure:: picture.png

   Figure caption.

   Figure legend.
"""],
["""\
.. figure:: picture.png

   ..

   A picture with a legend but no caption.
""",
"""\
.. figure:: picture.png

   ..

   A picture with a legend but no caption.
"""],
["""\
.. Figure:: picture.png
   :height: 100
   :width: 200
   :scale: 50

   A picture with image options and a caption.
""",
"""\
.. figure:: picture.png
   :width: 200
   :height: 100
   :scale: 50

   A picture with image options and a caption.
"""],
["""\
.. Figure:: picture.png
   :height: 100
   :alt: alternate text
   :width: 200
   :scale: 50
   :figwidth: 300
   :figclass: class1 class2
   :name: fig:pix

   A picture with image options on individual lines, and this caption.
""",
"""\
.. figure:: picture.png
   :name: fig:pix
   :width: 200
   :height: 100
   :scale: 50
   :alt: alternate text
   :figclass: class1 class2
   :figwidth: 300px

   A picture with image options on individual lines, and this caption.
"""],
["""\
.. figure:: picture.png
   :align: center

   A figure with explicit alignment.
""",
"""\
.. figure:: picture.png
   :align: center

   A figure with explicit alignment.
"""],
["""\
.. figure:: picture.png
   :align: top

   A figure with wrong alignment.
""",
"""\
"""],
["""\
This figure lacks a caption. It may still have a
"Figure 1."-style caption appended in the output.

.. figure:: picture.png
""",
"""\
This figure lacks a caption. It may still have a
"Figure 1."-style caption appended in the output.

.. figure:: picture.png
"""],
["""\
.. figure:: picture.png

   A picture with a caption and a legend.

   +-----------------------+-----------------------+
   | Symbol                | Meaning               |
   +=======================+=======================+
   | .. image:: tent.png   | Campground            |
   +-----------------------+-----------------------+
   | .. image:: waves.png  | Lake                  |
   +-----------------------+-----------------------+
   | .. image:: peak.png   | Mountain              |
   +-----------------------+-----------------------+
""",
"""\
.. figure:: picture.png

   A picture with a caption and a legend.

   +-----------------------+-----------------------+
   | Symbol                | Meaning               |
   +=======================+=======================+
   | .. image:: tent.png   | Campground            |
   +-----------------------+-----------------------+
   | .. image:: waves.png  | Lake                  |
   +-----------------------+-----------------------+
   | .. image:: peak.png   | Mountain              |
   +-----------------------+-----------------------+
"""],
["""\
.. figure:: picture.png

   ..

   A picture with a legend but no caption.
   (The empty comment replaces the caption, which must
   be a single paragraph.)
""",
"""\
.. figure:: picture.png

   ..

   A picture with a legend but no caption.
   (The empty comment replaces the caption, which must
   be a single paragraph.)
"""],
["""\
Testing for line-leaks:

.. figure:: picture.png

   A picture with a caption.
.. figure:: picture.png

   A picture with a caption.
.. figure:: picture.png

   A picture with a caption.
.. figure:: picture.png
.. figure:: picture.png
.. figure:: picture.png
.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png
""",
"""\
Testing for line-leaks:

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png

.. figure:: picture.png

.. figure:: picture.png

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png

.. figure:: picture.png

   A picture with a caption.

.. figure:: picture.png
"""],
]


def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
