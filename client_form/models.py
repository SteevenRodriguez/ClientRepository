from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    LOCATION_CHOICES = (
        ('U', 'Urbano'),
        ('R', 'Rural'),
     )

    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    procedencia = models.CharField(max_length=1 ,choices=LOCATION_CHOICES)
    origen = models.CharField(max_length=20)
    derivacion = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    tratamiento = models.ForeignKey('Product', 
            on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre


class Product(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class Register(models.Model):
    fecha = models.DateTimeField(
                        default=timezone.now)
    paciente = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha.strftime('%b %d %Y %H:%M:%S')
