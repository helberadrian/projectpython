from unicodedata import name
from django.urls import path
from blog import views, urls

#login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("usuario/", views.usuario, name="usuario"),
    path("articulo/", views.articulo, name="articulo"),
    path("buscar/", views.busquedaUsuario, name="busquedaUsuario"),
    path(r'^(?P<pk>\d+)$', views.detalleArticulos.as_view(template_name= "blog/articulos.html"), name='detalle'),
    path(r'^nuevo$', views.crearArticulos.as_view(template_name= "blog/articulos.html"), name='nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.updateArticulos.as_view(template_name= "blog/articulos.html"), name='editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.eliminarArticulos.as_view(template_name= "blog/articulos.html"), name='eliminar'),
    path("login/", views.login_request, name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", LogoutView.as_view(template_name= "blog/logout.html"), name="logout"),
    path("editarUsuario/", views.editarUsuario, name="editarUsuario"),
]