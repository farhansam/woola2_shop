from django.contrib import admin

# Register your models here.
from .models import Earring, Collection, Tag

admin.site.register(Earring)
admin.site.register(Collection)
admin.site.register(Tag)