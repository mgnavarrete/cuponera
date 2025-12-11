from django.contrib import admin
from .models import Cupon

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'codigo', 'fecha_expiracion', 'fue_canjeado', 'activo')
    list_filter = ('fue_canjeado', 'activo')
    search_fields = ('titulo', 'codigo')