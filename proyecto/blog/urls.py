from unicodedata import name
from django.urls import path
from blog import views, urls

#login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    #CRUD Articulos
    path("crearArticulo/", views.crearArticulo, name="nuevo"),
    path("detalleArticulo/<id>/", views.detalleArticulo, name="detalle"),
    path("editarArticulo/<id>/", views.editarArticulo, name="editar"),
    path("eliminarArticulo/<id>/", views.eliminarArticulo, name="eliminar"),
    #Login y Usuario
    path("login/", views.login_request, name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", LogoutView.as_view(template_name= "blog/logout.html"), name="logout"),
    path("blog/admin/", views.admin, name="admin"),
]