from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)

    def __str__(self):
        return self.name