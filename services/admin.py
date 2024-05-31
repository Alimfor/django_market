from django.contrib import admin
from .models import Service

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Service, ServicesAdmin)