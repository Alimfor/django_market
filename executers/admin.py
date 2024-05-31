from django.contrib import admin
from .models import Executor

class ExecutersAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Executor, ExecutersAdmin)