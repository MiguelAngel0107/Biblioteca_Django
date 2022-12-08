from django.db import models
from django.db.models import Q

#Basicamente Esto Sirve Para filtrar los Datos

class AutorManager(models.Manager):

    def listar_autores(self):
        return self.all()

    def buscar_autores(self, kword):
        resultado = self.filter(
            #nombre=kword
            nombre__icontains = kword
        )
        return resultado
    
    def buscar_autores2(self, kword):
        resultado = self.filter(
            #Esto es una operacion logica de Or
            Q(nombre__icontains = kword) | Q(apellido__icontains = kword)   
        )
        return resultado