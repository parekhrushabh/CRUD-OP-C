from django.db import models

# Create your models here.

class carbooking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)