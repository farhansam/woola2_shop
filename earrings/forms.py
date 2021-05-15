from django import forms
from .models import Earring, Collection


class EarringForm(forms.ModelForm):
    class Meta:
        model = Earring
        fields = ('name', 'description', 'price', 'stock', 'collection', 'tags', 'creator', 'image')


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), required=False)