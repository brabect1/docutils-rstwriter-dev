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

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import unittest
import docutils
from docutils.core import publish_string, default_description

class MyWriterTestcase(unittest.TestCase, docutils.SettingsSpec):

    def test_pass(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        input = """My Title
========

This is my text.
"""
        output = docutils.core.publish_string(
              source=input,
              reader_name='standalone',
              parser_name='restructuredtext',
              writer_name='docutils-rstwriter',
              settings_spec=self,
              settings_overrides={})
        self.assertEqual(output, input)

    def test_unicode_cmp(self):
        s1 =  u'\u2022 BULLET'
        s2 =  u'\u2022 BULLET'
        self.assertEqual(s1, s2)

    def test_writer_unicode(self):
        input = u"""\
\u2022 BULLET
"""
        output = docutils.core.publish_string(
              source=input,
              reader_name='standalone',
              parser_name='restructuredtext',
              writer_name='docutils-rstwriter',
              settings_spec=self,
              settings_overrides={})
        self.assertEqual(output.decode('utf-8'), input)

        #print()
        #print("input='"+input+"'")
        u_exp = input
        if isinstance(u_exp, unicode):
            u_exp = u_exp.encode('raw_unicode_escape')
        #    print("enced="+u_exp)

        #print("output='"+output + "'(class=" + output.__class__.__name__ +")")
        u_act = output
        if not isinstance(u_act, unicode):
            u_act = u_act.decode('utf-8')
        u_act = u_act.encode('raw_unicode_escape')
        #print("enced ="+u_act)

        self.assertEqual(u_act, u_exp)

if __name__ == '__main__':
    unittest.main()

