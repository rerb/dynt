from django.db import IntegrityError
import django.test

from .models import Test, TestResult


class TestTestCase(django.test.TestCase):

    def test_name_is_unique(self):
        """Is Test.name unique?
        """
        Test.objects.create(name="Bob")
        self.assertRaises(IntegrityError,
                          Test.objects.create,
                          name="Bob")


class TestCaseTestCase(django.test.TestCase):

    def setUp(self):
        # 10 TestResults to play with.
        self.test_results = [TestResult.objects.create(
            test=Test.objects.create(name="Test{}".format(str(i))))
                           for i in range(10)]

    def test_fail_and_get_num_failures(self):
        """Do fail() and get_num_failures() work?
        """
        for i in range(5):
            self.test_results[i].fail()
            self.test_results[i].save()
        self.assertEqual(5, TestResult.get_num_failures())

    def test_error_and_get_num_errors(self):
        """Do error() and get_num_errors() work?
        """
        for i in range(5):
            self.test_results[i].error()
            self.test_results[i].save()
        self.assertEqual(5, TestResult.get_num_errors())

    def test_succeed_and_get_num_successes(self):
        """Do succeed() and get_num_successes() work?
        """
        for i in range(5):
            self.test_results[i].succeed()
            self.test_results[i].save()
        self.assertEqual(5, TestResult.get_num_successes())
