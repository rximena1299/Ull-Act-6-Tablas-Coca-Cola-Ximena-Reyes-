from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Proveedor, Producto, Empleado, Flota_produccion, Venta
from django.urls import reverse
from django.utils import timezone

def inicio_cocacola(request):
    return render(request, 'inicio.html')

# ==============================
# CLIENTE
# ==============================
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()
        preferencia = request.POST.get('preferencia', '').strip()
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            email=email,
            preferencia=preferencia
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        cliente.direccion = request.POST.get('direccion', cliente.direccion).strip()
        cliente.telefono = request.POST.get('telefono', cliente.telefono).strip()
        cliente.email = request.POST.get('email', cliente.email).strip()
        cliente.preferencia = request.POST.get('preferencia', cliente.preferencia).strip()
        cliente.save()
    return redirect('ver_cliente')

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==============================
# PROVEEDOR
# ==============================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa', '').strip()
        contacto = request.POST.get('contacto', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        correo = request.POST.get('correo', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        pais = request.POST.get('pais', '').strip()
        tipo_producto_suministro = request.POST.get('tipo_producto_suministro', '').strip()

        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            contacto=contacto,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            pais=pais,
            tipo_producto_suministro=tipo_producto_suministro
        )
        return redirect('ver_proveedor')

    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('-id')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        proveedor.nombre_empresa = request.POST.get('nombre_empresa', proveedor.nombre_empresa).strip()
        proveedor.contacto = request.POST.get('contacto', proveedor.contacto).strip()
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono).strip()
        proveedor.correo = request.POST.get('correo', proveedor.correo).strip()
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion).strip()
        proveedor.pais = request.POST.get('pais', proveedor.pais).strip()
        proveedor.tipo_producto_suministro = request.POST.get('tipo_producto_suministro', proveedor.tipo_producto_suministro).strip()
        proveedor.save()
    return redirect('ver_proveedor')

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})


# ==============================
# PRODUCTO (CORREGIDO Y FUNCIONAL)
# ==============================
def ver_producto(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


def agregar_producto(request):
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre_producto', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        precio_unitario = request.POST.get('precio_unitario', '').strip()
        stock_actual = request.POST.get('stock_actual', '').strip()
        fecha_fabricacion = request.POST.get('fecha_fabricacion', '').strip()
        fecha_vencimiento = request.POST.get('fecha_vencimiento', '').strip()
        cliente_id = request.POST.get('cliente')
        proveedor_id = request.POST.get('proveedor')

        Producto.objects.create(
            nombre_producto=nombre_producto,
            categoria=categoria,
            precio_unitario=precio_unitario,
            stock_actual=stock_actual,
            fecha_fabricacion=fecha_fabricacion or None,
            fecha_vencimiento=fecha_vencimiento or None,
            cliente_id=cliente_id if cliente_id else None,
            proveedor_id=proveedor_id if proveedor_id else None
        )
        return redirect('ver_producto')

    return render(request, 'producto/agregar_producto.html', {
        'clientes': clientes,
        'proveedores': proveedores
    })


def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        producto.nombre_producto = request.POST.get('nombre_producto', producto.nombre_producto).strip()
        producto.categoria = request.POST.get('categoria', producto.categoria).strip()
        producto.precio_unitario = request.POST.get('precio_unitario', producto.precio_unitario)
        producto.stock_actual = request.POST.get('stock_actual', producto.stock_actual)
        producto.fecha_fabricacion = request.POST.get('fecha_fabricacion', producto.fecha_fabricacion)
        producto.fecha_vencimiento = request.POST.get('fecha_vencimiento', producto.fecha_vencimiento)
        producto.cliente_id = request.POST.get('cliente') or None
        producto.proveedor_id = request.POST.get('proveedor') or None
        producto.save()
        return redirect('ver_producto')

    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'clientes': clientes,
        'proveedores': proveedores
    })


def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# ==============================
# EMPLEADO
# ==============================
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        puesto = request.POST.get('puesto', '').strip()
        fecha_contratacion = request.POST.get('fecha_contratacion', '').strip()
        
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            fecha_contratacion=fecha_contratacion
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleado(request):
    empleados = Empleado.objects.all().order_by('-id')
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, empleado_id):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id=empleado_id)
        empleado.nombre = request.POST.get('nombre', empleado.nombre).strip()
        empleado.apellido = request.POST.get('apellido', empleado.apellido).strip()
        empleado.puesto = request.POST.get('puesto', empleado.puesto).strip()
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion', empleado.fecha_contratacion)
        empleado.save()
    return redirect('ver_empleado')

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# ==============================
# FLOTA_PRODUCCION
# ==============================
def agregar_flota(request):
    if request.method == 'POST':
        tipo_transporte = request.POST.get('tipo_transporte', '').strip()
        nombre_transporte = request.POST.get('nombre_transporte', '').strip()
        placas = request.POST.get('placas', '').strip()
        codigo = request.POST.get('codigo', '').strip()
        modelo = request.POST.get('modelo', '').strip()
        
        Flota_produccion.objects.create(
            tipo_transporte=tipo_transporte,
            nombre_transporte=nombre_transporte,
            placas=placas,
            codigo=codigo,
            modelo=modelo
        )
        return redirect('ver_flota')
    return render(request, 'flota/agregar_flota.html')

def ver_flota(request):
    flotas = Flota_produccion.objects.all().order_by('-id')
    return render(request, 'flota/ver_flota.html', {'flotas': flotas})

def actualizar_flota(request, flota_id):
    flota = get_object_or_404(Flota_produccion, id=flota_id)
    return render(request, 'flota/actualizar_flota.html', {'flota': flota})

def realizar_actualizacion_flota(request, flota_id):
    if request.method == 'POST':
        flota = get_object_or_404(Flota_produccion, id=flota_id)
        flota.tipo_transporte = request.POST.get('tipo_transporte', flota.tipo_transporte).strip()
        flota.nombre_transporte = request.POST.get('nombre_transporte', flota.nombre_transporte).strip()
        flota.placas = request.POST.get('placas', flota.placas).strip()
        flota.codigo = request.POST.get('codigo', flota.codigo).strip()
        flota.modelo = request.POST.get('modelo', flota.modelo).strip()
        flota.save()
    return redirect('ver_flota')

def borrar_flota(request, flota_id):
    flota = get_object_or_404(Flota_produccion, id=flota_id)
    if request.method == 'POST':
        flota.delete()
        return redirect('ver_flota')
    return render(request, 'flota/borrar_flota.html', {'flota': flota})


# ==============================
# VENTA
# ==============================
def agregar_venta(request):
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        id_empleado_id = request.POST.get('id_empleado')
        fecha_venta = request.POST.get('fecha_venta', '').strip()
        id_cliente_id = request.POST.get('id_cliente')
        id_producto_id = request.POST.get('id_producto')
        cantidad_vendida = request.POST.get('cantidad_vendida', '').strip()
        monto_total = request.POST.get('monto_total', '').strip()
        
        Venta.objects.create(
            id_empleado_id=id_empleado_id,
            fecha_venta=fecha_venta,
            id_cliente_id=id_cliente_id,
            id_producto_id=id_producto_id,
            cantidad_vendida=cantidad_vendida,
            monto_total=monto_total
        )
        return redirect('ver_venta')
    
    return render(request, 'venta/agregar_venta.html', {
        'empleados': empleados,
        'clientes': clientes,
        'productos': productos
    })

def ver_venta(request):
    ventas = Venta.objects.all().order_by('-fecha_venta', '-id')
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})

def actualizar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'empleados': empleados,
        'clientes': clientes,
        'productos': productos
    })

def realizar_actualizacion_venta(request, venta_id):
    if request.method == 'POST':
        venta = get_object_or_404(Venta, id=venta_id)
        venta.id_empleado_id = request.POST.get('id_empleado', venta.id_empleado_id)
        venta.fecha_venta = request.POST.get('fecha_venta', venta.fecha_venta)
        venta.id_cliente_id = request.POST.get('id_cliente', venta.id_cliente_id)
        venta.id_producto_id = request.POST.get('id_producto', venta.id_producto_id)
        venta.cantidad_vendida = request.POST.get('cantidad_vendida', venta.cantidad_vendida)
        venta.monto_total = request.POST.get('monto_total', venta.monto_total)
        venta.save()
    return redirect('ver_venta')

def borrar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_venta')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})