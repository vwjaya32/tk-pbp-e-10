from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    manager = models.CharField(max_length = 100)
    description = models.TextField()
    attendees = models.ManyToManyField(User, blank = True)