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
import docutils.parsers
import docutils.nodes
import docutils.utils
import re

class HtmlParser(docutils.parsers.Parser):
    """Represents a base class of a HTML parser producing a docutils document tree."""

    supported = ('html')

    def getDefaultOptions(self):
        """Gets parser's default options.

        Return
            String indexed dictionary of default options.
        """
        return {}


class HtmlParserContext(object):

    def getDocNode(self):
        raise NotImplementedError()

    def getHtmlElement(self):
        raise NotImplementedError()


class Bs4ParserContext(HtmlParserContext):

    class InnerContext(HtmlParserContext):

        def __init__(self, node, element):
            self.node = node
            self.element = element

        def getDocNode(self):
            return self.node

        def getHtmlElement(self):
            return self.element

    def __init__(self, node, element):
        context = self.InnerContext(node, element)
        self.stack = [context]

    def getDocNode(self):
        if len(self.stack) == 0: return None
        return self.stack[-1].getDocNode()

    def getHtmlElement(self):
        if len(self.stack) == 0: return None
        return self.stack[-1].getHtmlElement()

    def pushContext(self, node, element):
        context = self.InnerContext(node, element)
        self.stack.append(context)

    def popContext(self):
        self.stack.pop()

    def peekContext(self, depth=1):
        if not isinstance(depth, int) or depth < 1:
            raise ValueError(f'Unexpected depth: {depth}')

        if len(self.stack) < depth: return self.InnerContext(None, None)
        return self.stack[-(depth+1)]


class Bs4DefaultHandler(object):

    headings = ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')

    inline = ('i', 'emph', 'b', 'strong', 'tt', 'code')

    def canHandle(self):
        return self.inline + ('html', 'body', 'div', 'p', 'a') + self.headings


    def handle(self, element, bs4HtmlParser, context):
        assert isinstance(context, Bs4ParserContext) #TODO turn to proper exception type
        t = element.name

        if t in self.inline + ('p',):
            if t in ('i', 'emph',):
                node = docutils.nodes.emphasis('', '')
            elif t in ('b', 'strong',):
                node = docutils.nodes.strong('', '')
            elif t in ('tt', 'code',):
                node = docutils.nodes.literal('', '')
            elif t == 'p':
                node = docutils.nodes.paragraph('', '')
            else:
                raise NotImplementedError(str(element))

            parent = context.getDocNode()
            parent += node #TODO replace with chained call to `append()`
            context.pushContext(node, element)
            for e in element.children: bs4HtmlParser.parseBs4(e, context=context)
            context.popContext()

            # Special case: empty parahraphs (e.g. `<p/>`)
            if t == 'p' and len(node) == 0:
                node += docutils.nodes.Text('')

        elif t == 'a':
            #TODO if element.has_attr('name'):
            #TODO     #TODO for now ignoring old way of creating an anchor target
            #TODO     return [docutils.nodes.paragraph('', '', *nodes)]
            #TODO elif element.has_attr('href'):
            #TODO     #TODO for now assuming an URL target
            #TODO     if len(nodes) == 1 and isinstance(nodes[0], docutils.nodes.Text):
            #TODO         name = nodes[0].astext()
            #TODO         #TODO for now doing no escape of `name` argument - this would form
            #TODO         #     a target ID and would likely be properly escaped
            #TODO         reference = docutils.nodes.reference('', name, name=name)
            #TODO         reference['refuri'] = element['href']
            #TODO         reference['anonymous'] = 1
            #TODO         return [reference]
            raise NotImplementedError(str(element))
        elif t in ('html', 'body','div',):
            for e in element.children: bs4HtmlParser.parseBs4(e, context=context)
        elif t in self.headings:
            # In RST, heading creates a new (sub)section and puts the heading text
            # as a title node of that section. All the following RST elements go
            # under that section, too. The section node, nor its title sub-node,
            # keeps track of section/heading's level; the level is eventually implied
            # by the document tree hierarchy.
            #
            # Hence for the HTML headings, we generally ignore heading's level. We
            # only use the level number to decide if we create a new subsection,
            # or if we need to pop context to a section closer to the document tree
            # root.
            #
            # For example:
            #
            #   <h1>H1</h1>
            #   <h5>H5</h5>
            #   <h2>H2</h2>
            #
            # would lead to the following document tree structure:
            #
            #   document
            #     - section
            #       - title H1
            #       - section
            #         - title H5
            #       - section
            #         - title H2
            #

            # section level
            slevel = 0
            parent = context.getDocNode()
            while parent is not None:
                if isinstance(parent, docutils.nodes.section): slevel += 1
                parent = parent.parent

            hlevel = int(t[1]) # heading level

            # recover the parser context to a proper level
            while hlevel <= slevel:
                parent = context.getDocNode()
                if isinstance(parent, docutils.nodes.section): slevel -= 1
                context.popContext()

            # create new section node
            node = docutils.nodes.section('')
            context.getDocNode().append(node)
            context.pushContext(node, element)

            # create new title node
            node = docutils.nodes.title('', '')
            context.getDocNode().append(node)
            context.pushContext(node, element)

            # parse the heading title
            for e in element.children: bs4HtmlParser.parseBs4(e, context=context)

            # recover the context to the section node
            # (we do not expect the context stack has been manipulated while parsing
            # the heading's text/title)
            assert isinstance(context.peekContext().getDocNode(), docutils.nodes.section)
            context.popContext()
        else:
            raise ValueError(f"Cannot handle '<{t}>' elements!")


class Bs4TableHandler(object):

    whitespace = re.compile(r'^\s*$')

    blankline = re.compile(r'^$')

    def canHandle(self):
        return ('table', 'tbody', 'thead', 'tr', 'th', 'td', 'colgroup', 'col')


    def handle(self, element, bs4HtmlParser, context):
        assert isinstance(context, Bs4ParserContext) #TODO turn to proper exception type
        t = element.name

        if t == 'table':
            # sanity check for 'row' type HTML elements
            unsupported = [e for e in element.children if self.isUnsupportedTableElement(e)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported elements under '<{t}>': {unsupported}")

            # create a new table body node and associate it with a new, empty context
            # (table parsing runs in a separate context so that structural elements
            # like headings in table cells do not interact with the incoming `context`
            # outside the table)
            tbody = docutils.nodes.tbody()
            tablecontext = Bs4ParserContext(tbody, element)
            for e in [c for c in element.children if isinstance(c, bs4.Tag)]: bs4HtmlParser.parseBs4(e, context=tablecontext)
            nodes = tbody.children

            # sanity check for 'row' type doctree subnodes
            unsupported = [n for n in nodes if not isinstance(n, docutils.nodes.row)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported doctree subnodes for a table node: {[n.__class__.__name__ for n in unsupported]}")

            cols = 0
            for r in nodes:
                rcols = 0
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

            context.getDocNode().append(table)

        elif t in ('thead', 'tbody',):
            for e in [c for c in element.children if isinstance(c, bs4.Tag)]: bs4HtmlParser.parseBs4(e, context=context)

        elif t == 'tr':
            # sanity check for 'cell' type HTML elements
            unsupported = [e for e in element.children if self.isUnsupportedRowElement(e)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported elements under '<{t}>': {unsupported}")

            row = docutils.nodes.row()
            context.getDocNode().append(row)
            context.pushContext(row, element)

            for e in [c for c in element.children if isinstance(c, bs4.Tag)]: bs4HtmlParser.parseBs4(e, context=context)

            context.popContext()

            # sanity check for 'cell' type doctree subnodes
            unsupported = [n for n in row.children if not isinstance(n, docutils.nodes.entry)]
            if len(unsupported) > 0:
                raise ValueError(f"Unsupported doctree subnodes for a row node: {[n.__class__.__name__ for n in unsupported]}")

        elif t in ('td', 'th',):
            attributes = {}
            if element.has_attr('rowspan') and int(element['rowspan']) > 1:
                attributes['morerows'] = int(element['rowspan']) - 1
            if element.has_attr('colspan') and int(element['colspan']) > 1:
                attributes['morecols'] = int(element['colspan']) - 1
            cell = docutils.nodes.entry(**attributes)
            context.getDocNode().append(cell)
            context.pushContext(cell, element)

            for e in element.children: bs4HtmlParser.parseBs4(e, context=context)

            context.popContext()

            # sanitize direct children of `Text` type, which should wrap under
            # a paragraph node
            # (Due to other inline markup, a block of free text (i.e. unwrapped in paragraph)
            # may split into a series of document tree nodes. Hence we first indentify such
            # blocks and then wrap them under paragraph nodes.)
            blocks = []
            block = []
            for n in cell.children:
                if isinstance(n, docutils.nodes.Text) or isinstance(n, docutils.nodes.Inline):
                    block.append(n)
                elif len(block) > 0:
                    blocks.append(block)
                    block = []
            if len(block) > 0: blocks.append(block)

            for block in blocks:
                p = docutils.nodes.paragraph()
                for i in range(0, len(block)):
                    n = block[i]
                    if i == 0: cell.replace(n, p)
                    else: cell.remove(n)
                    p += n

        elif t in ('colgroup', 'col',): # ignored HTML tags/elements
            pass

        else:
            raise ValueError(f"Cannot handle '<{t}>' elements!")


    def isUnsupportedRowElement(self, e):
        return (
                (isinstance(e, bs4.Tag) and e.name not in ('th', 'td',)) or
                (isinstance(e, bs4.NavigableString) and Bs4TableHandler.whitespace.match(e.string) is None)
                )


    def isUnsupportedTableElement(self, e):
        return (
                (isinstance(e, bs4.Tag) and e.name not in ('tbody', 'tr', 'thead', 'colgroup')) or
                (isinstance(e, bs4.NavigableString) and Bs4TableHandler.whitespace.match(e.string) is None)
                )


class Bs4HtmlParser(HtmlParser):

    settings_spec = (
        'HTML Parser Options',
        None,
        ())

    def __init__(self, opts=None):
        self.opts = opts or self.getDefaultOptions()
        self.handlers = {}

        defaultHandlers = [Bs4TableHandler(),
                Bs4DefaultHandler(),
                ]
        for handler in defaultHandlers:
            for tag in handler.canHandle():
                self.handlers[tag] = handler

    def parse(self, inputstring, document):
        self.parseHtml(inputstring, document)
        #TODO print(document.pformat())


    def parseHtml(self, html, document=None):
        parser = None
        if self.opts and 'html_parser' in self.opts:
            parser = self.opts['html_parser']
        parser = parser or 'html.parser'
        soup = bs4.BeautifulSoup(html, parser)
        return self.parseBs4(soup, document)


    def parseBs4(self, element, document=None, context=None):
        """Parses a BeautifulSoup element.

        Raise
            TypeError: When `element` not a bs4 BeautifulSoup type.
        """

        if element is None: return None

        if isinstance(element, bs4.BeautifulSoup):
            elements = element.children
            if document is None:
                document = docutils.utils.new_document('', None)
            if context is None:
                context = Bs4ParserContext(document, element)
        else:
            assert isinstance(context, Bs4ParserContext) #TODO change to proper exception raising
            elements = [element]

        for element in elements:
            if isinstance(element, bs4.Tag):
                t = element.name
                if t in self.handlers:
                    self.handlers[t].handle(element, self, context)
                else:
                    #TODO add a system message about unsupported HTML tag
                    pass
            elif isinstance(element, bs4.Comment):
                # Note: `bs4.Comment` is a subclass of `bs4.NavigableString` and hence
                # the former class test must precede the latter class test
                text = element.string
                comment = docutils.nodes.comment(text, text)
                parent = context.getDocNode()
                parent += comment #TODO replace with chained call to `append()`
            elif isinstance(element, bs4.NavigableString):
                s = element.string
                if Bs4TableHandler.whitespace.match(s) is None:
                    context.getDocNode().append(docutils.nodes.Text(re.sub('\n+$', '', s)))
            else:
                raise TypeError(f"Expecting bs4 type but got '{element.__class__.__name__}'")

        if document is not None:
            #TODO # docutils 0.16: reference type nodes are expected to be inside a TextElement parent
            #TODO directRefs = [n for n in document.children if isinstance(n, docutils.nodes.reference)]
            #TODO if len(directRefs) > 0:
            #TODO     p = docutils.nodes.paragraph()
            #TODO     p.extend(nodes)
            #TODO     nodes = [p]

            #TODO document.extend(nodes)
            return document
        else:
            return None


