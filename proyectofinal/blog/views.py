from re import template
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import formUsuario, formArticulo, UserEditForm #UserRegisterForm
from blog.models import Usuario, Articulo

#View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import is_valid_path, reverse_lazy

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    return render(request, "blog/index.html", contexto)

def about(request):
    return render(request, "blog/about.html")

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

def busquedaUsuario(request):
    if request.GET["usuario"]:
        usuario = request.GET["usuario"]
        usuarios = Usuario.objects.filter(usuario__icontains=usuario)
        return render(request, "blog/resultados.html", {"usuarios":usuarios, "usuario":usuario})
    else:
        respuesta = "No enviaste datos..."
    return HttpResponse(respuesta)

class detalleArticulos(DetailView):
    model = Articulo
    template_name = "blog/detalleArticulos.html"

#View del Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "blog/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "blog/index.html", {"mensaje": "Error, los datos ingresados son incorrectos..."})
        
        else:
            return render(request, "blog/index.html", {"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "blog/login.html", {"form":form})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "blog/index.html", {"mensaje": "Usuario creado con exito"})
    
    else:
        form = UserCreationForm()
        return render(request, "blog/registro.html", {"form":form})

@login_required
def editarUsuario(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            usuario.email = info["email"]
            usuario.pass1 = info["pass1"]
            usuario.pass2 = info["pass2"]
            usuario.save()

            return render(request, "blog/index.html")
    else:
        miFormulario = UserEditForm(initial={"email": usuario.email})
    
    return render(request, "blog/editar_usuario.html", {"miFormulario":miFormulario})

class crearArticulos(CreateView):
    model = Articulo
    success_url = "blog/successArticulos.html"
    fields = ["titulo", "contenido", "fecha", "imagen", "resumen"]

class updateArticulos(UpdateView):
    model = Articulo
    success_url = "blog/successArticulos.html"
    fields = ["titulo", "contenido", "fecha", "imagen", "resumen"]

class eliminarArticulos(DeleteView):
    model = Articulo
    success_url = "blog/successArticulos.html"