from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

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
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    stock = models.IntegerField(blank=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.name


