from django import forms

class ItemForm(forms.Form):
    CHOICES = [
        ('Soul Comforter', 'Soul Comforter'),
        ('Anxiety Booster', 'Anxiety Booster'),
    ]
    name = forms.CharField(label='', max_length=64, widget=forms.TextInput(attrs={'id':'input-name'}))
    type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id':'input-category'}))
    comfortrate = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-comfortrate'}))
    boostrate = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-boostrate'}))
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-price'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'input-image'}))
