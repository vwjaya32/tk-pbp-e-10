from django import forms

class ItemForm(forms.Form):
    CHOICES = [
        ('Soul comforter', 'Soul Comforter'),
        ('Anxiety booster', 'Anxiety Booster'),
    ]
    name = forms.CharField(label='', max_length=64, widget=forms.TextInput(attrs={'id':'input-name'}))
    category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id':'input-type'}))
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-price'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'input-image'}))
