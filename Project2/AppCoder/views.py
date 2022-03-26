from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre="Desarrollo Web", camada=2806)
    curso.save()

    documento = f"Agregado --> Curso: {curso.nombre} a la camada {curso.camada}"
    return HttpResponse(documento)