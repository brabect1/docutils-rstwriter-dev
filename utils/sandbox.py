#!/usr/bin/env python

# $Id: rst2pseudoxml.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing pseudo-XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import docutils
from docutils.core import publish_cmdline, default_description
from docutils import frontend, nodes, statemachine, utils, io
from docutils.parsers import rst


description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + default_description)

parser = rst.Parser()
#parser_class = docutils.parsers.get_parser_class('restructuredtext')
#parser = parser_class()

reader_class = docutils.readers.get_reader_class('standalone')
reader =reader_class()

option_parser = frontend.OptionParser(components=(rst.Parser,))

settings = option_parser.parse_args()
#settings = option_parser.get_default_values()

settings.report_level = 5
settings.halt_level = 5
##settings.debug = package_unittest.debug

##settings.__dict__.update(self.suite_settings)
print settings._source
source = io.FileInput(source=None, source_path=settings._source, encoding=settings.input_encoding)
input = source.read()
print "-------------------"
print input
print "-------------------"

document = utils.new_document('test data', settings)

#input = """\
#ref_
#"""

#parser.parse(input, document)
#print document.pformat()

publish_cmdline(description=description, parser=parser, reader=reader, settings=settings)
#publish_cmdline(description=description)

