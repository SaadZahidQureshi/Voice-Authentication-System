from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.TextField()
    image = models.ImageField(upload_to ='pics')

class contactus(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.TextField(max_length=1000)
    message = models.TextField(max_length=1000)
    