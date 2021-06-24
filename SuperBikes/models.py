from django.db import models

# Create your models here.

class Newcar(models.Model):
    name = models.CharField(max_length=50)
    link_address = models.CharField(max_length=100)

from django.utils.timezone import now
class Recommended(models.Model):
    img = models.ImageField(blank=True)
    img_address = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=now)
    ammount = models.IntegerField(default=0)

# for supercars
class Supercars(models.Model):
    img = models.ImageField(blank=True)
    img_address = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=now)

# for carbrands
class Carbrands(models.Model):
    img = models.ImageField(blank=True)
    brand_name = models.CharField(max_length=100)