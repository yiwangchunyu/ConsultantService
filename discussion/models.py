import json

from django.db import models

# Create your models here.
from django.utils import timezone


class Discussion(models.Model):
    user_id = models.IntegerField()
    # type = models.CharField(max_length=255,default='')
    # category = models.CharField(max_length=255, default='')
    # title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    images = models.TextField(default=json.dumps([]),blank=True)
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now = True)