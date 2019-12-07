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



class PedidoDetail(generics.RetrieveAPIView):
    serializer_class = CabeceraPedidoSerializer
    queryset = CabeceraPedido.objects.all()



class AddPedido(generics.CreateAPIView):
    serializer_class = AddCabeceraPedidoSerializer
    queryset = CabeceraPedido.objects.all()


class AddDetallePedido(generics.CreateAPIView):
    serializer_class = AddDetallePedidoSerializer
    queryset = DetallePedido.objects.all()



class TrabajadoresList(generics.ListAPIView):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()



class ZonaList(generics.RetrieveAPIView):
    serializer_class = ZonaSerializer
    queryset = Zona.objects.all()


class TrabajadorDetail(generics.RetrieveAPIView):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()


class ClienteDetail(generics.RetrieveAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class Trabajador_PedidosList(generics.ListAPIView):
    serializer_class = Trabajador_PedidosSerializer
    def get_queryset(self):
        dni = self.kwargs['dni']
        return CabeceraPedido.objects.filter(trabajador=dni)


class ZonaTrabajadorList(generics.ListAPIView):
    serializer_class = ZonaTrabajadorSerializer
    def get_queryset(self):
        dni = self.kwargs['dni']
        return ZonaTrabajador.objects.filter(trabajador=dni)


class FormaPagoList(generics.ListAPIView):
    serializer_class = DetailFormaPagoSerializer
    queryset = FormaPago.objects.all()


class ProductoDetail(generics.RetrieveAPIView):
    serializer_class = ProductosSerializer
    queryset = Producto.objects.all()