from unicodedata import name
from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("curso/", views.curso, name="curso"),
    path("estudiante/", views.estudiante, name="estudiante"),
    path("profesor/", views.profesor, name="profesor"),
    path("entregable/", views.entregable, name="entregable"),
    path("formulario/", views.formulario, name="formulario"),
    path("busquedaCamada/", views.busquedaCamada, name="busquedaCamada"),
    path("buscar/", views.buscar, name="buscar"),
]