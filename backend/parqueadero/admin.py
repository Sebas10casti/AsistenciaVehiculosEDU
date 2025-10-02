from django.contrib import admin
from .models import Vehiculo, Registro

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_dueno','tipo','placa','area')
    search_fields = ('nombre_dueno','documento','placa')

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id','vehiculo','fecha','hora_entrada','hora_salida')
    list_filter = ('fecha','vehiculo__tipo','vehiculo__area')
