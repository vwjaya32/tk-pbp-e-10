from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'description')
        labels = {
            'name':'Event Name',
            'date':'Date and Time',
            'description':'Description',
        }
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
        }