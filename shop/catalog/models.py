from django.db import models
from colorfield.fields import ColorField
# Create your models here.


class Color(models.Model):
    name = models.CharField("Название цвета", max_length=50)
    value = ColorField("Цвет", default="#000000")

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='product_variants')
    size = models.CharField("Размер", max_length=50)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Вариант товара"
        verbose_name_plural = "Варианты товара"

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size}"