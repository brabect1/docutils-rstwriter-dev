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


import docutils.parsers
import docutils.nodes
import docutils.utils
import yaml
import sys

class YamlParser(docutils.parsers.Parser):
    """Represents a base class of a YAML parser producing a docutils document tree."""

    supported = ('yaml')

    settings_spec = (
        'YAML Parser Options',
        None,
        ())

    def getDefaultOptions(self):
        """Gets parser's default options.

        Return
            String indexed dictionary of default options.
        """
        return {}


    def __init__(self, opts=None):
        self.opts = opts or self.getDefaultOptions()


    def parse(self, inputstring, document):
        if document is None or not isinstance(document, docutils.nodes.document):
            raise ValueError('Invalid document type!')

        ydoc = yaml.safe_load(inputstring)

        if 'document' not in ydoc:
            #TODO add system message under `document`
            pass
        else:
            attrs = ydoc['document'].get('attrs', {})
            for aname, aval in attrs.items():
                document.replace_attr(aname, aval)

            childs = ydoc['document'].get('children', None)
            for node in self.createNodes(childs):
                document += node


    def createNodes(self, elist):
        """Creates a list of document tree nodes from the list of dictionaries
           representing document sub-trees.
        """

        nodes = []
        if elist is None:
            #TODO add system message to `nodes`
            return nodes

        for elem in elist:
            if isinstance(elem, str):
                nodes.append(docutils.nodes.Text(elem))
            elif isinstance(elem, dict):
                assert len(elem.keys()) == 1 # TODO refactor to sanity check
                for classname, nodedict in elem.items():
                    nodeclass = getattr(sys.modules['docutils.nodes'], classname)
                    childs = nodedict.get('children', None)
                    subnodes = self.createNodes(childs)
                    if len(subnodes) != len([n for n in subnodes if isinstance(n, docutils.nodes.Node)]):
                        for i in range(0, len(subnodes)):
                            if not isinstance(subnodes[i], docutils.nodes.Node):
                                raise TypeError(f"{i}-th element wrong type: {subnodes[i].__class__.__name__}")
                    node = nodeclass('', *subnodes)
                    attrs = nodedict.get('attrs', {})
                    for aname, aval in attrs.items():
                        node.replace_attr(aname, aval)
                    nodes.append(node)

        return nodes
