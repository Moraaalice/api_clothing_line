from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


# These are my customer models

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    phone_number = PhoneNumberField(null = False, blank=False, unique=True)


def __str__(self):
    return self.name    
