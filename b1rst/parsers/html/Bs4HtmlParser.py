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
import re

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


class Bs4TableHandler(object):

    whitespace = re.compile(r'^\s*$')

    def canHandle(self):
        return ('table', 'tbody', 'tr', 'th', 'td')


    def handle(self, element, bs4HtmlParser):
        t = element.name

        if t in ('table', 'tbody',):
            # sanity check for 'row' type HTML elements
            unsupported = [e for e in element.children if self.isUnsupportedTableElement(e)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported elements under '<{t}>': {unsupported}")

            nodes = []
            for e in [c for c in element.children if isinstance(c, bs4.Tag)]: nodes.extend(bs4HtmlParser.parseBs4(e))

            if t == 'table' and len(nodes) == 1 and isinstance(nodes[0], docutils.nodes.table):
                return nodes

            # sanity check for 'row' type doctree subnodes
            unsupported = [n for n in nodes if not isinstance(n, docutils.nodes.row)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported doctree subnodes for a table node: {[n.__class__.__name__ for n in unsupported]}")

            cols = 0
            tbody = docutils.nodes.tbody()
            for r in nodes:
                rcols = 0
                tbody += r
                for c in r:
                    if isinstance(c, docutils.nodes.entry):
                        if 'colspan' in c: rcols += c['colspan']
                        else: rcols += 1

                if rcols > cols: cols = rcols

            tgroup = docutils.nodes.tgroup(cols=cols)
            for i in range(0,cols):
                #TODO temporary until proper `colwidth`
                #     (using the same value for all columns would assumably yield the even width
                #     for all columns; using 20 as a "sane" default for writers that may render
                #     the table in some plain text format)
                tgroup += docutils.nodes.colspec(colwidth=20)
            tgroup += tbody

            table = docutils.nodes.table()
            #TODO temporary until supporting proper `colwidth`
            #     (using `colwidths-auto` would assumably yield ignoring `colwidth` attributes
            #     in `colspec` subnodes of `tgroup`)
            table['classes'] += ['colwidths-auto']
            table += tgroup

            return [table]
        elif t == 'tr':
            # sanity check for 'cell' type HTML elements
            unsupported = [e for e in element.children if self.isUnsupportedRowElement(e)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported elements under '<{t}>': {unsupported}")

            nodes = []
            for e in [c for c in element.children if isinstance(c, bs4.Tag)]: nodes.extend(bs4HtmlParser.parseBs4(e))

            # sanity check for 'cell' type doctree subnodes
            unsupported = [n for n in nodes if not isinstance(n, docutils.nodes.entry)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported doctree subnodes for a row node: {[n.__class__.__name__ for n in unsupported]}")

            row = docutils.nodes.row()
            row.extend(nodes)
            return [row]
        elif t in ('td', 'th',):
            attributes = {}
            if element.has_attr('rowspan') and int(element['rowspan']) > 1:
                attributes['morerows'] = int(element['rowspan']) - 1
            if element.has_attr('colspan') and int(element['colspan']) > 1:
                attributes['morecols'] = int(element['colspan']) - 1
            cell = docutils.nodes.entry(**attributes)
            for e in element.children:
                for n in bs4HtmlParser.parseBs4(e):
                    if isinstance(n, docutils.nodes.Text):
                        p = docutils.nodes.paragraph()
                        p += n
                        cell.append(p)
                    else:
                        cell.append(n)
            return [cell]
        else:
            raise ValueError(f"Cannot handle '<{t}>' elements!")


    def isUnsupportedRowElement(self, e):
        return (
                (isinstance(e, bs4.Tag) and e.name not in ('th','td',)) or
                (isinstance(e, bs4.NavigableString) and Bs4TableHandler.whitespace.match(e.string) is None)
                )


    def isUnsupportedTableElement(self, e):
        return (
                (isinstance(e, bs4.Tag) and e.name not in ('tbody','tr',)) or
                (isinstance(e, bs4.NavigableString) and Bs4TableHandler.whitespace.match(e.string) is None)
                )


class Bs4HtmlParser(HtmlParser):


    def __init__(self, opts=None):
        self.opts = opts or self.getDefaultOptions()
        self.handlers = {}

        defaultHandlers = [Bs4TableHandler(),
                Bs4DefaultHandler(),
                ]
        for handler in defaultHandlers:
            for tag in handler.canHandle():
                self.handlers[tag] = handler

    def parse(self, html):
        parser = None
        if self.opts and 'html_parser' in self.opts:
            parser = self.opts['html_parser']
        parser = parser or 'html.parser'
        soup = bs4.BeautifulSoup(html, parser)
        return self.parseBs4(soup)


    def parseBs4(self, element):
        """Parses a BeautifulSoup element.

        Raise
            TypeError: When `element` not a bs4 BeautifulSoup type.
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
            elif isinstance(element, bs4.Comment):
                # Note: `bs4.Comment` is a subclass of `bs4.NavigableString` and hence
                # the former class test must precede the latter class test
                text = element.string
                comment = docutils.nodes.comment(text, text)
                nodes.append(comment)
            elif isinstance(element, bs4.NavigableString):
                nodes.append(docutils.nodes.Text(element.string))
            else:
                raise TypeError(f"Expecting bs4 type but got '{element.__class__.__name__}'")

        if document is not None:
            document.extend(nodes)
            return document
        else:
            return nodes


parser = Bs4HtmlParser()
html="""<p>This is <b>some <i>bold</i> test</b> text.</p><p>THis is 2nd paragraph. Here we have <tt>literal</tt> text. Let's see if <tt>literal <b>can</b> contain</tt> some other inline elements.</p>"""
html="""
<!-- source: https://www.w3schools.com/html/html_table_colspan_rowspan.asp
and so ....

... show must go on -->

<table>
<tbody><tr>
<th colspan="3">2022</th>
</tr>
    <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;  </td>
</tr>
<tr>
<th colspan="2" rowspan="2">FIESTA</th>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
"""
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
soup = bs4.BeautifulSoup(output, 'html.parser')
print(soup.prettify())
