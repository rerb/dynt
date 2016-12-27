from django.db import models


class Test(models.Model):

    name = models.CharField(max_length=512, db_index=True, unique=True)


class TestResult(models.Model):

    FAILURE = "failure"
    ERROR = "error"
    SUCCESS = "success"

    test = models.ForeignKey(Test, related_name="results")
    status = models.CharField(max_length=24, db_index=True,
                              null=True, blank=True)
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)

    @classmethod
    def get_num_failures(cls):
        return cls.objects.filter(status=cls.FAILURE).count()

    @classmethod
    def get_num_errors(cls):
        return cls.objects.filter(status=cls.ERROR).count()

    @classmethod
    def get_num_successes(cls):
        return cls.objects.filter(status=cls.SUCCESS).count()

    @classmethod
    def get_num_left(cls):
        return cls.objects.filter(status="").count()

    def fail(self):
        self.status = self.FAILURE

    def error(self):
        self.status = self.ERROR

    def succeed(self):
        self.status = self.SUCCESS

    def is_failure(self):
        return self.status == self.FAILURE

    def is_error(self):
        return self.status == self.ERROR

    def is_success(self):
        return self.status == self.SUCCESS
