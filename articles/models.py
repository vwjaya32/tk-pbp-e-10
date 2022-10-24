# Create your models here.
from operator import length_hint
from django.db import models
# from django.contrib.auth.models import User

class Articles(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length = 150)
    title = models.CharField(max_length = 150)
    content = models.TextField()