# Generated by Django 5.0.3 on 2024-04-12 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_taken',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_taken_at',
        ),
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_executor', models.TextField(blank=True, null=True, verbose_name='Об исполнителе')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('accepted', 'Принято'), ('rejected', 'Отклонено')], default='pending', max_length=20, verbose_name='Статус')),
                ('executor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_requests', to='freelance.executor', verbose_name='Исполнитель')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='freelance.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Заявка на заказ',
                'verbose_name_plural': 'Заявки на заказы',
                'unique_together': {('order', 'executor')},
            },
        ),
    ]
