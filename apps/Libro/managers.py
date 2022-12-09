import datetime
from django.db import models
from django.db.models import Q

#Basicamente Esto Sirve Para filtrar los Datos

class LibrosManager(models.Manager):

    def listar_libros(self):
        return self.all()

    def buscar_libros(self, kword):
        resultado = self.filter(
            #titulo=kword
            titulo__icontains = kword
        )
        return resultado
    
    def buscar_libros2(self, kword):
        resultado = self.filter(
            #Esto es una operacion logica de Or
            Q(titulo__icontains = kword) | Q(categoria__icontains = kword)   
        )
        return resultado

    def listar_libros2(self, f1,f2):
        resultado = self.filter(
            fecha__range = (f1,f2)
        )
        return resultado

    def Imagenes(self, p):
        resultado = self.get(id=2)

        return resultado