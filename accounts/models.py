from django.db import models

# Create your models here.

class Profile(models.Model):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'users/')