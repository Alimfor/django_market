from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

admin.site.register(Customer, CustomersAdmin)
