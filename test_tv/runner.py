import os
import sys
import unittest

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from django.test.utils import captured_stdout, captured_stderr
from django.utils import six

from .apps.results.models import Test, TestResult

SUCCESS = "clemente"
FAILURE = "tebow"
ERROR = "bojackson"


class ThisShouldNeverHappenError(Exception):
    pass


class TestTVTestResult(unittest.TestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TextTestTVRunner(unittest.TextTestRunner):
    """Saves results as Tests and TestResults.

    For each test run, captures test, STDOUT, STDERR, result (success,
    failure, or error).

    """
    def _makeResult(self):
        import ipdb; ipdb.set_trace()
        self.result = TestTVTestResult()

        return self.result


        # # if self.result.wasSuccessful():
        # #     self.result.status = SUCCESS
        # # elif len(self.result.failures):
        # #     self.result.status = FAILURE
        # # elif len(self.result.errors):
        # #     self.result.status = ERROR
        # # else:
        # #     raise ThisShouldNeverHappenError

        # return self.result

    def run(self, test):
        """Run a test or a test suite.

        """
        import ipdb; ipdb.set_trace()
        result = super().run(test)

    def _run_test(self, test):
        """Run one test.

        """
        with captured_stdout() as stdout, captured_stderr() as stderr:
            super().run(test)
            persistent_test, created = Test.objects.get_or_create(
                name=str(test))
            test_result = TestResult.objects.create(test=persistent_test,
                                                    stdout=stdout,
                                                    stderr=stderr)
            if self.result.wasSuccessful():
                test_result.succeed()
            elif len(self.result.failures):
                test_result.fail()
            elif len(self.result.errors):
                test_result.error()
            else:
                raise ThisShouldNeverHappenError


class TestTVTestSuite(unittest.suite.TestSuite):

    pass


class TestTVRunner(DiscoverRunner):

    test_runner = TextTestTVRunner
    # test_suite = TestTVTestSuite

    def setup_test_environment(self, **kwargs):
        super().setup_test_environment(**kwargs)
        # start runserver against (production) database
        self.start_live_server()
        # Re: the "production part":  _create_server_thread()

    def teardown_test_environment(self, **kwargs):
        LiveServerTestCase.tearDownClass()  # Stops server.
        super().teardown_test_environment(**kwargs)

    def start_live_server(self):
        """Copied shamelessly from unittest.testcases.LiveServerTestCase.

        Copied in so I can override db connection settings.
        """
        # Launch the live server's thread
        specified_address = os.environ.get(
            'DJANGO_LIVE_TEST_SERVER_ADDRESS', 'localhost:8081-8179')

        # The specified ports may be of the form '8000-8010,8080,9200-9300'
        # i.e. a comma-separated list of ports or ranges of ports, so we break
        # it down into a detailed list of all possible ports.
        possible_ports = []
        try:
            host, port_ranges = specified_address.split(':')
            for port_range in port_ranges.split(','):
                # A port range can be of either form: '8000' or '8000-8010'.
                extremes = list(map(int, port_range.split('-')))
                assert len(extremes) in [1, 2]
                if len(extremes) == 1:
                    # Port range of the form '8000'
                    possible_ports.append(extremes[0])
                else:
                    # Port range of the form '8000-8010'
                    for port in range(extremes[0], extremes[1] + 1):
                        possible_ports.append(port)
        except Exception:
            msg = 'Invalid address ("%s") for live server.' % specified_address
            six.reraise(ImproperlyConfigured, ImproperlyConfigured(msg),
                        sys.exc_info()[2])

        import ipdb; ipdb.set_trace()

        production_connections = settings.DATABASES
        LiveServerTestCase.server_thread = (
            LiveServerTestCase._create_server_thread(host, possible_ports,
                                                     production_connections))
        LiveServerTestCase.server_thread.daemon = True
        LiveServerTestCase.server_thread.start()

        # Wait for the live server to be ready
        LiveServerTestCase.server_thread.is_ready.wait()
        if LiveServerTestCase.server_thread.error:
            # Clean up behind ourselves, since tearDownClass won't get
            # called in case of errors.
            LiveServerTestCase._tearDownClassInternal()
            raise LiveServerTestCase.server_thread.error
