from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id_ciudad = models.AutoField(db_column='idCiudad',primary_key=True)
    ciudad = models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return str(self.ciudad)

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=20)
    email = models.EmailField(unique=True,max_length=30, blank=True, null=True)
    telefono = models.IntegerField(blank=False,null=False)
    id_ciudad = models.ForeignKey('Ciudad',on_delete=models.CASCADE, db_column='idCiudad')
    contrasena = models.CharField(max_length=50)
    def __str__(self):
        return str(self.nombre)
    
