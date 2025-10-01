# Sistema de Control de Acceso Vehicular

Sistema desarrollado en Django para el control de acceso de vehículos en un parqueadero empresarial.

## 🚀 Características

- **Gestión de Vehículos**: Registro de carros, motos y bicicletas
- **Control de Acceso**: Registro de ingresos y salidas
- **Reportes**: Exportación de datos a Excel
- **API REST**: Integración con frontend
- **Panel de Administración**: Gestión completa desde Django Admin

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

### Opción 1: Script Automático (Recomendado)

```bash
./setup.sh
```

### Opción 2: Instalación Manual

1. **Crear entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

4. **Crear superusuario (opcional):**
```bash
./create_admin.sh
```

## 🚀 Ejecución

### Opción 1: Script de Inicio (Recomendado)

```bash
./start.sh
```

### Opción 2: Manual

1. **Activar entorno virtual:**
```bash
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. **Ejecutar servidor:**
```bash
python manage.py runserver
```

3. **Abrir en el navegador:**
   - Aplicación: http://127.0.0.1:8000
   - Admin: http://127.0.0.1:8000/admin
   - API: http://127.0.0.1:8000/api/

## 📚 API Endpoints

### Vehículos
- `GET /api/vehicles/` - Listar vehículos
- `POST /api/vehicles/` - Crear vehículo
- `GET /api/vehicles/{id}/` - Obtener vehículo
- `PUT /api/vehicles/{id}/` - Actualizar vehículo
- `DELETE /api/vehicles/{id}/` - Eliminar vehículo
- `POST /api/vehicles/{id}/ingreso/` - Registrar ingreso
- `POST /api/vehicles/{id}/salida/` - Registrar salida
- `GET /api/vehicles/{id}/history/` - Historial de accesos

### Registros
- `GET /api/registros/` - Listar registros
- `GET /api/registros/export/` - Exportar a Excel

### Parámetros de consulta
- `?tipo=carro` - Filtrar por tipo de vehículo
- `?desde=2024-01-01` - Filtrar registros desde fecha
- `?hasta=2024-12-31` - Filtrar registros hasta fecha

## 🗄️ Modelos de Datos

### Vehiculo
- `tipo`: Tipo de vehículo (carro, moto, bicicleta)
- `nombre_dueno`: Nombre del propietario
- `documento`: Documento de identidad
- `placa`: Placa del vehículo (opcional)
- `serial`: Serial de bicicleta (opcional)
- `color`: Color del vehículo
- `marca`: Marca del vehículo (opcional)
- `area`: Área de trabajo (producción, administración, logística, soplado)

### Registro
- `vehiculo`: Referencia al vehículo
- `fecha`: Fecha del ingreso
- `hora_entrada`: Timestamp de entrada
- `hora_salida`: Timestamp de salida (opcional)

## 🔧 Configuración

El proyecto está configurado para desarrollo local con:
- Base de datos SQLite
- CORS habilitado para integración con frontend
- Debug activado
- Archivos estáticos configurados

## 📊 Exportación de Datos

El sistema permite exportar registros a Excel con la siguiente información:
- Datos del propietario y vehículo
- Fechas y horas de entrada/salida
- Filtros por rango de fechas

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
