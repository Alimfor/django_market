from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'executor'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1, verbose_name='Тип пользователя')
    email = models.EmailField(unique=True, verbose_name='Электронная почта' )
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, verbose_name='Рейтинг')

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
