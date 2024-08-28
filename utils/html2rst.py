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

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import docutils
import docutils.core
import docutils.io
import b1rst
from b1rst.parsers.html import Bs4HtmlParser

# Work around due to improper module naming: https://stackoverflow.com/questions/7583652/python-module-with-a-dash-or-hyphen-in-its-name
docutils_rstwriter = __import__("docutils-rstwriter")

description = ('Generates no-stylesheet HTML from standalone reStructuredText '
               'sources (for testing purposes).  ' + docutils.core.default_description)

parser = Bs4HtmlParser.Bs4HtmlParser()
docutils.core.publish_cmdline(writer_name='docutils-rstwriter', parser=parser, description=description)
