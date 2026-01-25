from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("E-mail")
    phone = models.CharField("Телефон", max_length=20)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_read = models.BooleanField("Прочитано", default=False)
    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name} - {self.email}"
