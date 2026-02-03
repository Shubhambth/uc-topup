# models.py
from django.db import models
from cloudinary.models import CloudinaryField

class PaymentQR(models.Model):
    name = models.CharField(max_length=100)
    qr_image = CloudinaryField("image")

    def __str__(self):
        return self.name
