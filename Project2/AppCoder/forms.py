from django import forms

class Formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()