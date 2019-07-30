from django.contrib import admin
from django.db import models

# Create your models here.

class DjangoBoard(models.Model):
    title = models.CharField(max_length =50, blank=True)
    body = models.CharField(max_length=1000, blank=True)
    license = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/',  null=True)


    
    def __str__(self):
        return self.title

