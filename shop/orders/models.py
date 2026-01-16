from django.db import models


class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        CARD = "card", "Оплата картой"
        CASH = "cash", "Оплата наличными"

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(
        max_length=10,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CARD,
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.name}"
