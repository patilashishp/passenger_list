from django.db import models

# Create your models here.
class passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    boarding = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)