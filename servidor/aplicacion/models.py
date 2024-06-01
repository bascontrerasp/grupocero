from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    
def __str__(self):
    return str(self.genero)

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique=True,max_length=30, blank=True, null=True)
    contrasena = models.CharField(max_length=100)
    
def __str__(self):
    return str(self.nombre)