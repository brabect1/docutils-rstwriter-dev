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


import b1rst.parsers.html.Bs4HtmlParser
import bs4
import docutils.utils

parser = b1rst.parsers.html.Bs4HtmlParser.Bs4HtmlParser()
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
html = """And don't forget to <a href="https://www.w3schools.com">Visit W3Schools.com!</a>"""
document = parser.parseHtml(html)
print(document.pformat())
print(20*'=')
document = docutils.utils.new_document('', None)
parser.parse(html, document)
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
