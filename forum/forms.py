from django import forms
from django.forms import ModelForm
from .models import Posts, Replies

class post_box(ModelForm):
    class Meta:
        model = Posts
        fields = ('author','title','content')
        labels = {
        'author':'Who are you?',
        'title':'What is the subject?',
        'content':'Tell me your story!',
        }
        widget = {
            'author': forms.TextInput(attrs={'class':'form-control', 'id':'author'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'id':'title'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'id':'content'})
        }

class reply_box(ModelForm):
    class Meta:
        model = Replies
        fields = ('author','content')
        labels = {
        'author':'author',
        'content':'content',
        }
        widget = {
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'tes'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'tes'})
        }