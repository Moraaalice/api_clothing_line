from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    store_name = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)
    phone_number = PhoneNumberField(null = False, blank = False, unique = True)