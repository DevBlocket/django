from django.db import models

from fix_request.models.status import Status
from tag.models import Tag


class FixRequest(models.Model):

    user_id = models.IntegerField()
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    date_created = models.DateTimeField(auto_now_add=True)

