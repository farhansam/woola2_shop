from django import forms
from .models import Earring, Collection
from pyuploadcare.dj.forms import ImageField


class EarringForm(forms.ModelForm):
    image = ImageField(label='Image', required=False)
    class Meta:
        model = Earring
        fields = ('name', 'description', 'price', 'stock', 'collection', 'tags', 'creator', 'image')


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), required=False)