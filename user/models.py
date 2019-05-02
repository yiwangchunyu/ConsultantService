from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=20,default='')
    gender = models.IntegerField(default=1)
    password = models.CharField(max_length=100)
    avatar = models.CharField(max_length=200,default='http://consultant.yiwangchunyu.wang/media/system/avatar.jpg')
    status = models.IntegerField(default=1)
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now=True)