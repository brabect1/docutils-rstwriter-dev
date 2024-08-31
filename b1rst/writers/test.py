import docutils.parsers
import docutils.readers
import docutils.writers
import docutils.frontend
import docutils.io
import b1rst.writers.YamlWriter

inputstr = """\
A paragraph :: some text

A paragraph::
some text

A paragraph\\::
"""

# instantiate a parser
comp_class = docutils.parsers.get_parser_class('restructuredtext')
parser = comp_class()

# instantiate a reader
comp_class = docutils.readers.get_reader_class('standalone')
reader = comp_class()

# instantiate a writer
writer_class = b1rst.writers.YamlWriter.YamlWriter
writer = writer_class()

# initialize document settings
settings_overrides = {}
defaults = (settings_overrides or {}).copy()
defaults.setdefault('traceback', True)
option_parser = docutils.frontend.OptionParser(
        components=(parser, reader, writer,),
        defaults=defaults,
        read_config_files=True,
        usage=None,
        description=None)
settings = option_parser.get_default_values()

# initialize data input and output
source = docutils.io.StringInput(
        source=inputstr, source_path=settings._source,
        encoding=settings.input_encoding)
destination = docutils.io.StringOutput(
    destination=None, destination_path=settings._destination,
    encoding=settings.output_encoding,
    error_handler=settings.output_encoding_error_handler)

# create the document
document = reader.read(source, parser, settings)

# write output
output = writer.write(document, destination)
writer.assemble_parts()

if isinstance(output, bytes):
    output = output.decode()
print(output)
