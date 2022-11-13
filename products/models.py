from django.db import models

# Create your models here.


class Category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=80)


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=180)
    price = models.IntegerField(default=1)
    colour = models.CharField(max_length=20)
    characteristics = models.TextField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)
