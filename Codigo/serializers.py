from rest_framework import serializers
from .models import *

class CoordenadaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Coordenada
        fields = ['latitud', 'longitud','orden_polygono']

class ZonaSerializer(serializers.ModelSerializer):
    coordenadas = CoordenadaSerialize(many=True)
    class Meta:
        model = Zona
        fields = ['id', 'descripcion', 'coordenadas']

class DatosFacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosFacturacion
        fields = ['ruc', 'razon_social']

class ClienteSerializer(serializers.ModelSerializer): 
    datos_facturacion = DatosFacturacionSerializer(many=True)
    zona = ZonaSerializer(many=False)
    class Meta:
        model = Cliente
        fields = ['apellidos','nombre','dni','puntaje','direccion','latitud','longitud','verificado','datos_facturacion','zona']


class TrabajadorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Trabajador
        fields = ['apellidos','nombre','dni','fecha_inicio']


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['descripcion', 'categoria', 'precio']

class  DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['cantidad', 'producto']


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


