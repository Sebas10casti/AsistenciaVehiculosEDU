from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.http import HttpResponse
import pandas as pd
from io import BytesIO

from .models import Vehiculo, Registro
from .serializers import VehiculoSerializer, RegistroSerializer
from rest_framework.permissions import IsAuthenticated

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('nombre_dueno')
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

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
        regs = veh.registros.all()
        serializer = RegistroSerializer(regs, many=True)
        return Response(serializer.data)


class RegistroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Registro.objects.select_related('vehiculo').all()
    serializer_class = RegistroSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def export(self, request):
        qs = self.get_queryset()
        desde = request.query_params.get('desde')  # opcional
        hasta = request.query_params.get('hasta')
        if desde:
            qs = qs.filter(fecha__gte=desde)
        if hasta:
            qs = qs.filter(fecha__lte=hasta)

        rows = []
        for r in qs:
            rows.append({
                'dueño': r.vehiculo.nombre_dueno,
                'documento': r.vehiculo.documento,
                'tipo': r.vehiculo.tipo,
                'placa_o_serial': r.vehiculo.placa or r.vehiculo.serial or '',
                'color': r.vehiculo.color,
                'marca': r.vehiculo.marca,
                'area': r.vehiculo.area,
                'fecha': r.fecha.strftime('%Y-%m-%d'),
                'hora_entrada': r.hora_entrada.strftime('%Y-%m-%d %H:%M:%S'),
                'hora_salida': r.hora_salida.strftime('%Y-%m-%d %H:%M:%S') if r.hora_salida else ''
            })

        df = pd.DataFrame(rows)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Registros')
        output.seek(0)
        resp = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        resp['Content-Disposition'] = 'attachment; filename=registros.xlsx'
        return resp
