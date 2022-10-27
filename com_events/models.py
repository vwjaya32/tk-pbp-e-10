from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)

class Event(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateTimeField()
    manager = models.CharField(max_length = 100)
    description = models.TextField()
    attendees = models.ManyToManyField(User, blank = True)