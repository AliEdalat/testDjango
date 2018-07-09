from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')