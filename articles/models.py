# Create your models here.
from operator import length_hint
from django.db import models
# from django.contrib.auth.models import User

class Articles(models.Model):
    author = models.CharField(max_length = 150)
    title = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length = 150)
    artc_place = models.ForeignKey(Articles,blank=True,on_delete=models.CASCADE, related_name="responses")
    content = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.content)