from rest_framework import serializers
from .models import *

class CoordenadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenada
        fields = ['latitud', 'longitud','orden_polygono']

class ZonaSerializer(serializers.ModelSerializer):
    coordenadas = CoordenadaSerializer(many=True)
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
        fields = ['apellidos','nombre','dni','fecha_inicio','contacto','usuario','contrasenia','foto_perfil']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['descripcion']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['descripcion']

class ProductosSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer(many=False)
    categoria = CategoriaSerializer(many=False)
    class Meta:
        model = Producto
        fields = ['id','marca', 'categoria', 'nombre', 'tipo', 'presentacion' , 'precio', 'descripcion']

class  FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = ['descripcion']

    
class  DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductosSerializer(many=False)
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']


class  CabeceraPedidoSerializer(serializers.ModelSerializer):
    detalle_pedido = DetallePedidoSerializer(many=True)
    cliente = ClienteSerializer(many=False)
    trabajador = TrabajadorSerializer(many=False)
    formaPago = FormaPagoSerializer(many=False)
    class Meta:
        model = CabeceraPedido
        fields = ['id','cliente', 'trabajador', 'fecha_pedido', 'fecha_entrega','entregado','pagado','formaPago','descuento','monto','detalle_pedido']








