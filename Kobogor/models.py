import django
from django.db import models


class ContactUs(models.Model):
    name = models.CharField(default='', max_length=100)
    phone = models.IntegerField(default='')
    email = models.CharField(default='', max_length=100)
    message = models.CharField(default='', max_length=255)
