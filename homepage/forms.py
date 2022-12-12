from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterUserForm(UserCreationForm):
    CHOICES = [
        ('Customer', 'Customer'),
        ('Admin', 'Admin'),
    ]
    regist_as = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id':'input-type'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "regist_as")
        
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user