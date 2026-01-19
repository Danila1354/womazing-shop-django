from django.db import models


class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        CARD = "card", "Оплата картой"
        CASH = "cash", "Оплата наличными"

    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица', max_length=100)
    house = models.CharField('Дом', max_length=20)
    apartment = models.CharField('Квартира', max_length=20, blank=True, null=True)
    payment_method = models.CharField(
        max_length=10,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CARD,
        verbose_name='Способ оплаты'
    )
    comment = models.TextField('Комментарий', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.id} от {self.name}"
