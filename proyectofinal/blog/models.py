from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=40)
    email = models.EmailField()
    contraseña = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Usuario: {self.usuario}, Email: {self.email}, Contraseña: {self.contraseña}"

class Articulo(models.Model):
    titulo = models.CharField(max_length=300)
    contenido = models.CharField(max_length=200000)
    fecha = models.DateField()
    imagen = models.CharField(max_length=3000)
    resumen = models.CharField(max_length=20000)

    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Contenido: {self.contenido}, Fecha: {self.fecha}, Imagen: {self.imagen}"

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"