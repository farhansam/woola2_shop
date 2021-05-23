from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    price = models.DecimalField(validators=[MinValueValidator(0.01),MaxValueValidator(100000)], 
                                max_digits=10, decimal_places=2, blank=False)
    stock = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100000)], 
                                blank=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.name


