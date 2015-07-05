from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
