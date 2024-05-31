from django.db import models
from django.conf import settings


class Executor(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"
