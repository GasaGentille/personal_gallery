from django.db import models

# Create your models here.


class Location(models.Model):
    location= models.CharField(max_length =30)

class Category(models.Model):
    category = models.CharField(max_length =30)

class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    location =  models.ForeignKey(Location)
    category = models.ForeignKey(Category)

