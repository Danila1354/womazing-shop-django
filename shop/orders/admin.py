from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "payment_method", "comment")

    fieldsets = (
        ("Данные покупателя", {
            "fields": ("name", "email", "phone")
        }),
        ("Адрес доставки", {
            "fields": ("country", "city", "street", "house", "apartment")
        }),
        ("Оплата и комментарий", {
            "fields": ("payment_method", "comment")
        }),
        ("Служебная информация", {
            "fields": ("created_at",)
        }),
    )
    list_display = ("id", "name", "email", "phone", "city")
    search_fields = ("name", "email", "phone", "city")
    list_filter = ("payment_method",)