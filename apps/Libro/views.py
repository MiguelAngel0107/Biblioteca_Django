from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from apps.Libro import models
# Create your views here.

class ListLibros(ListView):
    model = models.Libro
    context_object_name = 'Lista_Libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        fecha1=self.request.GET.get('f1','')
        fecha2=self.request.GET.get('f2','')
        print(palabra_clave)
        #return models.Autor.objects.all()
        if fecha1 and fecha2:
            return models.Libro.objects.listar_libros2(fecha1,fecha2)
        else:
            return models.Libro.objects.buscar_libros(palabra_clave)

class ListLibros2(ListView):
    model = models.Libro
    context_object_name = 'Lista_Libros'
    template_name = "libro/lista2.html"

    def get_queryset(self):
        return models.Libro.objects.listar_libros_categoria()


