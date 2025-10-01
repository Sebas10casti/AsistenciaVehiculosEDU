#!/bin/bash

echo "🚗 Configurando Sistema de Control de Acceso Vehicular"
echo "=================================================="

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado. Por favor instala Python 3.8 o superior."
    exit 1
fi

echo "✅ Python3 encontrado: $(python3 --version)"

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
echo "⬆️ Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar migraciones
echo "🗄️ Ejecutando migraciones de base de datos..."
python manage.py migrate

# Crear superusuario (opcional)
echo "👤 ¿Deseas crear un superusuario? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "🎉 ¡Configuración completada!"
echo ""
echo "Para ejecutar el servidor:"
echo "1. Activa el entorno virtual: source venv/bin/activate"
echo "2. Ejecuta el servidor: python manage.py runserver"
echo "3. Abre tu navegador en: http://127.0.0.1:8000"
echo ""
echo "Endpoints de la API:"
echo "- http://127.0.0.1:8000/api/vehicles/ (Gestión de vehículos)"
echo "- http://127.0.0.1:8000/api/registros/ (Registros de acceso)"
echo "- http://127.0.0.1:8000/admin/ (Panel de administración)"
