from dataclasses import field
import imp
from django import forms

class formUsuario(forms.Form):
    usuario = forms.CharField(max_length=40)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=20)

class formArticulo(forms.Form):
    titulo = forms.CharField(max_length=300)
    contenido = forms.CharField(max_length=200000)
    resumen = forms.CharField(max_length=20000)
    imagen = forms.CharField(max_length=3000)