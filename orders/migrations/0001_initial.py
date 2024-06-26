# Generated by Django 5.0.6 on 2024-05-16 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('executers', '0001_initial'),
        ('services', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('end_at', models.DateTimeField(null=True, verbose_name='Завершен')),
                ('deadline', models.DateTimeField(null=True, verbose_name='Дедлайн')),
                ('is_taken', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to='customers.customers', verbose_name='Покупатель')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executor_profile', to='executers.executers', verbose_name='Исполнитель')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
