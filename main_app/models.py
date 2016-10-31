from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Twister(models.Model):
    content = models.CharField(max_length=999)
    content_id = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.content

class Test(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
