from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model  = Image
        fields = ('title', 'image')
        labels = {
            'title': '',
            'image': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',
                                            'placeholder':'Title'}),
            'image': forms.URLInput(attrs={'class':'form-control',
                                           'id':'imageurl',
                                           'placeholder':'Image URL'}),
        }