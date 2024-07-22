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

class HtmlParser(object):
    """Represents a base class of a HTML parser producing a docutils document tree."""

    def getDefaultOptions(self):
        """Gets parser's default options.

        Return
            String indexed dictionary of default options.
        """
        return {}


class Bs4CommonlineHandler(object):

    def canHandle(self):
        return ('i', 'emph', 'b', 'strong', 'tt', 'code', 'hmtl', 'body', 'div', 'p')


    def handle(self, element, bs4HtmlParser):
        t = element.name
        nodes = []
        for e in element.children: nodes.extend(bs4HtmlParser.parseBs4(e))

        if t in ('i', 'emph',):
            return ['*' + ' '.join(nodes) +'*']
        elif t in ('b', 'strong',):
            return ['**' + ' '.join(nodes) +'**']
        elif t in ('tt', 'code',):
            return ['``' + ' '.join(nodes) +'``']
        elif t == 'p':
            return [''.join(nodes)]
        elif t in ('html', 'body','div',):
            return [' '.join(nodes)]
        else:
            raise ValueError(f"Cannot handle '<{t}>' elements!")


class Bs4HtmlParser(HtmlParser):


    def __init__(self, opts=None):
        self.opts = opts or self.getDefaultOptions()
        self.handlers = {}

        defaultHandler = Bs4CommonlineHandler()
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

        if isinstance(element, bs4.BeautifulSoup):
            elements = element.children
        else:
            elements = [element]

        nodes = []
        for element in elements:
            if isinstance(element, bs4.Tag):
                t = element.name
                if t in self.handlers: nodes.extend(self.handlers[t].handle(element,self))
            elif isinstance(element, bs4.NavigableString):
                nodes.append(element.string)
            elif isinstance(element, bs4.Comment):
                lines = element.string.split('\n')
                s = '.. ' + lines[0]
                if len(lines) > 1:
                    s += '\n   ' + '\n   '.join(lines[1:])
                nodes.append(s)
            else:
                raise TypeError(f"Expecting bs4 type but got '{element.__class__.__name__}'")

        return nodes


parser = Bs4HtmlParser()
html="""<p>This is <b>some</b> test text.</p><p>THis is 2nd paragraph.</p>"""
nodes = parser.parse(html)
print('\n\n'.join(nodes))

