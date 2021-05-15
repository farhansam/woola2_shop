from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Collection(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name

class Earring(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.name


