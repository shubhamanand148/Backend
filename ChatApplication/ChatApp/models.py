from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.CharField(max_length=10000)