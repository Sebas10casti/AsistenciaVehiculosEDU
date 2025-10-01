#!/bin/bash

echo "🚗 Iniciando Sistema de Control de Acceso Vehicular"
echo "================================================="

# Activar entorno virtual
source venv/bin/activate

# Ejecutar servidor
echo "🌐 Iniciando servidor en http://127.0.0.1:8000"
echo "Presiona Ctrl+C para detener el servidor"
echo ""

python manage.py runserver
