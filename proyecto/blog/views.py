from re import template
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import formUsuario, formArticulo
from blog.models import Usuario, Articulo
import datetime

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

def usuario(request): #No se usa, guardar un nuevo usuario
    if request.method == "POST":
        miFormulario = formUsuario(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            user = Usuario(nombre=info["nombre"], contenido=info["contenido"], usuario=info["usuario"], resumen=info["resumen"], contraseña=info["contraseña"])
            user.save()
            return render(request, "blog/index.html")
    else:
        miFormulario = formUsuario()
    return render(request, "blog/usuarios.html", {"miFormulario":miFormulario})

def detalleArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    contexto= {"articulo":articulo}
    return render(request, "blog/articulos_detalle.html", contexto)

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
def admin(request):
    return render(request, "blog/admin.html")

def crearArticulo(request):
    date = datetime.datetime.now()

    if request.method == "POST":
        miFormulario = formArticulo(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            article = Articulo(titulo=info["titulo"], contenido=info["contenido"], resumen=info["resumen"], imagen=info["imagen"], fecha=date)
            article.save()
            return render(request, "blog/articulos_success.html")
    else:
        miFormulario = formArticulo()
    return render(request, "blog/articulo_nuevo.html", {"miFormulario":miFormulario})

def editarArticulo(request, id):
      articulo = Articulo.objects.get(id=id)
      if request.method == 'POST':
            miFormulario = formArticulo(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  articulo.titulo = informacion['titulo']
                  articulo.contenido = informacion['contenido']
                  articulo.resumen = informacion['resumen']
                  articulo.imagen = informacion['imagen']
                  articulo.save()
                  return render(request, "blog/articulos_success.html")
      else: 
            miFormulario= formArticulo(initial={'titulo': articulo.titulo, 'contenido':articulo.contenido , 
            'resumen':articulo.resumen, 'imagen':articulo.imagen})
      return render(request, "blog/articulos_update.html", {"miFormulario":miFormulario})

def eliminarArticulo(request, id):
      articulo = Articulo.objects.get(id=id)
      articulo.delete()

      articulos = Articulo.objects.all()
      contexto= {"articulos":articulos}
      return render(request, "blog/articulos_success.html", contexto)

