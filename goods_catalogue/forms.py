from django import forms
from goods_catalogue import models

class ItemForm(forms.ModelForm) :
    class Meta:
        model = models.Purchase
        fields = ['metode_pembayaran', 'metode_pengiriman']