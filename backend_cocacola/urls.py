from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_cocacola.urls')),  # rutas de la app en la raíz
]