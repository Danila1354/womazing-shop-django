from django.db import models
from colorfield.fields import ColorField
from .utils.upload_paths import product_image_path
from django.utils.text import slugify

# Create your models here.


class Color(models.Model):
    name = models.CharField("Название цвета", max_length=50)
    value = ColorField("Цвет", default="#000000")

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)
    slug = models.SlugField("Слаг категории", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    slug = models.SlugField("Слаг товара", unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants"
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        related_name="product_variants",
        blank=True,
        null=True,
        verbose_name="Цвет",
    )
    image = models.ImageField(
        "Фото товара", upload_to=product_image_path, blank=True, null=True
    )
    size = models.CharField("Размер", max_length=20, blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    price_with_discount = models.DecimalField(
        "Цена со скидкой", max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        verbose_name = "Вариант товара"
        verbose_name_plural = "Варианты товара"

    def __str__(self):
        return f"{self.product.name} - {self.color.name if self.color else 'Цвет не указан'} - {self.size if self.size else 'Размер не указан'}"
