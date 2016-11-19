import unittest

import django.test.runner


class TestTVRunner(django.test.runner.DiscoverRunner):

    def __init__(self, *args, **kwargs):
        self.test_runner = TestTVTestRunner
        self.test_suite = TestTVTestSuite
        self.server = None

    def setup_test_environment(self, **kwargs):
        self.start_app_server()
        super().setup_test_environment(**kwargs)

    def start_app_server(self):
        server = magic()
        self.server = server

    def teardown_test_environment(self, **kwargs):
        self.server.stop()


class TestTVTestRunner(unittest.TextTestRunner):

    pass


class TestTVTestSuite(unittest.TestSuite):

    pass
