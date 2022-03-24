from contextvars import Context
from multiprocessing import context
from pipes import Template
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola este es un Response")

def saludoHtml(request):
    return HttpResponse("<h1>Saludo en:</h1><br><h3>HTML pana...</h3>")

def diadehoy(request):
    date = datetime.now()
    texto = f"La fecha de hoy es: {date}"
    return HttpResponse(texto)

def minombre(request, nombre):
    return HttpResponse(f"Mi nombre es: {nombre}")

def probandoTemplate(request):
    nom = "Helber"
    ap = "Rodriguez"
    notas = [10,9,8,4,3,5,9]
    diccionario = {"nombre": nom,"apellido": ap,"notas": notas}
    
    plantilla = loader.get_template("template1.html") #Abrimos el archivo
    #plantilla = Template(html.read()) #Creamos la plantilla
    #html.close() #Cerramos el archivo despues de leerlo
    #contexto = Context(diccionario) #Se guarda el contexto en el caso de que haya parametros
    documento = plantilla.render(diccionario) #Se renderiza la plantilla

    return HttpResponse(documento)

