from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
