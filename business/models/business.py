from django.db import models

from tag.models import Tag


class Business(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    tags = models.ManyToManyField(Tag, related_name='businesses')

    # 주소
    road_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
