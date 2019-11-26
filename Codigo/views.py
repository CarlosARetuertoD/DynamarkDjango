from django.http import HttpResponse
from rest_framework import generics

from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Di Lorenzo Application")


class ClienteList(generics.ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class ProductosList(generics.ListAPIView):
    serializer_class = ProductosSerializer
    queryset = Producto.objects.all()

class PedidosList(generics.ListAPIView):
    serializer_class = CabeceraPedidoSerializer
    queryset = CabeceraPedido.objects.all()

class TrabajadoresList(generics.ListAPIView):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()

class ZonaList(generics.RetrieveAPIView):
    serializer_class = ZonaSerializer
    queryset = Zona.objects.all()


