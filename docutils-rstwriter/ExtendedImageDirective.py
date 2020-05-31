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

from docutils.parsers.rst.directives.images import Image

class ExtendedImageDirective(Image):

    def run(self):
        # This adds the `source` pointing to the path of the source RST file
        self.options['source'] = self.state_machine.input_lines.source(self.lineno - self.state_machine.input_offset - 1)

        # now call the default directive processing (of the super class)
        return super(ExtendedImageDirective,self).run()

