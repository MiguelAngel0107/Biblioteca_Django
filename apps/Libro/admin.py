from django.contrib import admin

# Register your models here.

from apps.Libro import models

admin.site.register(models.Libro)
admin.site.register(models.Categoria)
