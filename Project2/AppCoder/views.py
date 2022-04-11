from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import Formulario

# Requerimientos de Autenticación
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/index.html")

def curso(request):
    return render(request, "AppCoder/curso.html")

def estudiante(request):
    return render(request, "AppCoder/estudiantes.html")

def profesor(request):
    return render(request, "AppCoder/profesores.html")

def entregable(request):
    return render(request, "AppCoder/entregables.html")

def formulario(request):
    if request.method == "POST":
        miFormulario = Formulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Curso(nombre=info["curso"], camada=info["camada"])
            curso.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = Formulario()
    return render(request, "AppCoder/formulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultados.html", {"cursos":cursos,"camada":camada})
    else:
        respuesta = "No enviaste datos..."
    return HttpResponse(respuesta)

def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            username = data.get("username")
            password = data.get("password")
            