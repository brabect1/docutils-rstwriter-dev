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


import bs4
import docutils.nodes
import docutils.utils

class HtmlParser(object):
    """Represents a base class of a HTML parser producing a docutils document tree."""

    def getDefaultOptions(self):
        """Gets parser's default options.

        Return
            String indexed dictionary of default options.
        """
        return {}


class Bs4DefaultHandler(object):

    def canHandle(self):
        return ('i', 'emph', 'b', 'strong', 'tt', 'code', 'hmtl', 'body', 'div', 'p')


    def handle(self, element, bs4HtmlParser):
        t = element.name
        nodes = []
        for e in element.children: nodes.extend(bs4HtmlParser.parseBs4(e))

        if t in ('i', 'emph',):
            return [docutils.nodes.emphasis('', '', *nodes)]
        elif t in ('b', 'strong',):
            return [docutils.nodes.strong('', '', *nodes)]
        elif t in ('tt', 'code',):
            return [docutils.nodes.literal('', '', *nodes)]
        elif t == 'p':
            return [docutils.nodes.paragraph('', '', *nodes)]
        elif t in ('html', 'body','div',):
            return nodes
        else:
            raise ValueError(f"Cannot handle '<{t}>' elements!")


class Bs4HtmlParser(HtmlParser):


    def __init__(self, opts=None):
        self.opts = opts or self.getDefaultOptions()
        self.handlers = {}

        defaultHandler = Bs4DefaultHandler()
        for tag in defaultHandler.canHandle():
            self.handlers[tag] = defaultHandler

    def parse(self, html):
        parser = None
        if self.opts and 'html_parser' in self.opts:
            parser = self.opts['html_parser']
        parser = parser or 'html.parser'
        soup = bs4.BeautifulSoup(html, parser)
        return self.parseBs4(soup)


    def parseBs4(self, element):
        """Parses a BeutifulSoup element.

        Raise
            TypeError: When `element` not a bs4 BeutifulSoup type.
        """

        if element is None: return None

        document = None
        if isinstance(element, bs4.BeautifulSoup):
            elements = element.children
            document = docutils.utils.new_document('', None)
        else:
            elements = [element]

        nodes = []
        for element in elements:
            if isinstance(element, bs4.Tag):
                t = element.name
                if t in self.handlers: nodes.extend(self.handlers[t].handle(element,self))
            elif isinstance(element, bs4.NavigableString):
                nodes.append(docutils.nodes.Text(element.string))
            elif isinstance(element, bs4.Comment):
                pass
                #lines = element.string.split('\n')
                #s = '.. ' + lines[0]
                #if len(lines) > 1:
                #    s += '\n   ' + '\n   '.join(lines[1:])
                #nodes.append(s)
            else:
                raise TypeError(f"Expecting bs4 type but got '{element.__class__.__name__}'")

        if document is not None:
            document.extend(nodes)
            return document
        else:
            return nodes


parser = Bs4HtmlParser()
html="""<p>This is <b>some <i>bold</i> test</b> text.</p><p>THis is 2nd paragraph. Here we have <tt>literal</tt> text. Let's see if <tt>literal <b>can</b> contain</tt> some other inline elements.</p>"""
document = parser.parse(html)
print(document.pformat())
print(20*'=')

import docutils.writers
import docutils.io
import docutils.frontend
writer_class = docutils.writers.get_writer_class('html')
##option_parser = self.setup_option_parser(
##    usage, description, settings_spec, config_section, **defaults)
#option_parser = self.setup_option_parser(settings_spec=writer_class.settings_spec)
#settings = option_parser.get_default_values()
writer = writer_class()
option_parser = docutils.frontend.OptionParser(
    components=(writer,),
    read_config_files=False,
    description='')
settings = option_parser.parse_args()
document.settings = settings
output = writer.write(document, docutils.io.StringOutput(encoding='utf8'))
print(output)
