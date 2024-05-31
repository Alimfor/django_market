from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250, blank=False, null=False)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"