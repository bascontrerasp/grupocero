from django import forms
from .models import Ciudad,Cliente
from django.forms import ModelForm


class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = ["ciudad",]
        labels = {'ciudad': 'ciudad',}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'email', 'telefono', 'id_ciudad']
    def __str__(self):
        return self.nombre