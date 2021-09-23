from django.db import models
from products.models import Products
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Products , blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    