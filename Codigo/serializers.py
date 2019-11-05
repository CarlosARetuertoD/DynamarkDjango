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


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['descripcion', 'idCategoria', 'precio']

class  DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['cantidad', 'idProducto']


class  CabeceraPedidoSerializer(serializers.ModelSerializer):
    detalle = DetallePedidoSerializer(many=True)
    class Meta:
        model = CabeceraPedido
        fields = ['fecha_pedido', 'fecha_entrega', 'monto', 'detalle']



class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True)

    class Meta:
        model = Categoria
        fields = ['descripcion', 'productos']


