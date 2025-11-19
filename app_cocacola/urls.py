from django.urls import path
from . import views

urlpatterns = [
    # raíz de la app
    path('', views.inicio_cocacola, name='inicio_cocacola'),

    # CLIENTE (ya existentes)
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_cliente, name='ver_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/actualizar/realizar/<int:cliente_id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),

    # PROVEEDOR
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/actualizar/<int:proveedor_id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/actualizar/realizar/<int:proveedor_id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # PRODUCTOS
    path('ver_producto/', views.ver_producto, name='ver_producto'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('borrar_producto/<int:id>/', views.borrar_producto, name='borrar_producto'),


    # EMPLEADO
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/ver/', views.ver_empleado, name='ver_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/actualizar/realizar/<int:empleado_id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # FLOTA_PRODUCCION
    path('flota/agregar/', views.agregar_flota, name='agregar_flota'),
    path('flota/ver/', views.ver_flota, name='ver_flota'),
    path('flota/actualizar/<int:flota_id>/', views.actualizar_flota, name='actualizar_flota'),
    path('flota/actualizar/realizar/<int:flota_id>/', views.realizar_actualizacion_flota, name='realizar_actualizacion_flota'),
    path('flota/borrar/<int:flota_id>/', views.borrar_flota, name='borrar_flota'),

    # VENTA
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/ver/', views.ver_venta, name='ver_venta'),
    path('venta/actualizar/<int:venta_id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/actualizar/realizar/<int:venta_id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:venta_id>/', views.borrar_venta, name='borrar_venta'),
]
