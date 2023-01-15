from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Logs)
class Logs(admin.ModelAdmin):
    list_display = [field.name for field in Logs._meta.fields]
    search_fields = ('user__username', 'status',)