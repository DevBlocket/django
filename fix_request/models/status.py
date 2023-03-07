from django.db import models


class Status(models.Model):

    name = models.CharField(max_length=10)
    step = models.IntegerField()
    description = models.CharField(max_length=100)
