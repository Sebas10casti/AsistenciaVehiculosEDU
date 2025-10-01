#!/bin/bash

echo "👤 Creando superusuario para Django Admin"
echo "========================================"

# Activar entorno virtual
source venv/bin/activate

# Crear superusuario
python manage.py createsuperuser

echo ""
echo "✅ Superusuario creado exitosamente"
echo "Ahora puedes acceder al admin en: http://127.0.0.1:8000/admin"
