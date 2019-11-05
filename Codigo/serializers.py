from rest_framework import serializers
from .models import *
class ClienteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cliente
        fields = ['apellidos','nombre','dni','puntaje','latitud','longitud','verificado']

class TrabajadorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Trabajador
        fields = ['apellidos','nombre','dni','fecha_inicio']

