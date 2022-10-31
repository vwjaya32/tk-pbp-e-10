from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class MentalTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateTimeField()