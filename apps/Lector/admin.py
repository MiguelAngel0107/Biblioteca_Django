from django.contrib import admin

# Register your models here.

from apps.Lector import models

admin.site.register(models.Lector)
admin.site.register(models.Prestamo)