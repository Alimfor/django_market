from django.db import models
from django.conf import settings
from django.utils import timezone

from orders.models import Order
from users.models import CustomUser


class Rating(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='ratings')
    rated_by = models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name='given_ratings')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', default=0)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return f"{self.rating} by {self.rated_by.username} to {self.user.username}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Testimonial(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    testimonial = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.user} for order {self.order}"
