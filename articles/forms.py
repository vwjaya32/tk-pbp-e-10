from django import forms
from django.forms import ModelForm
from .models import Articles, Comments


class edit_box(ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'author', 'content')
        labels = {
            'title':'title',
            'author':'author',
            'content':'content',
        }
        widget = {
            'title': forms.TextInput(attrs={'class':'form-control', 'id':'title'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'id':'author'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'id':'content'})
        }

class comment_box(ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'content')
        labels = {
            'author':'author',
            'content':'content',
        }
        widget = {
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'tes'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'tes'})
        }