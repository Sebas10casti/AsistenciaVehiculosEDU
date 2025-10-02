# Cambios Necesarios en el Backend desde el Fork

Este documento detalla todos los cambios que se han implementado en el backend del sistema de control de acceso vehicular desde que se hizo el fork del proyecto original.

## 📋 Resumen de la Estructura Actual

### 🗂️ Estructura del Proyecto
```
backend/
├── control_accesos/          # Proyecto principal Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── parqueadero/              # App principal del sistema
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── scripts de configuración
```

## 🏗️ Modelos de Datos Implementados

### 1. Modelo `Vehiculo`
**Ubicación:** `parqueadero/models.py`

**Campos implementados:**
- `tipo`: CharField con opciones (carro, moto, bicicleta)
- `nombre_dueno`: CharField para el nombre del propietario
- `documento`: CharField para número de documento
- `placa`: CharField opcional para vehículos con placa
- `serial`: CharField opcional para bicicletas
- `color`: CharField para el color del vehículo
- `marca`: CharField opcional para la marca
- `area`: CharField con opciones (producción, administración, logística, soplado)
- `created_at`: DateTimeField automático

**Características especiales:**
- Método `__str__` personalizado que muestra dueño, tipo e identificación
- Relación uno-a-muchos con el modelo Registro

### 2. Modelo `Registro`
**Ubicación:** `parqueadero/models.py`

**Campos implementados:**
- `vehiculo`: ForeignKey hacia Vehiculo
- `fecha`: DateField automático para el día
- `hora_entrada`: DateTimeField automático
- `hora_salida`: DateTimeField opcional

**Características especiales:**
- Ordenamiento por hora_entrada descendente
- Método `__str__` personalizado

## 🔌 API REST Implementada

### Endpoints Disponibles

#### 1. Gestión de Vehículos
- **GET** `/api/vehicles/` - Listar todos los vehículos
- **POST** `/api/vehicles/` - Crear nuevo vehículo
- **GET** `/api/vehicles/{id}/` - Obtener vehículo específico
- **PUT/PATCH** `/api/vehicles/{id}/` - Actualizar vehículo
- **DELETE** `/api/vehicles/{id}/` - Eliminar vehículo

#### 2. Acciones Especiales de Vehículos
- **POST** `/api/vehicles/{id}/ingreso/` - Registrar ingreso de vehículo
- **POST** `/api/vehicles/{id}/salida/` - Registrar salida de vehículo
- **GET** `/api/vehicles/{id}/history/` - Obtener historial de registros

#### 3. Gestión de Registros
- **GET** `/api/registros/` - Listar todos los registros
- **GET** `/api/registros/{id}/` - Obtener registro específico
- **GET** `/api/registros/export/` - Exportar registros a Excel

### Filtros Implementados
- **Por tipo de vehículo:** `?tipo=carro|moto|bicicleta`
- **Por rango de fechas:** `?desde=YYYY-MM-DD&hasta=YYYY-MM-DD`

## 📊 Serializers Implementados

### 1. VehiculoSerializer
**Ubicación:** `parqueadero/serializers.py`

**Campos incluidos:**
- Todos los campos del modelo Vehiculo
- `active_registro`: Campo calculado que muestra el registro activo (sin salida)

### 2. RegistroSerializer
**Ubicación:** `parqueadero/serializers.py`

**Campos incluidos:**
- Campos del modelo Registro
- `dueño`: Nombre del dueño del vehículo (campo calculado)
- `placa_or_serial`: Placa o serial del vehículo (campo calculado)

## ⚙️ Configuración del Proyecto

### Settings Implementados
**Archivo:** `control_accesos/settings.py`

### Apps Instaladas
- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`
- `corsheaders` - Para CORS con frontend Angular
- `parqueadero` - App principal
- `rest_framework` - Para API REST

### Middleware Configurado
- CORS middleware para comunicación con frontend
- Middleware de seguridad estándar de Django
- Middleware de sesiones y autenticación

### Configuración CORS
```python
CORS_ALLOW_ALL_ORIGINS = True  # Para desarrollo
```

### Configuración REST Framework
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
}
```

## 📦 Dependencias Instaladas

**Archivo:** `requirements.txt`

```
Django==4.2.25
djangorestframework==3.15.2
pandas==1.5.3
numpy==1.24.3
openpyxl==3.1.2
django-cors-headers==4.3.1
requests==2.31.0
```

## 🚀 Funcionalidades Especiales Implementadas

### 1. Control de Ingreso/Salida
- **Validación de doble ingreso:** Previene crear múltiples registros de ingreso sin salida
- **Validación de salida sin ingreso:** Previene registrar salida sin ingreso previo
- **Timestamps automáticos:** Fecha y hora se registran automáticamente

### 2. Exportación de Datos
- **Formato Excel:** Exportación de registros a archivo .xlsx
- **Filtros por fecha:** Posibilidad de exportar registros por rango de fechas
- **Datos completos:** Incluye información del vehículo y registros

### 3. API REST Completa
- **ViewSets:** Implementación con ModelViewSet para CRUD completo
- **Acciones personalizadas:** Endpoints especiales para ingreso/salida
- **Filtros:** Búsqueda por tipo de vehículo
- **Paginación:** Manejo automático de grandes volúmenes de datos

## 🔧 Scripts de Configuración

### Scripts Disponibles
- `setup.sh` - Configuración inicial del proyecto
- `start.sh` - Inicio del servidor de desarrollo
- `create_admin.sh` - Creación de usuario administrador
- `create_sample_data.py` - Datos de prueba
- `test_api.py` - Pruebas de la API

## 📝 Migraciones de Base de Datos

### Migración Inicial
**Archivo:** `parqueadero/migrations/0001_initial.py`

**Tablas creadas:**
- `parqueadero_vehiculo` - Tabla de vehículos
- `parqueadero_registro` - Tabla de registros de ingreso/salida

## 🎯 Endpoints de la API

### Base URL: `http://localhost:8000/api/`

#### Vehículos
```
GET    /vehicles/                    # Listar vehículos
POST   /vehicles/                    # Crear vehículo
GET    /vehicles/{id}/               # Obtener vehículo
PUT    /vehicles/{id}/               # Actualizar vehículo
PATCH  /vehicles/{id}/               # Actualización parcial
DELETE /vehicles/{id}/               # Eliminar vehículo
POST   /vehicles/{id}/ingreso/       # Registrar ingreso
POST   /vehicles/{id}/salida/        # Registrar salida
GET    /vehicles/{id}/history/       # Historial del vehículo
```

#### Registros
```
GET    /registros/                   # Listar registros
GET    /registros/{id}/              # Obtener registro
GET    /registros/export/            # Exportar a Excel
```

## 🔒 Consideraciones de Seguridad

### Configuración Actual (Desarrollo)
- `DEBUG = True` - Solo para desarrollo
- `CORS_ALLOW_ALL_ORIGINS = True` - Solo para desarrollo
- `SECRET_KEY` expuesta - Solo para desarrollo

### Para Producción (Cambios Necesarios)
- Cambiar `DEBUG = False`
- Configurar `ALLOWED_HOSTS` específicos
- Configurar CORS específico para dominios de producción
- Usar variables de entorno para `SECRET_KEY`
- Configurar HTTPS
- Implementar autenticación si es necesario

## 📈 Próximos Pasos Recomendados

1. **Configuración de Producción**
   - Variables de entorno
   - Configuración de base de datos de producción
   - Configuración de CORS específica

2. **Autenticación y Autorización**
   - Implementar sistema de usuarios
   - Configurar permisos específicos
   - Autenticación JWT o similar

3. **Validaciones Adicionales**
   - Validación de documentos únicos
   - Validación de placas únicas
   - Validaciones de negocio específicas

4. **Funcionalidades Adicionales**
   - Reportes avanzados
   - Notificaciones
   - Dashboard de estadísticas
   - Integración con sistemas externos

---

**Fecha de creación:** $(date)
**Versión del documento:** 1.0
**Autor:** Sistema de Control de Acceso Vehicular
