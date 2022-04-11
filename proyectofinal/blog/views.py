from re import template
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import formUsuario, formArticulo, formEtiqueta
from blog.models import Usuario, Articulo, Etiqueta
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "blog/index.html")

def usuario(request):
    if request.method == "POST":
        miFormulario = formUsuario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Usuario(nombre=info["nombre"], apellido=info["apellido"], usuario=info["usuario"], email=info["email"], contraseña=info["contraseña"])
            curso.save()
            return render(request, "blog/index.html")
    else:
        miFormulario = formUsuario()
    return render(request, "blog/usuarios.html", {"miFormulario":miFormulario})

def articulo(request):
    if request.method == "POST":
        miFormulario = formArticulo(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Articulo(titulo=info["titulo"], contenido=info["contenido"], fecha=info["fecha"])
            curso.save()
            return render(request, "blog/index.html")
    else:
        miFormulario = formArticulo()
    return render(request, "blog/articulos.html", {"miFormulario":miFormulario})

def etiqueta(request):
    if request.method == "POST":
        miFormulario = formEtiqueta(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Etiqueta(nombre=info["nombre"])
            curso.save()
            return render(request, "blog/index.html")
    else:
        miFormulario = formEtiqueta()
    return render(request, "blog/etiquetas.html", {"miFormulario":miFormulario})

def busquedaUsuario(request):
    if request.GET["usuario"]:
        usuario = request.GET["usuario"]
        usuarios = Usuario.objects.filter(usuario__icontains=usuario)
        return render(request, "blog/resultados.html", {"usuarios":usuarios, "usuario":usuario})
    else:
        respuesta = "No enviaste datos..."
    return HttpResponse(respuesta)

class leerArticulos(ListView):
    model = Articulo
    template_name = "blog/leerArticulos.html"

class detalleArticulos(DetailView):
    model = Articulo
    template_name = "blog/detalleArticulos.html"

class crearArticulos(CreateView):
    model = Articulo
    success_url = "blog/successArticulos.html"
    fields = ["titulo", "contenido", "fecha"]

class updateArticulos(UpdateView):
    model = Articulo
    success_url = "blog/successArticulos.html"
    fields = ["titulo", "contenido", "fecha"]

class eliminarArticulos(DeleteView):
    model = Articulo
    success_url = "blog/successArticulos.html"