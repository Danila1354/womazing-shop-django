from django.contrib import admin

# Register your models here.

from .models import Color, Product, ProductVariant


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "value")

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductVariantInline] 