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
