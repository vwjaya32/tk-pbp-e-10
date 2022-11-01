from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=250)

    def __str__(self):
        return self.title

