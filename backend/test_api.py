#!/usr/bin/env python3
"""
Script de prueba para la API del Sistema de Control de Acceso Vehicular
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

def test_api():
    print("🧪 Probando API del Sistema de Control de Acceso Vehicular")
    print("=" * 60)
    
    # Probar endpoint de vehículos
    print("\n1. Probando endpoint de vehículos...")
    try:
        response = requests.get(f"{BASE_URL}/vehicles/")
        print(f"   Status: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Probar endpoint de registros
    print("\n2. Probando endpoint de registros...")
    try:
        response = requests.get(f"{BASE_URL}/registros/")
        print(f"   Status: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Crear un vehículo de prueba
    print("\n3. Creando vehículo de prueba...")
    vehiculo_data = {
        "tipo": "carro",
        "nombre_dueno": "Juan Pérez",
        "documento": "12345678",
        "placa": "ABC123",
        "color": "Azul",
        "marca": "Toyota",
        "area": "produccion"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/vehicles/", json=vehiculo_data)
        print(f"   Status: {response.status_code}")
        if response.status_code == 201:
            vehiculo = response.json()
            print(f"   Vehículo creado: {vehiculo}")
            
            # Probar ingreso
            print("\n4. Probando ingreso del vehículo...")
            response = requests.post(f"{BASE_URL}/vehicles/{vehiculo['id']}/ingreso/")
            print(f"   Status: {response.status_code}")
            if response.status_code == 201:
                print(f"   Ingreso registrado: {response.json()}")
            
            # Probar salida
            print("\n5. Probando salida del vehículo...")
            response = requests.post(f"{BASE_URL}/vehicles/{vehiculo['id']}/salida/")
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                print(f"   Salida registrada: {response.json()}")
        
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n✅ Pruebas completadas")

if __name__ == "__main__":
    test_api()
