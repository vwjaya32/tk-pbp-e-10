from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MentalTest(models.Model):
#     CHOICE1 = [
#     (
#             ('1', 'Yes, I do have some besties'),
#             ('2', 'I feel lonely sometimes'),
#             ('3', "I don't have any friends"),
#     ),
#     ]
#     CHOICE2 = [
#     (
#             ('1', 'Yes, I love my family'),
#             ('2', 'We fight every other day'),
#             ('3', "Maybe they don't love me"),
#     ),
#     ]
#     CHOICE3 = [
#     (
#             ('1', 'I feel happy being myself'),
#             ('2', 'Sometimes I feel happy, sometimes not'),
#             ('3', "I can't accept myself"),
#     ),
#     ]
#     CHOICE4 = [
#     (
#             ('1', 'No, I am not using drugs'),
#             ('2', 'I take some pills when in need'),
#             ('3', "They are basically a necessity"),
#     ),
#     ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#     friendship = models.CharField(max_length=200, choices = CHOICE1)
#     family = models.CharField(max_length=200, choices = CHOICE2)
#     acceptance = models.CharField(max_length=200, choices = CHOICE3)
#     drugs = models.CharField(max_length=200, choices = CHOICE4)