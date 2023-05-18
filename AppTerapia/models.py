from django.db import models

# Create your models here.
class Terapeuta (models.Model):
    nombre=models.CharField(max_length=40)
    edad = models.IntegerField()
    precioSesion = models.IntegerField()
    especializacion= models.CharField(max_length=100)
    matricula = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.EmailField(blank=True)

    def __str__ (self):
        return f"{self.nombre} | {self.especializacion}"

class Paciente (models.Model):
    nombre=models.CharField(max_length=40)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.EmailField(blank=True)
    def __str__ (self):
        return f"{self.nombre}"

class Consultante (models.Model):
    nombre=models.CharField(max_length=40)
    motivo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    mail = models.EmailField()
    def __str__ (self):
        return f"{self.nombre} | {self.motivo}"