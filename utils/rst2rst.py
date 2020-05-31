#!/usr/bin/python

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

from docutils.core import publish_cmdline, default_description
from docutils.core import publish_cmdline, default_description
from docutils.parsers.rst import directives

# Work around due to improper module naming: https://stackoverflow.com/questions/7583652/python-module-with-a-dash-or-hyphen-in-its-name
docutils_rstwriter = __import__("docutils-rstwriter")

# This overrides what directive class will be used to process the `image` directive
directives._directives['image'] = docutils_rstwriter.ExtendedImageDirective
directives._directives['figure'] = docutils_rstwriter.ExtendedFigureDirective

description = ('Generates RST documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='docutils-rstwriter', description=description)
