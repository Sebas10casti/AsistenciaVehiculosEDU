from rest_framework import serializers
from .models import Vehiculo, Registro

class RegistroSerializer(serializers.ModelSerializer):
    nombre_dueno = serializers.CharField(source='vehiculo.nombre_dueno', read_only=True)

    class Meta:
        model = Registro
        fields = ('id','vehiculo','placa','nombre_dueno','fecha','hora_entrada','hora_salida')
        extra_kwargs = {
            'vehiculo': {'required': False}
        }

    def validate(self, data):
        # Solo validar en creación (cuando no hay instancia)
        if not self.instance:
            # Si no se proporciona vehiculo, placa es requerida
            if not data.get('vehiculo') and not data.get('placa'):
                raise serializers.ValidationError("Debe proporcionar 'vehiculo' o 'placa'")
        return data

    def create(self, validated_data):
        placa = validated_data.get('placa')
        if placa and not validated_data.get('vehiculo'):
            try:
                # Buscar vehículo por placa
                vehiculo = Vehiculo.objects.get(placa=placa)
            except Vehiculo.DoesNotExist:
                raise serializers.ValidationError(f"No se encontró un vehículo con placa: {placa}")
            validated_data['vehiculo'] = vehiculo
        return super().create(validated_data)

class VehiculoSerializer(serializers.ModelSerializer):
    active_registro = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = ('id','tipo','nombre_dueno','documento','placa','color','marca','area','active_registro')

    def get_active_registro(self, obj):
        reg = obj.registros.filter(hora_salida__isnull=True).first()
        if not reg:
            return None
        return {
            'id': reg.id,
            'hora_entrada': reg.hora_entrada,
            'fecha': reg.fecha
        }
