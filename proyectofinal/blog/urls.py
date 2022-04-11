from unicodedata import name
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("usuario/", views.usuario, name="usuario"),
    path("articulo/", views.articulo, name="articulo"),
    path("etiqueta/", views.etiqueta, name="etiqueta"),
    path("buscar/", views.busquedaUsuario, name="busquedaUsuario"),
    path("successArticulos/", views.leerArticulos.as_view(), name="success"),
    path(r'^(?P<pk>\d+)$', views.detalleArticulos.as_view(), name='detalle'),
    path(r'^nuevo$', views.crearArticulos.as_view(), name='nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.updateArticulos.as_view(), name='editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.eliminarArticulos.as_view(), name='eliminar'),
]