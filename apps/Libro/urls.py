from django.urls import path
from apps.Libro import views

urlpatterns = [
    path("libros/", views.ListLibros.as_view(), name='libros'),
    
]