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

import unittest
import docutils
import docutils.core
import docutils.nodes
import docutils.utils

# Work around due to improper module naming: https://stackoverflow.com/questions/7583652/python-module-with-a-dash-or-hyphen-in-its-name
docutils_rstwriter = __import__("docutils-rstwriter")

class custom_node(docutils.nodes.General, docutils.nodes.TextElement): pass

class CustomNodeHandler(docutils_rstwriter.writer.ExternalHandler):

    def handle_visit(self, visitor, node):
        if isinstance(node,custom_node):
            visitor.visit_paragraph(node);
            return True;
        return False;

    def handle_depart(self, visitor, node):
        if isinstance(node,custom_node):
            visitor.depart_paragraph(node);
            return True;
        return False;

class TestExternHandlers(unittest.TestCase):

    def test_visitor_init(self):
        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        self.assertTrue(visitor_class is not None);

        visitor = visitor_class(None,None);
        self.assertTrue(visitor is not None);

        self.assertEqual(len(visitor.extern_handlers),0);

    def test_add_handler(self):
        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(None,None);

        h1 = docutils_rstwriter.writer.ExternalHandler();
        visitor.add_extern_handler(h1);
        self.assertEqual(len(visitor.extern_handlers),1);

        # see that cannot add the same handler twice
        visitor.add_extern_handler(h1);
        self.assertEqual(len(visitor.extern_handlers),1);

        h2 = docutils_rstwriter.writer.ExternalHandler();
        visitor.add_extern_handler(h2);
        self.assertEqual(len(visitor.extern_handlers),2);

    def test_remove_handler(self):
        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(None,None);

        h1 = docutils_rstwriter.writer.ExternalHandler();
        visitor.add_extern_handler(h1);

        h2 = docutils_rstwriter.writer.ExternalHandler();
        visitor.add_extern_handler(h2);

        self.assertEqual(len(visitor.extern_handlers),2);

        h3 = docutils_rstwriter.writer.ExternalHandler();
        visitor.remove_extern_handler(h3);
        self.assertEqual(len(visitor.extern_handlers),2);

        visitor.remove_extern_handler(h2);
        self.assertEqual(len(visitor.extern_handlers),1);

        visitor.remove_extern_handler(h2);
        self.assertEqual(len(visitor.extern_handlers),1);

        visitor.remove_extern_handler(h1);
        self.assertEqual(len(visitor.extern_handlers),0);

    def test_walk_all_known(self):
        document = docutils.utils.new_document('', None);
        document += docutils.nodes.title(text='My title');
        document += docutils.nodes.paragraph(text='1st paragraph');
        document += docutils.nodes.paragraph(text='2nd paragraph');

        expected = '''My title
================

1st paragraph

2nd paragraph
'''

        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(document,None);

        document.walkabout(visitor);
        self.assertEqual(visitor.text, expected);

    def test_except_on_unknown(self):
        document = docutils.utils.new_document('', None);
        document += docutils.nodes.title(text='My title');
        document += custom_node(text='1st paragraph');
        document += docutils.nodes.paragraph(text='2nd paragraph');

        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(document,None);

        with self.assertRaises(NotImplementedError):
            document.walkabout(visitor);

    def test_except_on_unhandled(self):
        document = docutils.utils.new_document('', None);
        document += docutils.nodes.title(text='My title');
        document += custom_node(text='1st paragraph');
        document += docutils.nodes.paragraph(text='2nd paragraph');

        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(document,None);

        h1 = docutils_rstwriter.writer.ExternalHandler();
        visitor.add_extern_handler(h1);

        with self.assertRaises(NotImplementedError):
            document.walkabout(visitor);

    def test_except_on_handled(self):
        document = docutils.utils.new_document('', None);
        document += docutils.nodes.title(text='My title');
        document += custom_node(text='1st paragraph');
        document += docutils.nodes.paragraph(text='2nd paragraph');

        visitor_class = docutils_rstwriter.writer.RstCollectVisitor;
        visitor = visitor_class(document,None);

        h1 = CustomNodeHandler();
        visitor.add_extern_handler(h1);

        document.walkabout(visitor);

        expected = '''My title
================

1st paragraph

2nd paragraph
'''
        self.assertEqual(visitor.text, expected);



if __name__ == '__main__':
    unittest.main()
