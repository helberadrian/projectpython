from unicodedata import name
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("usuario/", views.usuario, name="usuario"),
    path("articulo/", views.articulo, name="articulo"),
    path("etiqueta/", views.etiqueta, name="etiqueta"),
    path("buscar/", views.busquedaUsuario, name="busquedaUsuario"),
]