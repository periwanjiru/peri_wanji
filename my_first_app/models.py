from __ future __ import unicode_literals

from django.db import models

#create your models here.

class Blog (models.Models):
    Name = models.Charfield(max_length = 20)
    Title = models.CharField(max_length = 20)
    content = models.TextField()
    Timestamp = models.