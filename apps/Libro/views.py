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
        print(palabra_clave)
        #return models.Autor.objects.all()
        return models.Libro.objects.buscar_libros(palabra_clave)


