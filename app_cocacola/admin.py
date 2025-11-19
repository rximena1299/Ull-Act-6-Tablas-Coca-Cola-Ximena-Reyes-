from django.contrib import admin
from .models import Cliente, Proveedor, Producto, Empleado, Flota_produccion, Venta
# ==========================================
# ADMIN: CLIENTE
# ==========================================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'email', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')

# ==========================================
# ADMIN: PROVEEDOR
# ==========================================
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_empresa', 'contacto', 'telefono', 'correo', 'pais')
    search_fields = ('nombre_empresa', 'contacto', 'correo', 'telefono')

# ==========================================
# ADMIN: PRODUCTO
# ==========================================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_producto',
        'categoria',
        'precio_unitario',
        'stock_actual',
        'fecha_fabricacion',
        'fecha_vencimiento',
        'cliente',
        'proveedor'
    )
    search_fields = ('nombre_producto', 'categoria')
    list_filter = ('categoria', 'proveedor', 'cliente')



# ==========================================
# ADMIN: EMPLEADO
# ==========================================
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'puesto', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'puesto')
    list_filter = ('puesto',)


# ==========================================
# ADMIN: FLOTA_PRODUCCION
# ==========================================
@admin.register(Flota_produccion)
class FlotaProduccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_transporte', 'nombre_transporte', 'placas', 'codigo', 'modelo')
    search_fields = ('nombre_transporte', 'placas', 'codigo', 'modelo', 'tipo_transporte')
    list_filter = ('tipo_transporte',)


# ==========================================
# ADMIN: VENTA
# ==========================================
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_empleado', 'fecha_venta', 'id_cliente', 'id_producto', 'cantidad_vendida', 'monto_total')
    search_fields = ('id_empleado__nombre', 'id_cliente__nombre', 'id_producto__nombre_producto')
    list_filter = ('fecha_venta', 'id_empleado', 'id_cliente')
    date_hierarchy = 'fecha_venta'