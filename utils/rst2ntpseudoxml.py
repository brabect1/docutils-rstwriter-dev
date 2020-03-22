#! /usr/bin/env python

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

"""
A modified minimal front end to the Docutils Publisher, producing pseudo-XML
without any intervening tarnsforms applied to the parsed doctree.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import docutils
import docutils.core
import docutils.io


description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + docutils.core.default_description)

parser_class = docutils.parsers.get_parser_class('restructuredtext')
parser = parser_class()

reader_class = docutils.readers.get_reader_class('standalone')
reader = reader_class()

writer_class = docutils.writers.get_writer_class('pseudoxml')
writer = writer_class()

option_parser = docutils.frontend.OptionParser(
    components=(parser, reader, writer),
    read_config_files=True,
    description=description)

settings = option_parser.parse_args()

source = docutils.io.FileInput(source=None, source_path=settings._source, encoding=settings.input_encoding)

document = reader.read(source, parser, settings)

destination = docutils.io.FileOutput(
    destination=None, destination_path=settings._destination,
    encoding=settings.output_encoding,
    error_handler=settings.output_encoding_error_handler)

output = writer.write(document, destination)
writer.assemble_parts()

