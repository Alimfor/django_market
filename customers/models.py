from django.db import models
from django.conf import settings

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Заказчик"
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"
