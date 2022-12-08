from django.db import models
from apps.Autor import models as model

from apps.Libro import managers
# Create your models here.

class Categoria(models.Model):
    
    nombre = models.CharField('Categoria', max_length=50)

    def __str__(self) :
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(model.Autor)
    titulo = models.CharField('Titulo', max_length=50)
    fecha = models.DateField('Fecha Publicacion', auto_now=False, auto_now_add=False)
    portada = models.ImageField('Portada', upload_to='portada', height_field=None, width_field=None, max_length=None)
    visitas = models.PositiveIntegerField()

    objects = managers.LibrosManager()

    def __str__(self):
        return self.titulo