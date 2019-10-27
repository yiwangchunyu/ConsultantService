import json

from django.db import models

# Create your models here.
from django.utils import timezone


class Diary(models.Model):
    user_id = models.CharField(max_length=200)
    label = models.IntegerField()
    #[0:”angry”,1:”sad”,2:”exhausted”,3:”anxious”,4:” neutral”,5:”happy”,6:”exciting”,7:”surprise”,8:”peace”]
    title = models.TextField(default='',blank=True)
    content = models.TextField(default='',blank=True)
    weather = models.CharField(max_length=200, default='', blank=True)
    loc = models.CharField(max_length=200, default='', blank=True)
    adv = models.CharField(max_length=200, default='', blank=True)
    images = models.TextField(default=json.dumps([]), blank=True)
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now = True)