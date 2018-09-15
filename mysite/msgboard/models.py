from django.db import models

# Create your models here.

class Msg(models.Model):
    username=models.CharField(max_length=32)
    time=models.DateTimeField()
    msg=models.TextField(max_length=65535)
