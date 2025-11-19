from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    preferencia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# (PROVEEDOR y PRODUCTO quedan pendientes - abajo hay plantillas comentadas)

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    tipo_producto_suministro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empresa

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"
    
# ==========================================
# MODELO: FLOTA_PRODUCCION
# ==========================================
class Flota_produccion(models.Model):
    tipo_transporte = models.CharField(max_length=100)
    nombre_transporte = models.CharField(max_length=100)
    placas = models.CharField(max_length=20, unique=True)
    codigo = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_transporte} - {self.placas}"
    
# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado")
    fecha_venta = models.DateField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad_vendida = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta} - ${self.monto_total}"