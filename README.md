# Sistema de Gestión de Biblioteca

**Autores:** Diego Alejandro Torres Carrillo y Jonhy Sebastian Bejarano Gonzales

## Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Crear base de datos MySQL
```sql
CREATE DATABASE biblioteca;
```

### 3. Inicializar base de datos
```bash
python init_database.py
```

### 4. Cargar datos de ejemplo (opcional)
```bash
python sample_data.py
```

## Iniciar Aplicación

```bash
python app.py
```

Acceder a: http://localhost:5000

## Funcionalidades

- ✅ CRUD completo para Autores, Libros, Usuarios y Préstamos
- 🔍 Búsqueda de libros por título, autor y género
- 📊 Reportes y estadísticas en tiempo real
- 🌐 Interfaz web moderna con Bootstrap 5

## Datos de Ejemplo

El sistema incluye:
- 3 autores (Gabriel García Márquez, J.K. Rowling, Stephen King)
- 5 libros
- 2 usuarios
- 2 préstamos activos

## Estructura del Proyecto

```
pytonOrm/
├── app.py              # Aplicación Flask principal
├── requirements.txt     # Dependencias
├── config/            # Configuración de base de datos
├── models/            # Modelos SQLAlchemy
├── routes/            # Rutas Flask
├── templates/         # Plantillas HTML
├── utils/             # Operaciones CRUD
└── database_schema.sql # Script SQL generado
```

## Tecnologías

- **Backend**: Python 3.8+, Flask, SQLAlchemy
- **Base de datos**: MySQL
- **Frontend**: Bootstrap 5, HTML5
- **ORM**: SQLAlchemy 2.0+

**Proyecto entregado como requisito del reto de programación.**
