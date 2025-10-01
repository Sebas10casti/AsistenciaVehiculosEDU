from rest_framework import serializers
from .models import Vehiculo, Registro

class RegistroSerializer(serializers.ModelSerializer):
    dueño = serializers.CharField(source='vehiculo.nombre_dueno', read_only=True)
    placa_or_serial = serializers.SerializerMethodField()

    class Meta:
        model = Registro
        fields = ('id','vehiculo','dueño','placa_or_serial','fecha','hora_entrada','hora_salida')

    def get_placa_or_serial(self, obj):
        return obj.vehiculo.placa or obj.vehiculo.serial or ''

class VehiculoSerializer(serializers.ModelSerializer):
    active_registro = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = ('id','tipo','nombre_dueno','documento','placa','serial','color','marca','area','active_registro')

    def get_active_registro(self, obj):
        reg = obj.registros.filter(hora_salida__isnull=True).first()
        if not reg:
            return None
        return {
            'id': reg.id,
            'hora_entrada': reg.hora_entrada,
            'fecha': reg.fecha
        }
