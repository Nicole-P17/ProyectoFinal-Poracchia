from django.db import models

# Create your models here.
class Terapeuta (models.Model):
    nombre=models.CharField(max_length=40)
    edad = models.IntegerField()
    precioSesion = models.IntegerField()
    especializacion= models.TextField(max_length=100)
    matricula = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.EmailField()

class Paciente (models.Model):
    nombre=models.CharField(max_length=40)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.EmailField()

class Consultante (models.Model):
    nombre=models.CharField(max_length=40)
    motivo = models.TextField(max_length=100)
    telefono = models.IntegerField()
    mail = models.EmailField()