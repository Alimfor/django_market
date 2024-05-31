from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'customer', 'executor', 'service', 'deadline', 'is_taken']

admin.site.register(Order, OrderAdmin)