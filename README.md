# Sistema de Gestión de Biblioteca

Una aplicación web completa para la gestión de bibliotecas utilizando Python, Flask, SQLAlchemy y MySQL.

## 📋 Descripción del Proyecto

Este sistema permite gestionar de manera eficiente:
- **Autores**: Registro y gestión de autores
- **Libros**: Catálogo completo de libros con búsqueda avanzada
- **Usuarios**: Gestión de usuarios registrados
- **Préstamos**: Control completo de préstamos y devoluciones

### Características Principales

- ✅ CRUD completo para todos los modelos
- 🔍 Búsqueda de libros por título, autor o género
- 📚 Gestión de préstamos con control de fechas
- 📊 Reportes y estadísticas avanzadas
- 🌐 Interfaz web moderna con Bootstrap 5
- 🗄️ Base de datos MySQL con SQLAlchemy ORM

## 🏗️ Estructura del Proyecto

```
pytonOrm/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── sample_data.py        # Script para datos de ejemplo
├── README.md             # Este archivo
├── config/
│   ├── __init__.py
│   └── database.py       # Configuración de la base de datos
├── models/
│   ├── __init__.py
│   ├── autor.py         # Modelo Autor
│   ├── libro.py         # Modelo Libro
│   ├── usuario.py       # Modelo Usuario
│   └── prestamo.py      # Modelo Préstamo
├── routes/
│   ├── __init__.py
│   ├── autores.py       # Rutas para autores
│   ├── libros.py        # Rutas para libros
│   ├── usuarios.py      # Rutas para usuarios
│   └── prestamos.py     # Rutas para préstamos
├── templates/
│   ├── base.html        # Plantilla base
│   ├── index.html       # Página principal
│   ├── autores/         # Plantillas de autores
│   ├── libros/          # Plantillas de libros
│   ├── usuarios/        # Plantillas de usuarios
│   └── prestamos/       # Plantillas de préstamos
├── utils/
│   ├── __init__.py
│   └── crud.py          # Operaciones CRUD y búsquedas
└── static/              # Archivos estáticos (CSS, JS, imágenes)
```

## 🛠️ Requisitos Previos

### 1. MySQL Server
Asegúrate de tener MySQL Server instalado y en ejecución.

### 2. Python 3.8+
```bash
python --version
```

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/DaTorresCarrillo/RetoOrm
cd pytonOrm
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos MySQL

#### 4.1 Crear la base de datos
```sql
mysql -u root -p
CREATE DATABASE biblioteca;
EXIT;
```

#### 4.2 Configurar la conexión
La configuración de la base de datos está en `config/database.py`. 
La conexión actual usa:
- **Usuario**: root
- **Contraseña**: perroperro
- **Base de datos**: biblioteca
- **Host**: localhost

Si necesitas cambiar estos valores, edita la línea:
```python
DATABASE_URL = "mysql+pymysql://root:perroperro@localhost/biblioteca"
```

### 5. Inicializar la base de datos
Las tablas se crearán automáticamente al ejecutar la aplicación por primera vez.

### 6. Cargar datos de ejemplo (opcional)
```bash
python sample_data.py
```
Este script creará:
- 3 autores (Gabriel García Márquez, J.K. Rowling, Stephen King)
- 5 libros
- 2 usuarios
- 2 préstamos de ejemplo

## 🏃‍♂️ Ejecutar la Aplicación

### Iniciar el servidor web
```bash
python app.py
```

La aplicación estará disponible en:
- **URL**: http://localhost:5000
- **Host**: 0.0.0.0 (accesible desde la red local)

## 📖 Guía de Uso

### 1. Página Principal
Al acceder a http://localhost:5000 verás el panel principal con acceso a todas las funcionalidades.

### 2. Gestión de Autores
- **Ver lista**: `Autores` en el menú
- **Crear autor**: `Nuevo Autor`
- **Editar/Eliminar**: Botones en la tabla

### 3. Gestión de Libros
- **Ver catálogo**: `Libros` en el menú
- **Buscar libros**: `Buscar` → seleccionar tipo de búsqueda
- **Agregar libro**: `Nuevo Libro`

### 4. Gestión de Usuarios
- **Ver usuarios**: `Usuarios` en el menú
- **Registrar usuario**: `Nuevo Usuario`

### 5. Gestión de Préstamos
- **Ver todos**: `Préstamos` en el menú
- **Préstamos activos**: `Activos`
- **Préstamos vencidos**: `Vencidos`
- **Reportes**: `Reportes` → estadísticas avanzadas

## 🔍 Ejemplos de Búsqueda

### Búsqueda por Título
- Ingresa "Harry" para encontrar todos los libros de Harry Potter

### Búsqueda por Autor
- Ingresa "García" para encontrar libros de Gabriel García Márquez

### Búsqueda por Género
- Ingresa "Fantasía" para encontrar libros de ese género

## 📊 Funcionalidades Avanzadas

### Reportes Disponibles
1. **Autor con más libros**: Muestra el autor que tiene más títulos registrados
2. **Préstamos vencidos**: Lista de usuarios con préstamos fuera de plazo
3. **Préstamos activos**: Todos los préstamos actualmente vigentes

### Consultas SQL Generadas
El sistema genera automáticamente las consultas SQL mediante SQLAlchemy. Puedes ver las consultas en la consola al ejecutar la aplicación (modo debug activado).

## 🔧 Personalización

### Cambiar Contraseña de MySQL
Edita `config/database.py`:
```python
DATABASE_URL = "mysql+pymysql://root:NUEVA_CONTRASEÑA@localhost/biblioteca"
```

### Cambiar Puerto del Servidor
Edita `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Cambiar puerto
```

## 🐛 Solución de Problemas

### Error de Conexión a MySQL
1. Verifica que MySQL esté en ejecución
2. Confirma la contraseña en `config/database.py`
3. Asegúrate de que la base de datos `biblioteca` exista

### Error de Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Error de Puerto en Uso
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

## 📝 Notas Técnicas

- **ORM**: SQLAlchemy 2.0+ con mapeo declarativo
- **Web Framework**: Flask 2.3+
- **Frontend**: Bootstrap 5 + Font Awesome
- **Base de Datos**: MySQL 8.0+
- **Python**: 3.8+

## 👤 Autores

Diego Alejandro Torres Carrillo
Jonhy Sebastian Bejarano Gonzales

## 📄 Licencia

Este proyecto es de uso educativo y puede ser modificado y distribuido libremente.

# RetoOrm
