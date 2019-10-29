from django.db import models

# Create your models here.
class Coordenadas(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self):
        return '%s %s' % (self.latitud, self.longitud)

class Zona(models.Model):
    descripcion = models.CharField(max_length = 200)
    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    dni = models.CharField(max_length = 8, primary_key=True)
    nombre = models.CharField(max_length = 200)
    apellidos = models.CharField(max_length = 200)
    contacto = models.CharField(max_length = 13)
    email = models.CharField(max_length = 200)
    direccion = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s' % (self.apellidos, self.nombre)

class Cliente(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    puntaje = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    verificado = models.BooleanField()

    def __str__(self):
        return '%s %s' % (self.idUsuario, self.puntaje)

class ZonasCoordenadas(models.Model):
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    idCoordenadas = models.ForeignKey(Coordenadas, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.idZona, self.idCoordenadas)


class Trabajador(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    def __str__(self):
        return '%s %s' % (self.idUsuario, self.fecha_inicio)


class ZonasTrabajador(models.Model):
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self):
        return '%s %s' % (self.idTrabajador, self.idZona)


class DatosFacturacion(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ruc = models.CharField(max_length = 200)
    razon_social = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s %s' % (self.idCliente, self.razon_social, self.ruc)


class Marcas(models.Model):
    descripcion = models.CharField(max_length = 200)
    def __str__(self):
        return self.descripcion

class Categorias(models.Model):
    descripcion = models.CharField(max_length = 200)
    def __str__(self):
        return self.descripcion

class FormaPago(models.Model):
    descripcion = models.CharField(max_length = 200)
    def __str__(self):
        return self.descripcion

class Productos(models.Model):
    idMarca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    tipo = models.CharField(max_length = 200)
    presentacion = models.CharField(max_length = 200)
    precio = models.FloatField()
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.tipo, self.presentacion)


class CabeceraPedido(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    pagado = models.BooleanField()
    idFormaPago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    descuento = models.FloatField()
    def __str__(self):
        return '%s %s' % (self.idCliente, self.idTrabajador)


class DetallePedido(models.Model):
    idCabeceraPedido = models.ForeignKey(CabeceraPedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return '%s %s' % (self.idProducto, self.cantidad)


class Pagos(models.Model):
    idCabeceraPedido = models.ForeignKey(CabeceraPedido, on_delete=models.CASCADE)
    idTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()
    def __str__(self):
        return '%s %s' % (self.monto, self.fecha_pago)
