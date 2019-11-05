from django.http import HttpResponse
from rest_framework import generics

from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Hola Codigo")


class ClienteList(generics.ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class TrabajadorList(generics.ListCreateAPIView):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()


class CategoriaList(generics.ListCreateAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProductoList(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class DetalleList(generics.ListAPIView):
    serializer_class = DetallePedidoSerializer
    queryset = DetallePedido.objects.all()


class CabeceraList(generics.ListAPIView):
    serializer_class = CabeceraPedidoSerializer
    queryset = CabeceraPedido.objects.all()
