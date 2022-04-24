from dataclasses import field
import imp
from django import forms

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class formUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    usuario = forms.CharField(max_length=40)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=20)

class formArticulo(forms.Form):
    titulo = forms.CharField(max_length=300)
    contenido = forms.CharField(max_length=200000)
    resumen = forms.CharField(max_length=20000)
    imagen = forms.CharField(max_length=3000)
    fecha = forms.DateField()

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     pass1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     pass2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["usuario", "email", "pass1", "pass2"]
#         help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    pass1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    pass2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "pass1", "pass2"]
        help_text = {k:"" for k in fields}
