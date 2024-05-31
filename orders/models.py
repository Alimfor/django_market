from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Order(models.Model):
    title = models.CharField(verbose_name="Описание", max_length=250, blank=False, null=False)
    description = models.TextField(verbose_name="Описание", blank=False, null=False)
    customer = models.ForeignKey(to='customers.Customer', on_delete=models.CASCADE, verbose_name="Покупатель", related_name="customer_profile")
    executor = models.ForeignKey(to='executers.Executor', on_delete=models.CASCADE, verbose_name="Исполнитель", related_name="executor_profile", null=True, blank=True)
    service = models.ForeignKey(to='services.Service', on_delete=models.CASCADE, verbose_name="Услуга")
    price = models.DecimalField(verbose_name="Цена", blank=False, null=False, max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name="Изменен", auto_now=True, null=False)
    end_at = models.DateTimeField(verbose_name="Завершен", null=True) 

    deadline = models.DateTimeField(verbose_name="Дедлайн", null=True)
    is_taken = models.BooleanField(default=False, verbose_name="Взят на выполнение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

@receiver(post_save, sender=Order)
def notify_client(sender, instance, created, **kwargs):
    if created:
        # Notify client about the new order
        pass