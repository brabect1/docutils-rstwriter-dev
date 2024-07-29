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


import docutils.nodes
import docutils.writers
import yaml

class YamlWriter(docutils.writers.Writer):
    """Writes document tree in the YAML format."""

    supported = ('yaml', 'pseudoyaml')
    """Formats this writer supports."""

    config_section = 'pseudoxml writer'
    config_section_dependencies = ('writers',)

    output = None
    """Final translated form of `document`."""

    def translate(self):
        self.output = yaml.dump(self.node2dict(self.document), default_flow_style=False)

    def supports(self, format):
        """This writer supports all format-specific elements."""
        return True

    def node2dict(self, node):
        """Turns a document sub-tree rooted by `node` into a dictionary."""

        if node is None: return {}

        if isinstance(node, docutils.nodes.Text):
            return node.astext()

        attrs = {}
        if hasattr(node, 'attlist'):
            for name, value in node.attlist():
                if value is None:           # boolean attribute
                    attrs[name] = True
                elif isinstance(value, list):
                    attrs[name] = [str(v) for v in value]
                else:
                    attrs[name] = str(value)

        d = {}
        if attrs: d['attrs'] = attrs;
        d['children'] = [self.node2dict(c) for c in node.children]
        return {node.tagname: d}


