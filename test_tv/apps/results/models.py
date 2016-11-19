from django.db import models


class Test(models.Model):

    name = models.CharField(max_length=512, db_index=True)


class TestResult(models.Model):

    test = models.ForeignKey(Test, related_name="results")
    status = models.CharField(max_length=24, db_index=True)

    @classmethod
    def get_num_failures(cls):
        return cls.objects.filter(status="failure").count()
