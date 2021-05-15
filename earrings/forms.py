from django import forms
from .models import Earring


class EarringForm(forms.ModelForm):
    class Meta:
        model = Earring
        fields = ('name', 'description', 'price', 'stock', 'collection', 'tags', 'image')