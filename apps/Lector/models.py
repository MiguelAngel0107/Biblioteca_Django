from django.db import models
from apps.Libro import models as model
# Create your models here.

class Lector(models.Model):

    nombre = models.CharField(
        'Nombre', 
        max_length=50
    )
    apellido = models.CharField(
        'Apellido', 
        max_length=50
    )
    nacionalidad = models.CharField(
        'Nacionalidad', 
        max_length=50
    )
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Prestamo(models.Model):
    
    lector = models.ForeignKey(
        Lector, 
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        model.Libro, 
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField(
        'Fecha de Prestamo', 
        auto_now=False, 
        auto_now_add=False
    )
    fecha_devolucion = models.DateField(
        'Fecha de Devolucion', 
        auto_now=False, 
        auto_now_add=False, 
        blank=True, 
        null=True
    )
    estado = models.BooleanField()

    def __str__(self):
        return self.libro.titulo
