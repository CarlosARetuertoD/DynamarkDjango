from django.db import models

# Create your models here.
class Coordenada(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self):
        return '%s %s' % (self.latitud, self.longitud)

class Meta:
        verbose_name_plural = "Lista de puntos del mapa"
        verbose_name = "Punto del mapa"

class Zona(models.Model):
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Lista de Zonas"
        verbose_name = "Zona"

class Usuario(models.Model):
    dni = models.CharField(max_length = 8, primary_key=True)
    nombre = models.CharField(max_length = 200)
    apellidos = models.CharField(max_length = 200)
    contacto = models.CharField(max_length = 13)
    email = models.CharField(max_length = 200)
    direccion = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s' % (self.apellidos, self.nombre)
    
    class Meta:
        verbose_name_plural = "Lista de Usuarios"
        verbose_name = "Usuario"

class Cliente(Usuario):
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    puntaje = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    verificado = models.BooleanField()

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellidos, self.puntaje)

    class Meta:
        verbose_name_plural = "Lista de Clientes"
        verbose_name = "Cliente"

class ZonaCoordenada(models.Model):
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    idCoordenadas = models.ForeignKey(Coordenada, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.idZona, self.idCoordenadas)
    
    class Meta:
        verbose_name_plural = "Asignacion de Coordenadas a Zonas"
        verbose_name = "Coordenadas de una zona"


class Trabajador(Usuario):
    fecha_inicio = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellidos, self.fecha_inicio)
    
    class Meta:
        verbose_name_plural = "Trabajadores"
        verbose_name = "Trabajador"


class ZonaTrabajador(models.Model):
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return '%s %s' % (self.idTrabajador, self.idZona)
    
    class Meta:
        verbose_name_plural = "Zonas Asignadas"
        verbose_name = "Zona Asignada"


class DatosFacturacion(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ruc = models.CharField(max_length = 200)
    razon_social = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s %s' % (self.idCliente, self.razon_social, self.ruc)
    
    class Meta:
        verbose_name_plural = "Datos de Facturacion"
        verbose_name = "Datos de Facturacion"


class Marca(models.Model):
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Lista de Marcas"
        verbose_name = "Marca"

class Categoria(models.Model):
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Lista de Categorias"
        verbose_name = "Categoria"

class FormaPago(models.Model):
    descripcion = models.CharField(max_length = 200)
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Formas de Pago"
        verbose_name = "Forma de Pago"

class Producto(models.Model):
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    tipo = models.CharField(max_length = 200)
    presentacion = models.CharField(max_length = 200)
    precio = models.FloatField()
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.tipo, self.presentacion)

    class Meta:
        verbose_name_plural = "Lista de Productos"
        verbose_name = "Producto"


class CabeceraPedido(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    pagado = models.BooleanField()
    idFormaPago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    descuento = models.FloatField()
    monto = models.FloatField()

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.idCliente, self.idTrabajador, self.entregado, self.pagado, self.monto)
    
    class Meta:
        verbose_name_plural = "Cabeceras de Pedidos"
        verbose_name = "Cabecera de Pedido"


class DetallePedido(models.Model):
    idCabeceraPedido = models.ForeignKey(CabeceraPedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.idProducto, self.cantidad)
    
    class Meta:
        verbose_name_plural = "Detalles Pedidos"
        verbose_name = "Detalle Pedido"


class Pago(models.Model):
    idCabeceraPedido = models.ForeignKey(CabeceraPedido, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()

    def __str__(self):
        return '%s %s' % (self.monto, self.fecha_pago)

    class Meta:
        verbose_name_plural = "Marcas de Producto"
        verbose_name = "Marca"
