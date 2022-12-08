from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from apps.Autor import models
# Create your views here.

class ListAutores(ListView):
    model = models.Autor
    context_object_name = 'Lista_Autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        print(palabra_clave)
        #return models.Autor.objects.all()
        return models.Autor.objects.buscar_autores(palabra_clave)
