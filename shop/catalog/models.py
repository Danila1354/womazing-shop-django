from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField('Название товара', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    size = models.CharField('Размер', max_length=50)