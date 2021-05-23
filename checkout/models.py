from django.db import models
from django.contrib.auth.models import User
from earrings.models import Earring

# Create your models here.
class Purchase(models.Model):
    earring_id = models.ForeignKey(Earring, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase made for item#{self.earring_id} by user#{self.user_id} on {self.purchase_date}"