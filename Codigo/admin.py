from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Coordenada)
admin.site.register(Zona)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(ZonaCoordenada)
admin.site.register(Trabajador)
admin.site.register(ZonaTrabajador)
admin.site.register(DatosFacturacion)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(FormaPago)
admin.site.register(Producto)
admin.site.register(CabeceraPedido)
admin.site.register(DetallePedido)
admin.site.register(Pago)

