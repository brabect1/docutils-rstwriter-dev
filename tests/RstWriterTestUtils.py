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


# Base classes copied and modified from docutils/test/DocutilsTestSupport.py, r8373 (2019-08-27)

from __future__ import print_function

import sys
import os
import inspect
import unittest
import docutils
from docutils import frontend, nodes, statemachine, utils
from docutils.parsers.rst import roles
import difflib
import re

def _format_str(*args):
    r"""
    Return a tuple containing representations of all args.

    Same as map(repr, args) except that it returns multi-line
    representations for strings containing newlines, e.g.::

        '''\
        foo  \n\
        bar

        baz'''

    instead of::

        'foo  \nbar\n\nbaz'

    This is a helper function for CustomTestCase.
    """
    return_tuple = []
    for i in args:
        r = repr(i)
        if ( (isinstance(i, bytes) or isinstance(i, unicode))
             and '\n' in i):
            stripped = ''
            if isinstance(i, unicode) and r.startswith('u'):
                stripped = r[0]
                r = r[1:]
            elif isinstance(i, bytes) and r.startswith('b'):
                stripped = r[0]
                r = r[1:]
            # quote_char = "'" or '"'
            quote_char = r[0]
            assert quote_char in ("'", '"'), quote_char
            assert r[0] == r[-1]
            r = r[1:-1]
            r = (stripped + 3 * quote_char + '\\\n' +
                 re.sub(r'(?<!\\)((\\\\)*)\\n', r'\1\n', r) +
                 3 * quote_char)
            r = re.sub(r' \n', r' \\n\\\n', r)
        return_tuple.append(r)
    return tuple(return_tuple)


class StandardTestCase(unittest.TestCase):

    """
    Helper class, providing the same interface as unittest.TestCase,
    but with useful setUp and comparison methods.
    """

    def setUp(self):
        #TODO os.chdir(testroot)
        pass

    def assertEqual(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        if not first == second:
            raise self.failureException(
                msg or '%s != %s' % _format_str(first, second))

    def assertNotEqual(self, first, second, msg=None):
        """Fail if the two objects are equal as determined by the '=='
           operator.
        """
        if first == second:
            raise self.failureException(
                msg or '%s == %s' % _format_str(first, second))

    # aliases for assertion methods, deprecated since Python 2.7

    #TODO failUnlessEqual = assertEquals = assertEqual

    #TODO assertNotEquals = failIfEqual = assertNotEqual


class CustomTestCase(StandardTestCase):

    """
    Helper class, providing extended functionality over unittest.TestCase.

    The methods assertEqual and assertNotEqual have been overwritten
    to provide better support for multi-line strings.  Furthermore,
    see the compare_output method and the parameter list of __init__.
    """

    compare = difflib.Differ().compare
    """Comparison method shared by all subclasses."""

    def __init__(self, method_name, input, expected, id,
                 run_in_debugger=True, suite_settings=None):
        """
        Initialise the CustomTestCase.

        Arguments:

        method_name -- name of test method to run.
        input -- input to the parser.
        expected -- expected output from the parser.
        id -- unique test identifier, used by the test framework.
        run_in_debugger -- if true, run this test under the pdb debugger.
        suite_settings -- settings overrides for this test suite.
        """
        self.id = id
        self.input = input
        self.expected = expected
        self.run_in_debugger = run_in_debugger
        self.suite_settings = suite_settings.copy() or {}

        # Ring your mother.
        unittest.TestCase.__init__(self, method_name)

    def __str__(self):
        """
        Return string conversion. Overridden to give test id, in addition to
        method name.
        """
        return '%s; %s' % (self.id, unittest.TestCase.__str__(self))

    def __repr__(self):
        return "<%s %s>" % (self.id, unittest.TestCase.__repr__(self))

    def clear_roles(self):
        # Language-specific roles and roles added by the
        # "default-role" and "role" directives are currently stored
        # globally in the roles._roles dictionary.  This workaround
        # empties that dictionary.
        roles._roles = {}

    def setUp(self):
        StandardTestCase.setUp(self)
        self.clear_roles()

    def compare_output(self, input, output, expected):
        """`input`, `output`, and `expected` should all be strings."""
        if isinstance(input, unicode):
            input = input.encode('raw_unicode_escape')
        if sys.version_info > (3, 0):
            # API difference: Python 3's node.__str__ doesn't escape
            #assert expected is None or isinstance(expected, unicode)
            if isinstance(expected, bytes):
                expected = expected.decode('utf-8')
            if isinstance(output, bytes):
                output = output.decode('utf-8')
        else:
            if not isinstance(expected, unicode):
                expected = expected.decode('utf-8')
            if not isinstance(output, unicode):
                output = output.decode('utf-8')
            expected = expected.encode('raw_unicode_escape')
            output = output.encode('raw_unicode_escape')
        # Normalize line endings:
        if expected:
            expected = '\n'.join(expected.splitlines())
        if output:
            output = '\n'.join(output.splitlines())
        try:
            self.assertEqual(output, expected)
        except AssertionError as error:
            print('\n%s\ninput:' % (self,), file=sys.stderr)
            print(input, file=sys.stderr)
            try:
                comparison = ''.join(self.compare(expected.splitlines(1),
                                                  output.splitlines(1)))
                print('-: expected\n+: output', file=sys.stderr)
                print(comparison, file=sys.stderr)
            except AttributeError:      # expected or output not a string
                # alternative output for non-strings:
                print('expected: %r' % expected, file=sys.stderr)
                print('output:   %r' % output, file=sys.stderr)
            raise error


class CustomTestSuite(unittest.TestSuite):

    """
    A collection of CustomTestCases.

    Provides test suite ID generation and a method for adding test cases.
    """

    id = ''
    """Identifier for the TestSuite. Prepended to the
    TestCase identifiers to make identification easier."""

    next_test_case_id = 0
    """The next identifier to use for non-identified test cases."""

    def __init__(self, tests=(), id=None, suite_settings=None):
        """
        Initialize the CustomTestSuite.

        Arguments:

        id -- identifier for the suite, prepended to test cases.
        suite_settings -- settings overrides for this test suite.
        """
        unittest.TestSuite.__init__(self, tests)
        self.suite_settings = suite_settings or {}
        if id is None:
            mypath = os.path.abspath(
                sys.modules[CustomTestSuite.__module__].__file__)
            outerframes = inspect.getouterframes(inspect.currentframe())
            for outerframe in outerframes[1:]:
                if outerframe[3] != '__init__':
                    callerpath = outerframe[1]
                    if callerpath is None:
                        # It happens sometimes.  Why is a mystery.
                        callerpath = os.getcwd()
                    callerpath = os.path.abspath(callerpath)
                    break
            mydir, myname = os.path.split(mypath)
            if not mydir:
                mydir = os.curdir
            if callerpath.startswith(mydir):
                self.id = callerpath[len(mydir) + 1:] # caller's module
            else:
                self.id = callerpath
        else:
            self.id = id

    def addTestCase(self, test_case_class, method_name, input, expected,
                    id=None, run_in_debugger=False, **kwargs):
        """
        Create a CustomTestCase in the CustomTestSuite.
        Also return it, just in case.

        Arguments:

        test_case_class -- the CustomTestCase to add
        method_name -- a string; CustomTestCase.method_name is the test
        input -- input to the parser.
        expected -- expected output from the parser.
        id -- unique test identifier, used by the test framework.
        run_in_debugger -- if true, run this test under the pdb debugger.
        """
        if id is None:                  # generate id if required
            id = self.next_test_case_id
            self.next_test_case_id += 1
        # test identifier will become suiteid.testid
        tcid = '%s: %s' % (self.id, id)
        # suite_settings may be passed as a parameter;
        # if not, set from attribute:
        kwargs.setdefault('suite_settings', self.suite_settings)
        # generate and add test case
        tc = test_case_class(method_name, input, expected, tcid,
                             run_in_debugger=run_in_debugger, **kwargs)
        self.addTest(tc)
        return tc

    def generate_no_tests(self, *args, **kwargs):
        pass


class WriterPublishTestCase(CustomTestCase, docutils.SettingsSpec):

    """
    Test case for publish.
    """

    settings_default_overrides = {'_disable_config': True,
                                  'strict_visitor': True,
                                  #TODO 'halt_level': 5,
                                  'report_level': 5}
    writer_name = '' # set in subclasses or constructor

    def __init__(self, *args, **kwargs):
        if 'writer_name' in kwargs:
            self.writer_name = kwargs['writer_name']
            del kwargs['writer_name']
        CustomTestCase.__init__(self, *args, **kwargs)

    def test_publish(self):
        if self.run_in_debugger:
            pdb.set_trace()
        output = docutils.core.publish_string(
              source=self.input,
              reader_name='standalone',
              parser_name='restructuredtext',
              writer_name=self.writer_name,
              settings_spec=self,
              settings_overrides=self.suite_settings)
        self.compare_output(self.input, output, self.expected)


class WriterNoTransformTestCase(WriterPublishTestCase):

    """
    Test case for publish, but using a custom process avoiding
    applying any transforms on the parsed doctree.
    """

    settings_default_overrides = {'_disable_config': True,
                                  'strict_visitor': True,
                                  #TODO 'halt_level': 5,
                                  'report_level': 5}
    writer_name = '' # set in subclasses or constructor

    def __init__(self, *args, **kwargs):
        if 'writer_name' in kwargs:
            self.writer_name = kwargs['writer_name']
            del kwargs['writer_name']
        CustomTestCase.__init__(self, *args, **kwargs)

    def test_publish(self):
        if self.run_in_debugger:
            pdb.set_trace()

        # instantiate a parser
        comp_class = docutils.parsers.get_parser_class('restructuredtext')
        parser = comp_class()

        # instantiate a reader
        comp_class = docutils.readers.get_reader_class('standalone')
        reader = comp_class()

        # instantiate a writer
        writer_class = docutils.writers.get_writer_class(self.writer_name)
        writer = writer_class()

        # initialize document settings
        settings_overrides = self.suite_settings
        defaults = (settings_overrides or {}).copy()
        defaults.setdefault('traceback', True)
        option_parser = docutils.frontend.OptionParser(
                components=(parser, reader, writer, self),
                defaults=defaults,
                read_config_files=True,
                usage=None,
                description=None)
        settings = option_parser.get_default_values()

        # initialize data input and output
        source = docutils.io.StringInput(
                source=self.input, source_path=settings._source,
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
        #output = docutils.core.publish_string(
        #      source=self.input,
        #      reader_name='standalone',
        #      parser_name='restructuredtext',
        #      writer_name=,
        #      settings_spec=self,
        #      settings_overrides=settings_overrides)

        # compare actual and expected output
        self.compare_output(self.input, output, self.expected)


class PublishTestSuite(CustomTestSuite):

    def __init__(self, writer_name, test_class=WriterPublishTestCase, suite_settings=None):
        """
        `writer_name` is the name of the writer to use.
        """
        CustomTestSuite.__init__(self, suite_settings=suite_settings)
        self.test_class = test_class
        self.writer_name = writer_name

    def generateTests(self, dict, dictname='totest'):
        for name, cases in dict.items():
            for casenum in range(len(cases)):
                case = cases[casenum]
                run_in_debugger = False
                if len(case)==3:
                    if case[2]:
                        run_in_debugger = True
                    else:
                        continue
                self.addTestCase(
                      self.test_class, 'test_publish',
                      input=case[0], expected=case[1],
                      id='%s[%r][%s]' % (dictname, name, casenum),
                      run_in_debugger=run_in_debugger,
                      # Passed to constructor of self.test_class:
                      writer_name=self.writer_name)

