from django.contrib import admin

# Register your models here.
from .models import Product, Collection, Tag

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Tag)