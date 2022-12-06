from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    title = models.CharField(max_length=180)
    price = models.IntegerField(default=1)
    colour = models.CharField(max_length=20)
    characteristics = models.TextField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.author.username }_{self.title}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    rating = (
        ('1/5', '1/5'),
        ('2/5', '2/5'),
        ('3/5', '3/5'),
        ('4/5', '4/5'),
        ('5/5', '5/5')
    )

    rate = models.CharField(default=5, choices=rating, max_length=10)

    def __str__(self):
        return f'{self.author.username}_{self.product}'
