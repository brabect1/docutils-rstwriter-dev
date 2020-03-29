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

"""reStructuredText document tree Writer."""

#
#TODO List of problems detected in docutils
#
# - `subtitle` has empty `rawtext`
# - info on title overline in source text not available
#

__docformat__ = 'reStructuredText'

import re
import roman
import textwrap
import tableclass

import docutils
from docutils import frontend, nodes, utils, writers, languages, io
from docutils.transforms import writer_aux
try:
    from docutils.utils.error_reporting import SafeString
    from docutils.utils.math import unichar2tex, pick_math_environment
    from docutils.utils.math.latex2mathml import parse_latex_math
    from docutils.utils.math.math2html import math2html
except ImportError:
    from docutils.error_reporting import SafeString
    from docutils.math import unichar2tex, pick_math_environment
    from docutils.math.latex2mathml import parse_latex_math
    from docutils.math.math2html import math2html


class Options(object):
    """Options for rst to rst conversion."""
    def __init__(self):
        self.title_chars = [u'#', u'*', u'=', u'-', u'^', u'"']
        """List of symbols used to underline and overline titles.

        List indices are "heading level - 1", i.e. at index 0 is the symbol
        used to underline/overline "H1".

        """

        self.title_prefix = [u'', u'\n', u'', u'', u'', u'']
        """List of prefixes before title and overline (typically, blank lines).

        Indices represent heading level.

        """

        self.title_suffix = [u'\n\n'] * 6
        """List of suffixes after title and underline (typically, blank lines).

        Indices represent heading level.

        """

        self.title_overline = [True, True, False, False, False, False]
        """List of booleans specifying whether to overline the title or not.

        List indices represent heading level.

        """

        self.indentation_char = u' '
        """Character used for indentation.

        Should be space or tab. Default is space.

        """

        self.blockquote_indent = 2
        """Indentation level for blockquotes."""

        self.wrap_length = 79
        """Wrap length, i.e. maximum text width, as number of chararcters."""

        self.bullet_character = ['*'] * 6
        """List of symbols used for bullet lists."""


class Writer(writers.Writer):
    supported = ('txt')  # Formats this writer supports.
    config_section = 'rst writer'
    config_section_dependencies = ('writers',)

    def __init__(self):
        writers.Writer.__init__(self)
        self.options = Options()

    def translate(self):
        self.abc()
        self.output = "<class=" + self.document.__class__.__name__ + ">\n";
        self.output = self.xyz()

        s = "";
        for i in self.document.traverse():
            if isinstance(i, nodes.title) or isinstance(i, nodes.subtitle):
                x = i.astext();
                s += x + "\n" + ("-" * len(x)) + "\n\n"
            elif isinstance(i, nodes.Text):
                indent = self.get_indent(i.parent)
                lines = [indent+line for line in i.astext().splitlines()]
                if lines:
                    s += '\n'.join(lines) + '\n'
            elif isinstance(i, nodes.paragraph):
                p = i.parent
                if not isinstance(p, nodes.list_item): s += '\n'
            elif isinstance(i, nodes.list_item):
                if i.parent.index(i) == 0: s += "\n"

        self.output = s

        visitor = RstCollectVisitor(self.document, self.options)
        self.document.walkabout(visitor)
        self.output = visitor.text
        #self.output = self.document.pformat()


    @classmethod
    def get_sec_level(cls, node):
        """
          There are three cases to consider (all are due to `frontmatter`
          transform happening on the parsed input). First::

              Title
              =====

              Subtitle
              --------

          which yields::

              <document>
                  <title>
                  <subtitle>

          Second::

              Title
              =====

              Subtitle 1
              ----------

              Subtitle 2
              ----------

          which yields::

              <document>
                  <title>
                  <section>
                      <title>
                  <section>
                      <title>

          And eventually third::

              Title 1
              =======

              Subtitle 1
              ----------

              Title 2
              =======

          which yields::

              <document>
                  <section>
                      <title>
                      <section>
                          <title>
                  <section>
                      <title>
        """
        if isinstance(node, nodes.document):
            # This will be called for the 1st (`title` and `subtitle`) and
            # 2nd case (`title` only)
            return 0
        elif isinstance(node, nodes.section):
            # This will be called for the 2nd (`subtitle` only) and 3rd case.
            # To distinguish the two, we need to see if the `document` node
            # contains a `title` child.
            i=0
            while node==None or not isinstance(node, nodes.document):
                node = node.parent
                i += 1
            if isinstance(node, nodes.document):
                hastitle = 0
                for c in node.children:
                    if isinstance(c, nodes.title):
                        hastitle = 1
                        break
                if not hastitle:
                    i -= 1
            return i
        else:
            return -1

    @classmethod
    def get_parent_element(cls, node):
        if node == None: 
            return None
        elif not isinstance(node, nodes.Element) or isinstance(node, nodes.Inline):
            p = node.parent
            while p!=None and (not isinstance(p, nodes.Element) or isinstance(p, nodes.Inline)):
                p = p.parent
            return p
        else:
            return node.parent

    @classmethod
    def get_indent(cls, node):
        if node == None: 
            return str("")
        elif node.hasattr("iprefix"):
            return node.get("iprefix");
        else:
            #print "# <class=" + node.__class__.__name__ + ">"
            s = str("")
            n = node
            while not (isinstance(n, nodes.document) or isinstance(n, nodes.section)):
                p = n.parent
                if p.hasattr("iprefix"):
                    s = p.get("iprefix")
                    if isinstance(p, nodes.list_item):
                        #if not isinstance(n, nodes.paragraph) or p.index(n)!=0:
                            l = len(s)
                            s = cls.get_indent(p.parent)
                            s += " " * (l - len(s))
                    #print "## " + n.__class__.__name__ + "=" + s;
                    break
                n = p

            if isinstance(node, nodes.entry):
                # This signals a table cell, hence we reset the indent.
                s = ''
            elif isinstance(node, nodes.block_quote) or isinstance(node, nodes.literal_block):
                s += "  "
            elif isinstance(node, nodes.line_block):
                if isinstance(node.parent, nodes.line_block):
                    s += '  '
                else:
                    s += "| "
            elif isinstance(node, nodes.list_item):
                if isinstance(node.parent, nodes.bullet_list):
                    s += node.parent.get("bullet")+" "
                elif isinstance(node.parent, nodes.enumerated_list):
                    p = node.parent
                    enumtype = p.get("enumtype")
                    pfx = p.get("prefix")
                    sfx = p.get("suffix")
                    start = p.get("start")
                    if start == None:
                        start = 1
                    start += p.index(node)
                    if enumtype == "arabic":
                        idx = 1
                    elif enumtype == "upperalpha":
                        idx = 'A'
                    elif enumtype == "loweralpha":
                        idx = 'a'
                    elif enumtype == 'upperroman':
                        idx = 'I'
                    elif enumtype == 'lowerroman':
                        idx = 'i'
                    else:
                        idx = '#'
                    if idx != '#':
                        if enumtype == "arabic":
                            idx += start-1
                        elif enumtype == 'upperroman':
                            idx = roman.toRoman(roman.fromRoman(idx)+start-1)
                        elif enumtype == 'lowerroman':
                            idx = roman.toRoman(roman.fromRoman(idx.upper())+start-1).lower()
                        else:
                            idx = chr(ord(idx)+start-1)
                    s += pfx+str(idx)+sfx+" "
            elif isinstance(node, nodes.definition_list_item):
                s += ""
            elif isinstance(node, nodes.definition):
                s += "  "
            elif isinstance(node, nodes.field_body):
                s += "  "
            elif isinstance(node, nodes.comment):
                s += "   "
            elif isinstance(node, nodes.Admonition):
                s += "   "
            elif isinstance(node, nodes.image) and not isinstance(node.parent, nodes.figure):
                s += "   "
            elif isinstance(node, nodes.figure):
                s += "   "
            elif isinstance(node, nodes.footnote):
                s += "   "
            elif isinstance(node, nodes.citation):
                s += "   "
            elif isinstance(node, nodes.math_block):
                s += "   "

            return s

    @classmethod
    def get_refids(cls, document):
        if not document or not isinstance(document, nodes.document):
            return {}
        else:
            ids_hash = {}
            for node in document.traverse():
                if 'ids' in node:
                    if isinstance(node, nodes.system_message):
                        continue

                    ids = node['ids']

                    #if 'anonymous' in node and node['anonymous']==1:
                    if 'anonymous' in node:
                        for refid in node['ids']:
                            ids_hash[refid] = None
                    else:
                        assert 'names' in node
                        if len(node['names']) > 0:
                            # In case of dangling references, there might be `target` nodes
                            # with less `ids` than `names`
                            assert len(ids) <= len(node['names'])
                            names = 'names'
                        else:
                            assert 'dupnames' in node
                            assert len(ids) == len(node['dupnames'])
                            names = 'dupnames'

                        for refid, name in zip(ids, node[names][:len(ids)]):
                            ids_hash[refid] = name
            return ids_hash

    def abc(self):
        for i in self.document.traverse():
            if isinstance(i, nodes.title):
                i.replace_attr("hlevel", Writer.get_sec_level(i.parent))
            elif isinstance(i, nodes.subtitle):
                i.replace_attr("hlevel", Writer.get_sec_level(i.parent)+1)

            if isinstance(i, nodes.Element):
                s = Writer.get_indent(i)
                i.replace_attr("iprefix", s)
                #print "## setting " + i.__class__.__name__ + ".iprefix='" + s + "'"
                #print "## getting " + i.__class__.__name__ + ".iprefix='" + i.get("iprefix") + "'"

    def xyz(self):
        str = '';
        l = self.document.traverse()
        for i in l:
            if isinstance(i, nodes.Element):
                str += self.indent(i) + "<" + i.__class__.__name__ + ">\n"
            elif isinstance(i, nodes.Text):
                str += self.indent(i) + i.astext() + "\n"

        return str

    def indent(self, node):
        if isinstance(node, nodes.Node):
            i=0;
            while node.parent != None and i < 100:
                i += 1
                node = node.parent
            if i==100:
                return "ERROR\t"
            else:
                return ' ' * 4 * i
        else:
            return ''

class RstCollectVisitor(nodes.SparseNodeVisitor):

    def __init__(self, document, options):
        self.document = document
        self.options = options
        self.tstack = ''
        self.text = ''
        self.tstack_stack = []
        self.heads = ["=", "-", ".", "~", "^"]
        self.table = []
        self.table_rowcells = []
        self.table_tstacks = []
        self.ref_ids = None
        nodes.SparseNodeVisitor.__init__(self, document)

    def vindent(self):
        if len(self.tstack)==0: return ''
        else: return '\n'

    def push_tstack(self):
        self.tstack_stack.append(self.tstack)
        self.tstack = ''

    def pop_tstack(self):
        if len(self.tstack_stack) > 0:
            self.tstack = self.tstack_stack.pop() + self.tstack

    def visit_document(self, node):
        if 'title' in node:
            title = node['title']
            if len(node.children) > 0 and isinstance(node[0], nodes.title):
                if title == node[0].astext():
                    title = None

            if title:
                self.tstack += self.vindent()
                self.tstack += '.. title:: ' + title + '\n'

    def depart_document(self, node):
        if len(self.text)>0: self.text += '\n'
        self.text += self.tstack
        self.tstack = ''

    def depart_Text(self, node):
        #self.tstack += "<!>"
        pass

    def visit_Text(self, node):
        # Since ``Text`` node is not an ``Element``, it cannot have attributes
        # and hence we need to get indentation from the ``Text`` instance
        # parent in the doc tree.
        pe = Writer.get_parent_element(node)
        pn = node.parent
        indent = Writer.get_indent(pe)
        lines = []
        i=0
        if isinstance(pe, nodes.term):
            #TODO # `term` shall be a one liner so we can replace `line`
            #TODO # with a `rawsource` text (this adds back extra escaping
            #TODO # that may be part of the term)
            #TODO # 22-Feb-2020/docutils.0.14: Terms with classifiers do
            #TODO # have `rawsource` empty. Hence we do:
            #TODO # a) use `node.parent.rawsource` instead of `node.rawsource`
            #TODO # b) ignore all `classifier` as they will be already part
            #TODO #    of `term`'s parrent rawsource
            #TODO lines.append(Writer.get_indent(pe.parent)+pn.rawsource)
            s = node.astext()
            if pe == pn:
                # Unless the `term` is embedded inside an inline element,
                # then do escape the colon character.
                s = s.replace(':', '\\:')
            lines.append(Writer.get_indent(pe.parent)+s)
        else:
            for line in node.astext().splitlines(True):
                if pe==pn and isinstance(pe, nodes.paragraph) and len(line) > 0:
                    # We need to escape the escape character.
                    line = line.replace('\\', '\\\\')

                    # We need to escape some of the line starting chracters so they
                    # do not alias with a start of another element.
                    if line[0]=='|':
                        line = '\\'+line
                    elif line[0].isspace():
                        ni = pn.index(node)
                        if ni == 0 or isinstance(pn[ni-1], nodes.Text):
                            line = '\\ '+line
                    elif i == 0 and pn.index(node) == 0:
                        if re.match(docutils.parsers.rst.states.Body.patterns['bullet'], line):
                            line = '\\'+line
                        elif re.match(docutils.parsers.rst.states.Body.patterns['enumerator'], line):
                            line = '\\'+line
                    pass

                if i==0:
                    if isinstance(pe, nodes.paragraph) and isinstance(pe.parent, nodes.list_item) and pe.parent.index(pe)==0:
                        lines.append(Writer.get_indent(pe.parent)+line)
                        #lines.append(Writer.get_indent(pe.parent)+line+"#"+str(i))
                    elif isinstance(pe, nodes.paragraph) and isinstance(pe.parent, nodes.field_body) and pe.parent.index(pe)==0:
                        lines.append(' '+line)
                    elif isinstance(pe, nodes.paragraph) and isinstance(pe.parent, nodes.Admonition) and pe.parent.index(pe)==0:
                        lines.append(' '+line)
                    elif isinstance(pe, nodes.paragraph) and (isinstance(pe.parent, nodes.footnote) or isinstance(pe.parent, nodes.citation)) and pe.parent.index(pe)==1:
                        lines.append(' '+line)
                    elif isinstance(pe, nodes.title) and isinstance(pe.parent, nodes.admonition):
                        lines.append(' '+line)
                    elif isinstance(pe, nodes.attribution):
                        lines.append(indent + '-- ' + line)
                    elif isinstance(pe, nodes.comment):
                        lines.append(line)
                    elif isinstance(pe, nodes.math_block):
                        lines.append(line)
                    elif isinstance(pe, nodes.line):
                        if isinstance(pe.parent, nodes.line_block):
                            if len(line) > 0 and line[-1]=='\n':
                                lines.append(line+' '*len(indent))
                            else:
                                lines.append(line)
                            #TODO if len(self.tstack)==0 or self.tstack[-1]=='\n':
                            #TODO     lines.append(indent+line)
                            #TODO else:
                            #TODO     lines.append('<='+self.tstack[-1]+'>'+line)
                        else:
                            lines.append('<!>'+line)
                    else:
                        if isinstance(pn, nodes.Inline):
                            #line = "<>"+line+"</>"
                            pass
                        ps = node
                        while (ps.parent != None and ps.parent != pe):
                            ps = ps.parent
                        #lines.append(indent+line+"#"+str(i)+",pe="+pe.__class__.__name__+"#")
                        #x = pe.index(ps)
                        #lines.append(indent+line+"#"+str(i)+",x="+str(x)+",pe="+pe.__class__.__name__+"#")
                        if (ps.parent==pe and pe.index(ps) > 0):
                            lines.append(line)
                        else:
                            lines.append(indent+line)
                else:
                    if isinstance(pe, nodes.line) and isinstance(pe.parent, nodes.line_block):
                        if len(line) > 0 and line[-1]=='\n':
                            lines.append(line+' '*len(indent))
                        else:
                            lines.append(line)
                    else: 
                        #lines.append(indent+line+"#"+str(i))
                        lines.append(indent+line)
                i += 1

        # For the `title` node of an `admonition` node, we need to
        # see if there are `class` and `name` attributes.
        if isinstance(pe, nodes.title) and isinstance(pe.parent, nodes.admonition):
            admonition = pe.parent
            hasNames = 'names' in admonition and len(admonition['names']) > 0
            hasClasses = 'classes' in admonition and len(admonition['classes']) > 0

            if hasNames:
                lines.append('\n' + indent + ':name: ' + ' '.join(admonition['names']))

            if hasClasses:
                # The `admonition` node type always has the `class` attribute,
                # either the default one or a user one. We ignore the default
                # one.
                defaultClass='admonition-'+nodes.make_id(pe.astext())
                if defaultClass != admonition['classes'][0]:
                    lines.append('\n' + indent + ':class: ' + ' '.join(admonition['classes']))

        if lines:
            #self.tstack += node.astext()+"<!>"
            #self.tstack += ''.join(node.astext().splitlines(True))+"!"
            self.tstack += ''.join(lines)# + '\n'

    def visit_title(self, node):
        if not isinstance(node.parent, nodes.admonition):
            x = node.rawsource;
            if x:
                # Normally we would leave formatting of children to be resolved
                # by descending in the node tree. However, titles are one liners
                # and so we may take the raw form right away.
                self.tstack += self.vindent() + x
                raise nodes.SkipChildren()
            else:
                # There are rare exceptions (e.g. `subtitle` nodes) when rawsource
                # is empty. There we let the node tree parsing/walking go on.
                self.tstack += self.vindent()

    def depart_title(self, node):
        if isinstance(node.parent, nodes.admonition):
            # Need to add newline as we would do with an ordinary
            # paragraph
            self.tstack += '\n'
        else:
            lvl = node.get("hlevel")
            if lvl == None:
                lvl = 0;
            if lvl >= len(self.heads):
                lvl = len(self.heads)-1
            x = node.rawsource;
            if not x:
                # When we do not have a rawsource (e.g. `subtitle` nodes), the
                # title character length based on `node.astext()` may be too
                # small (e.g. `*Emphasis title*` becomes "astext" `Emphasis title`).
                # Hence we use twice that length!
                x = node.astext() * 2;
            self.tstack += "\n" + (self.heads[lvl] * len(x)) + "\n"

    def visit_subtitle(self, node):
        self.visit_title(node)

    def depart_subtitle(self, node):
        self.depart_title(node)

    def visit_paragraph(self, node):
        p = node.parent
        if not (isinstance(p, nodes.list_item) or isinstance(p, nodes.field_body) or isinstance(p, nodes.Admonition) or isinstance(p, nodes.footnote) or isinstance(p, nodes.citation)):
            # For all but a paragraph in certain elements add a vertical space
            # before the paragraph. The special elements are:
            # - list_item's
            # - field_body's
            # - admonitions
            # - footnotes
            # - citations
            self.tstack += self.vindent()
        elif p.index(node) != 0 and \
                not (p.index(node) == 1 and (isinstance(p, nodes.footnote) or isinstance(p, nodes.citation))):
            # For 2nd+ paragraph in a list item we need to add a vertical
            # space.
            self.tstack += self.vindent()
        #else: self.tstack += '\n'
        #self.tstack += node.astext()
        #raise nodes.SkipChildren()

    def depart_paragraph(self, node):
        self.tstack += '\n'

    def visit_system_message(self, node):
        #TODO self.tstack += "!!!"
        raise nodes.SkipChildren()

    def visit_attribution(self, node): self.tstack += self.vindent()
    def depart_attribution(self, node): self.tstack += '\n'

    def visit_field_name(self, node): self.tstack += ':'
    def depart_field_name(self, node): self.tstack += ':'

    def visit_strong(self, node): self.tstack += '**'
    def depart_strong(self, node): self.tstack += '**'

    def visit_emphasis(self, node): self.tstack += '*'
    def depart_emphasis(self, node): self.tstack += '*'

    def visit_literal(self, node): self.tstack += '``'
    def depart_literal(self, node): self.tstack += '``'

    def visit_math(self, node): self.tstack += ':math:`'
    def depart_math(self, node): self.tstack += '`'

    def visit_reference(self, node):
        assert 'name' in node or 'refuri' in node
        if 'name' in node:
            if 'refuri' in node:
                self.tstack += '`'
            else:
                name = node['name']
                if len(name.split()) > 1:
                    # this must be a phrase reference
                    self.tstack += '`'
        elif 'refuri' in node:
            pass

        # save the text stack and reset it (to empty)
        self.push_tstack()

    def depart_reference(self, node):
        # In case of phrase references, we need to excape the phrase text.
        # A `reference` node shall have only `Text` underneath. Since we saved text stack
        # and reset text stack on `reference` visit, we can escape the whole text stack.
        for (k,v) in RstCollectVisitor.reference_phrase_escapes:
            if k in self.tstack: self.tstack = self.tstack.replace(k,v);

        if 'name' in node:
            if 'refuri' in node:
                refuri = node['refuri']
                # Check if we can simplify the reference to a form of `<refuri>`_.
                if refuri==self.tstack:
                    self.tstack = ''
                else:
                    self.tstack += ' '

                for (k,v) in RstCollectVisitor.refuri_escapes:
                    if k in refuri: refuri = refuri.replace(k,v);
                self.tstack += '<' + refuri + '>`'
            else:
                name = node['name']
                if len(name.split()) > 1:
                    # this must be a phrase reference
                    self.tstack += '`'
                elif name[-1]=='_':
                    # need to escape the last underscore and use backticks
                    self.tstack = '`' + self.tstack[:-1] + '\\_`'
            self.tstack += '_'
            if 'anonymous' in node and node['anonymous']==1:
                self.tstack += '_'
        elif 'refuri' in node:
            pass

        # restore the last text stack and append the present contents to it
        self.pop_tstack()

    def visit_footnote_reference(self, node):
        self.tstack += '['
        if 'auto' in node and (node['auto']==1 or node['auto']=='*'):
            if node['auto']==1:
                self.tstack += '#'
            else:
                self.tstack += '*'
            if 'refname' in node:
                self.tstack += node['refname']

    def depart_footnote_reference(self, node):
        self.tstack += ']_'

    def visit_citation_reference(self, node):
        self.tstack += '['

    def depart_citation_reference(self, node):
        self.tstack += ']_'

    reference_phrase_escapes = [
            ('\\', '\\\\'),
            ('`', '\`'),
            ('<', '\<'),
            ]

    refuri_escapes = [
            ('\\', '\\\\'),
            (' ', '\ '),
            ('_', '\_'),
            ]

    target_name_escapes = [
            ('\\', '\\\\'),
            (':', '\\:'),
            ]

    def visit_target(self, node):
        if not self.ref_ids:
            self.ref_ids = Writer.get_refids(self.document)
            #TODO for (k,v) in self.ref_ids.items():
            #TODO     print '>> ' + k + ' = ' + v

        if len(node.children) > 0:
            self.tstack += '_`'
        else:
            #if not ('refuri' in node or 'refid' in node or 'refname' in node): # indirect target ???
            p = node.parent
            if isinstance(p, nodes.document) or isinstance(p, nodes.section):
                if 'refid' in node:
                    refid = node['refid']
                    assert refid in self.ref_ids
                    name = self.ref_ids[refid]
                else:
                    #if 'anonymous' in node and node['anonymous']==1:
                    if 'anonymous' in node:
                        name = '_'
                    else:
                        assert 'names' in node
                        if len(node['names']) > 0:
                            name = node['names'][0]
                        else:
                            assert 'dupnames' in node
                            name = node['dupnames'][0]

                for (k,v) in RstCollectVisitor.target_name_escapes:
                    if k in name: name = name.replace(k,v);

                if name != '_' and name[0]=='_': name = '\\'+name

                self.tstack += self.vindent() + Writer.get_indent(node.parent) + ".. "
                self.tstack += '_' + name + ":"
                if 'refuri' in node:
                    self.tstack += " " + node['refuri']
                elif 'refname' in node:
                    refname = node['refname']
                    if len(refname.split()) > 1:
                        refname = '`' + refname + '`'
                    self.tstack += " " + refname + '_'
                self.tstack += "\n"

    def depart_target(self, node):
        if len(node.children) > 0:
            self.tstack += '`'

    def visit_classifier(self, node): self.tstack += ' : '

    def visit_definition_list_item(self, node):
        if node.parent.index(node) == 0: self.tstack += self.vindent()

    def visit_list_item(self, node):
        if node.parent.index(node) == 0: self.tstack += self.vindent()

        # Special case: List item with no text.
        if len(node.children)==0:
            self.tstack += Writer.get_indent(node) + "\n"

    def visit_literal_block(self, node):
        hindent = Writer.get_indent(node)
        self.tstack += self.vindent() + hindent[:-2] + "::\n\n"

    def depart_literal_block(self, node):
        self.tstack += "\n"

    def visit_line_block(self, node):
        if not isinstance(node.parent, nodes.line_block):
            self.tstack += self.vindent()

    def visit_line(self, node): self.tstack += Writer.get_indent(node)
    def depart_line(self, node): self.tstack += "\n"

    def visit_comment(self, node):
        #self.tstack += self.vindent() + Writer.get_indent(node.parent) + ".. "
        self.tstack += self.vindent() + ' '*len(Writer.get_indent(node.parent)) + ".. "

    def depart_comment(self, node): self.tstack += "\n"

    def visit_table(self, node):
        if len(self.table) == 0:
            self.text += self.tstack
            self.tstack = ''
        self.table.append( tableclass.tableclass() )
        self.table_tstacks.append( self.tstack )
        self.table_rowcells.append( [] )
        self.tstack = ''

    def depart_table(self, node):
        assert len(self.table) != 0
        assert len(self.table) == len(self.table_tstacks)
        assert len(self.table) == len(self.table_rowcells)

        table = self.table.pop()
        self.table_rowcells.pop()

        self.tstack = self.table_tstacks.pop()
        if self.tstack: self.tstack += self.vindent()
        self.tstack += table.format(prefix=Writer.get_indent(node.parent)) + '\n'
        #TODO cell = self.table.get_cell(4,3)
        #TODO print '-------' + str(cell.get_lineheight()) + ' ' + str(cell.lessrows)
        #TODO for l in cell.get_text().splitlines():
        #TODO     print l
        #TODO print '-------'
        #TODO rowcount = len(self.table.rows)
        #TODO rowheights = self.table.get_rowheights( rowcount )
        #TODO print rowheights
        #TODO print '~~~~~~~'

    def visit_colspec(self, node):
        if 'colwidth' in node and len(self.table) != 0:
            self.table[-1].colwidths.append( node['colwidth'] - 2 )

    def visit_row(self, node):
        assert len(self.table_rowcells) != 0
        self.table_rowcells[-1] = []

    def depart_row(self, node):
        assert len(self.table) != 0
        self.table[-1].add_row( self.table_rowcells.pop() )
        self.table_rowcells.append( [] )

        if isinstance(node.parent, nodes.thead):
            # Identify the last row as a header.
            # (Only the last row can be a header as there can be
            # a sole header rule in the table.)
            rows = self.table[-1].rows
            assert len(rows) > 0
            for r in rows: r.isheader = 0
            rows[-1].isheader = 1

    def visit_entry(self, node):
        self.tstack = ''

    def depart_entry(self, node):
        morecols = 0
        morerows = 0
        if 'morerows' in node: morerows = node['morerows']
        if 'morecols' in node: morecols = node['morecols']

        cell = tableclass.MultiCell(text=self.tstack,
                morerows=morerows, morecols=morecols)
        self.table_rowcells[-1].append( cell )

    def visit_note(self, node):
        p = node.parent
        if not isinstance(p, nodes.list_item):
            self.tstack += self.vindent()
        self.tstack += Writer.get_indent(node.parent)
        self.tstack += ".. " + node.__class__.__name__ + '::'

        indent = Writer.get_indent(node)
        hasNames = 'names' in node and len(node['names']) > 0
        hasClasses = 'classes' in node and len(node['classes']) > 0

        if hasNames or hasClasses:
            self.tstack += '\n'

        if hasNames:
            self.tstack += indent + ':name: ' + ' '.join(node['names']) + '\n'

        if hasClasses:
            self.tstack += indent + ':class: ' + ' '.join(node['classes']) + '\n'

        if (hasNames or hasClasses) and len(node.children) > 0:
            # using indent less one space (as the space will be
            # added by the `visit_Text` method)
            self.tstack += '\n' + ' '*(len(indent)-1)

    def visit_attention(self, node):    self.visit_note(node)
    def visit_caution(self, node):      self.visit_note(node)
    def visit_danger(self, node):       self.visit_note(node)
    def visit_error(self, node):        self.visit_note(node)
    def visit_important(self, node):    self.visit_note(node)
    def visit_tip(self, node):          self.visit_note(node)
    def visit_hint(self, node):         self.visit_note(node)
    def visit_warning(self, node):      self.visit_note(node)

    def visit_admonition(self, node):
        # This admonition class is special as it renders the 1st
        # paragraph as a title and that `class` and `name`
        # attributes shall come only after the title. Hence the
        # attributes are processed within the `visit_Text` method.
        self.tstack += self.vindent() + Writer.get_indent(node.parent)
        self.tstack += ".. " + node.__class__.__name__ + '::'

    image_attr_map = [
            ('names', 'name'),
            ('classes', 'class'),
            ('width', 'width'),
            ('height', 'height'),
            ('scale', 'scale'),
            ('alt', 'alt'),
            ('align', 'align')
            ]

    figure_attr_map = [
            ('classes', 'figclass'),
            ('width', 'figwidth'),
            ('height', 'figheight'),
            ('align', 'align')
            ]

    def visit_image(self, node):
        p = node.parent
        if isinstance(p, nodes.figure):
            directive = 'figure'
            p = p.parent
        else:
            directive = 'image'
        if not isinstance(p, nodes.list_item):
            self.tstack += self.vindent()
        self.tstack += Writer.get_indent(p)
        self.tstack += ".. " + directive + ':: ' \
                + node['uri'] + '\n'

        indent = Writer.get_indent(node)

        l = []
        l.append( (node, RstCollectVisitor.image_attr_map) )
        if isinstance(node.parent, nodes.figure):
            l.append( (node.parent, RstCollectVisitor.figure_attr_map) )

        for n, attr_map in l:
            for (k,v) in attr_map:
                if k in n:
                    val = n[k]
                    if isinstance(val,list) and len(val) == 0:
                        continue
                    self.tstack += indent + ':' + v + ':'
                    if isinstance(val,list) and len(val) > 0:
                        self.tstack += ' ' + ' '.join(val)
                    elif str(val):
                        self.tstack += ' ' + str(val)
                    self.tstack += '\n'

    def visit_legend(self, node):
        p = node.parent
        assert isinstance(p, nodes.figure)

        # Check for missing cpation.
        if p.index(node) == 1:
            # We need to add an empty caption (i.e. an empty comment)
            self.tstack += self.vindent()  + Writer.get_indent(node) + '..\n'

    def visit_caption(self, node):
        self.visit_paragraph(node)

    def depart_caption(self, node):
        self.depart_paragraph(node)

    def visit_label(self, node):
        p = node.parent
        if isinstance(p, nodes.footnote) or isinstance(p, nodes.citation):
            # `label` used with footnotes and cittions is presently ignored
            # (we take the ft. label from its `names` attribute)
            raise nodes.SkipChildren()
        else:
            pass

    def depart_footnote(self, node):
        if len(node.children) == 1:
            # There is no body of the footnote, so we need to add
            # newline.
            self.tstack += '\n'

    def visit_footnote(self, node):
        if 'auto' in node and (node['auto']==1 or node['auto']=='*'):
            if node['auto']==1: ft = '#'
            else:               ft = '*'
        else:
            assert 'names' in node and len(node['names']) > 0
            ft = node['names'][0]

        p = node.parent
        pidx = p.index(node)
        if not isinstance(p, nodes.list_item) and \
                not (pidx > 0 and isinstance(p[pidx-1], nodes.footnote)):
            self.tstack += self.vindent()
        self.tstack += Writer.get_indent(node.parent)
        self.tstack += '.. [' + ft + ']'

    def depart_citation(self, node):
        if len(node.children) == 1:
            # There is no body of the citation, so we need to add
            # newline.
            self.tstack += '\n'

    def visit_citation(self, node):
        assert 'names' in node and len(node['names']) > 0
        label = node['names'][0]

        p = node.parent
        pidx = p.index(node)
        if not isinstance(p, nodes.list_item) and \
                not (pidx > 0 and isinstance(p[pidx-1], nodes.citation)):
            self.tstack += self.vindent()
        self.tstack += Writer.get_indent(node.parent)
        self.tstack += '.. [' + label + ']'

    math_block_attr_map = [
            ('names', 'name'),
            ('classes', 'class'),
            ]

    def visit_math_block(self, node):
        assert len(node.children) == 1
        p = node.parent
        ni = p.index(node)
        indent = Writer.get_indent(p)

        attr_str = ''
        for (k,v) in RstCollectVisitor.math_block_attr_map:
            if k in node:
                val = node[k]
                if isinstance(val,list) and len(val) == 0:
                    continue
                attr_str += indent + '   :' + v + ':'
                if isinstance(val,list) and len(val) > 0:
                    attr_str += ' ' + ' '.join(val)
                elif str(val):
                    attr_str += ' ' + str(val)
                attr_str += '\n'

        self.tstack += self.vindent()
        if ni==0 or not isinstance(p[ni-1], nodes.math_block) or attr_str:
            self.tstack += indent + '.. math::'
            if attr_str:
                self.tstack += '\n' + attr_str
            if node[0].astext():
                if attr_str:
                    self.tstack += '\n' + indent + '   '
                else:
                    self.tstack += ' '
        else:
            self.tstack += indent + '   '

    def depart_math_block(self, node): self.tstack += '\n'
