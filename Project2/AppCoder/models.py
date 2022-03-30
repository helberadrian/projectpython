from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Camada: {self.camada}" #Para poder ver los valores y no como objeto


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Profesión: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Fecha: {self.fecha}, Entregado: {self.entregado}"