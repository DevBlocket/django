from django.db import models

from fix_request.models import FixRequest


class Photo(models.Model):

    url = models.URLField()
    fix_request = models.ForeignKey(FixRequest, on_delete=models.CASCADE, related_name='photos')
