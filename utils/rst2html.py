# Copyright 2024 Tomas Brabec
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

"""Implements a coverter from reStructuredText to HTML with no sytesheet.

This converter oughts to generate a simpler human readable HTML and is
primarily intended to create input HTML for testing a docutils HTML parser.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import docutils
import docutils.core
import docutils.io
import docutils.writers.html4css1


class SimpleHtmlWriter(docutils.writers.html4css1.Writer):
    """Overrides use of template file for a hard-coded template string."""
    
    def apply_template(self):
        template = """<html><body>%(body)s</body></html>"""
        subs = self.interpolation_dict()
        return template % subs


settings_overrides = {'_disable_config': True,
        'xml_declaration': '',
        'stylesheet': '',
        'stylesheet_path': [],
        }

description = ('Generates no-stylesheet HTML from standalone reStructuredText '
               'sources (for testing purposes).  ' + docutils.core.default_description)

writer = SimpleHtmlWriter()
docutils.core.publish_cmdline(writer=writer, description=description, settings_overrides=settings_overrides)
