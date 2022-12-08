from django.urls import path
from apps.Autor import views

urlpatterns = [
    path("autores/", views.ListAutores.as_view(), name='autores'),
    
]