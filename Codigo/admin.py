from django.contrib import admin
from .models import Coordenadas, Zona, Usuario, Cliente, ZonasCoordenadas, Trabajador, ZonasTrabajador, DatosFacturacion, Marcas, Categorias, FormaPago, Productos, CabeceraPedido, DetallePedido, Pagos

# Register your models here.
admin.site.register(Coordenadas)
admin.site.register(Zona)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(ZonasCoordenadas)
admin.site.register(Trabajador)
admin.site.register(ZonasTrabajador)
admin.site.register(DatosFacturacion)
admin.site.register(Marcas)
admin.site.register(Categorias)
admin.site.register(FormaPago)
admin.site.register(Productos)
admin.site.register(CabeceraPedido)
admin.site.register(DetallePedido)
admin.site.register(Pagos)

