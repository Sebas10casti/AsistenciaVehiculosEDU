from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.http import HttpResponse
import pandas as pd
from io import BytesIO
from django.db import transaction

from .models import Vehiculo, Registro
from .serializers import VehiculoSerializer, RegistroSerializer
from rest_framework.permissions import IsAuthenticated

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('nombre_dueno')
    serializer_class = VehiculoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        tipo = self.request.query_params.get('tipo')  # ?tipo=moto
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs

    @action(detail=True, methods=['post'])
    def ingreso(self, request, pk=None):
        veh = self.get_object()
        # evitar crear doble ingreso si ya existe un registro sin salida
        open_reg = veh.registros.filter(hora_salida__isnull=True).first()
        if open_reg:
            return Response({'detail': 'Ya existe un ingreso sin salida para este vehículo.'}, status=status.HTTP_400_BAD_REQUEST)
        reg = Registro.objects.create(vehiculo=veh)  # fecha y hora_entrada automáticos
        return Response(RegistroSerializer(reg).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def salida(self, request, pk=None):
        veh = self.get_object()
        open_reg = veh.registros.filter(hora_salida__isnull=True).first()
        if not open_reg:
            return Response({'detail': 'No hay ingreso pendiente para este vehículo.'}, status=status.HTTP_400_BAD_REQUEST)
        open_reg.hora_salida = timezone.now()
        open_reg.save()
        return Response(RegistroSerializer(open_reg).data)

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        veh = self.get_object()
        regs = [veh.registros.all()]
        serializer = RegistroSerializer(regs, many=True)
        return Response(serializer.data)



class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.select_related('vehiculo').all()
    serializer_class = RegistroSerializer

    @action(detail=False, methods=['post'])
    def registro(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            registro = serializer.save()
            return Response(RegistroSerializer(registro).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def export(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def update_registro(self, request, pk=None):
        """
        Actualiza un registro específico por ID.
        Útil para agregar hora_salida a un registro existente.
        """
        try:
            registro = self.get_object()
            serializer = self.get_serializer(registro, data=request.data, partial=True)
            if serializer.is_valid():
                updated_registro = serializer.save()
                # Refrescar el objeto desde la base de datos para obtener los datos actualizados
                updated_registro.refresh_from_db()
                return Response(RegistroSerializer(updated_registro).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def ultimo_registro(self, request):
        placa = request.query_params.get('placa')
        if not placa:
            return Response({'error': 'Parámetro placa es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Buscar el último registro de la placa que no tenga salida
            registro = Registro.objects.filter(
                placa=placa,
                hora_salida__isnull=True
            ).order_by('-hora_entrada').first()
            
            if not registro:
                return Response({'error': 'No se encontró un registro activo para esta placa'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = RegistroSerializer(registro)
            return Response(serializer.data)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
