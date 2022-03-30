import imp
from django import forms

class formUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    usuario = forms.CharField(max_length=40)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=20)

class formArticulo(forms.Form):
    titulo = forms.CharField(max_length=300)
    contenido = forms.CharField(max_length=20000)
    fecha = forms.DateField()

class formEtiqueta(forms.Form):
    nombre = forms.CharField(max_length=40)