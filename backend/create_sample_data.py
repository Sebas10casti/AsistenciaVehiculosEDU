#!/usr/bin/env python3
"""
Script para crear datos de prueba en el Sistema de Control de Acceso Vehicular
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'control_accesos.settings')
django.setup()

from parqueadero.models import Vehiculo, Registro

def create_sample_vehicles():
    """Crear vehículos de muestra"""
    print("🚗 Creando vehículos de muestra...")
    
    vehicles_data = [
        {
            'tipo': 'carro',
            'nombre_dueno': 'María González',
            'documento': '12345678',
            'placa': 'ABC123',
            'color': 'Azul',
            'marca': 'Toyota Corolla',
            'area': 'produccion'
        },
        {
            'tipo': 'carro',
            'nombre_dueno': 'Carlos Rodríguez',
            'documento': '87654321',
            'placa': 'XYZ789',
            'color': 'Rojo',
            'marca': 'Honda Civic',
            'area': 'administracion'
        },
        {
            'tipo': 'moto',
            'nombre_dueno': 'Ana Martínez',
            'documento': '11223344',
            'placa': 'MOT001',
            'color': 'Negro',
            'marca': 'Yamaha',
            'area': 'logistica'
        },
        {
            'tipo': 'moto',
            'nombre_dueno': 'Luis Pérez',
            'documento': '55667788',
            'placa': 'MOT002',
            'color': 'Verde',
            'marca': 'Honda',
            'area': 'soplado'
        },
        {
            'tipo': 'bicicleta',
            'nombre_dueno': 'Sofia Herrera',
            'documento': '99887766',
            'serial': 'BIC001',
            'color': 'Rosa',
            'marca': 'Trek',
            'area': 'produccion'
        },
        {
            'tipo': 'bicicleta',
            'nombre_dueno': 'Diego Castro',
            'documento': '44332211',
            'serial': 'BIC002',
            'color': 'Amarillo',
            'marca': 'Giant',
            'area': 'logistica'
        }
    ]
    
    created_vehicles = []
    for data in vehicles_data:
        vehicle, created = Vehiculo.objects.get_or_create(
            documento=data['documento'],
            defaults=data
        )
        if created:
            print(f"   ✅ Creado: {vehicle}")
            created_vehicles.append(vehicle)
        else:
            print(f"   ℹ️  Ya existe: {vehicle}")
            created_vehicles.append(vehicle)
    
    return created_vehicles

def create_sample_registros(vehicles):
    """Crear registros de entrada y salida de muestra"""
    print("\n📝 Creando registros de acceso...")
    
    # Crear registros para los últimos 7 días
    for i in range(7):
        date = datetime.now().date() - timedelta(days=i)
        
        for vehicle in vehicles:
            # 70% de probabilidad de que el vehículo haya venido ese día
            if random.random() < 0.7:
                # Hora de entrada aleatoria entre 6:00 y 9:00 AM
                entrada_hour = random.randint(6, 9)
                entrada_minute = random.randint(0, 59)
                hora_entrada = datetime.combine(date, datetime.min.time().replace(hour=entrada_hour, minute=entrada_minute))
                
                # Crear registro de entrada
                registro = Registro.objects.create(
                    vehiculo=vehicle,
                    fecha=date,
                    hora_entrada=hora_entrada
                )
                
                # 90% de probabilidad de que haya salido
                if random.random() < 0.9:
                    # Hora de salida entre 4:00 y 7:00 PM
                    salida_hour = random.randint(16, 19)
                    salida_minute = random.randint(0, 59)
                    hora_salida = datetime.combine(date, datetime.min.time().replace(hour=salida_hour, minute=salida_minute))
                    
                    registro.hora_salida = hora_salida
                    registro.save()
                    
                    print(f"   ✅ {vehicle.nombre_dueno} - {date}: {hora_entrada.strftime('%H:%M')} - {hora_salida.strftime('%H:%M')}")
                else:
                    print(f"   ✅ {vehicle.nombre_dueno} - {date}: {hora_entrada.strftime('%H:%M')} - (Aún en el parqueadero)")

def main():
    print("🎯 Creando datos de muestra para el Sistema de Control de Acceso Vehicular")
    print("=" * 70)
    
    # Crear vehículos
    vehicles = create_sample_vehicles()
    
    # Crear registros
    create_sample_registros(vehicles)
    
    print(f"\n✅ ¡Datos de muestra creados exitosamente!")
    print(f"   📊 Total de vehículos: {Vehiculo.objects.count()}")
    print(f"   📝 Total de registros: {Registro.objects.count()}")
    print(f"   🚗 Vehículos en el parqueadero: {Registro.objects.filter(hora_salida__isnull=True).count()}")
    
    print("\n🌐 Puedes ver los datos en:")
    print("   - API: http://127.0.0.1:8000/api/vehicles/")
    print("   - Admin: http://127.0.0.1:8000/admin/")
    print("   - Registros: http://127.0.0.1:8000/api/registros/")

if __name__ == "__main__":
    main()
