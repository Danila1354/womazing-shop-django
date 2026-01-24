from django.contrib import admin
from django.utils.html import format_html

from .models import Color, Product, ProductVariant, Category, Size


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "value")


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1
    readonly_fields = ("image_preview",)
    fields = (
        "image_preview",
        "image",
        "color",
        "size",
        "price",
        "price_with_discount",
        "is_new_collection",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name", "category__name")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductVariantInline]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    