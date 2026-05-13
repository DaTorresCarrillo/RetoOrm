#!/usr/bin/env python3
"""
Script para crear datos de ejemplo en la base de datos de la biblioteca.
Este script inserta 3 autores, 5 libros, 2 usuarios y 2 préstamos de ejemplo.
"""

from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from config.database import engine
from utils.crud import (
    crear_autor, crear_libro, crear_usuario, crear_prestamo,
    buscar_libros_por_titulo, buscar_libros_por_autor
)

def crear_datos_ejemplo():
    """Crea datos de ejemplo para demostrar el sistema."""
    
    # Crear sesión de base de datos
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        print("🚀 Creando datos de ejemplo para la biblioteca...")
        
        # 1. Insertar 3 autores
        print("\n📝 Creando autores...")
        autor1 = crear_autor(db, "Gabriel García Márquez", "Colombiana")
        autor2 = crear_autor(db, "J.K. Rowling", "Británica")
        autor3 = crear_autor(db, "Stephen King", "Estadounidense")
        
        print(f"✅ Autores creados: {autor1.nombre}, {autor2.nombre}, {autor3.nombre}")
        
        # 2. Insertar 5 libros
        print("\n📚 Creando libros...")
        libro1 = crear_libro(db, "Cien años de soledad", autor1.id, "Realismo mágico", 1967)
        libro2 = crear_libro(db, "El amor en los tiempos del cólera", autor1.id, "Novela romántica", 1985)
        libro3 = crear_libro(db, "Harry Potter y la piedra filosofal", autor2.id, "Fantasía", 1997)
        libro4 = crear_libro(db, "Harry Potter y el prisionero de Azkaban", autor2.id, "Fantasía", 1999)
        libro5 = crear_libro(db, "El resplandor", autor3.id, "Terror", 1977)
        
        print(f"✅ Libros creados: {libro1.titulo}, {libro2.titulo}, {libro3.titulo}, {libro4.titulo}, {libro5.titulo}")
        
        # 3. Insertar 2 usuarios
        print("\n👥 Creando usuarios...")
        usuario1 = crear_usuario(db, "Ana Martínez", "ana.martinez@email.com", "555-1234")
        usuario2 = crear_usuario(db, "Carlos López", "carlos.lopez@email.com", "555-5678")
        
        print(f"✅ Usuarios creados: {usuario1.nombre}, {usuario2.nombre}")
        
        # 4. Registrar 2 préstamos
        print("\n📖 Registrando préstamos...")
        
        # Préstamo 1: Ana Martínez toma "Cien años de soledad" por 7 días
        prestamo1 = crear_prestamo(
            db, 
            libro1.id, 
            usuario1.id, 
            datetime.now().date() + timedelta(days=7)
        )
        
        # Préstamo 2: Carlos López toma "Harry Potter y la piedra filosofal" por 14 días
        prestamo2 = crear_prestamo(
            db, 
            libro3.id, 
            usuario2.id, 
            datetime.now().date() + timedelta(days=14)
        )
        
        print(f"✅ Préstamos registrados:")
        print(f"   - {usuario1.nombre} tomó '{libro1.titulo}' (Devuelve: {prestamo1.fecha_devolucion})")
        print(f"   - {usuario2.nombre} tomó '{libro3.titulo}' (Devuelve: {prestamo2.fecha_devolucion})")
        
        # 5. Ejecutar búsquedas de ejemplo
        print("\n🔍 Ejecutando búsquedas de ejemplo...")
        
        # Búsqueda por título
        libros_titulo = buscar_libros_por_titulo(db, "Harry")
        print(f"📖 Libros encontrados por título 'Harry': {len(libros_titulo)} libros")
        for libro in libros_titulo:
            print(f"   - {libro.titulo} ({libro.autor.nombre})")
        
        # Búsqueda por autor
        libros_autor = buscar_libros_por_autor(db, "García")
        print(f"👤 Libros encontrados por autor 'García': {len(libros_autor)} libros")
        for libro in libros_autor:
            print(f"   - {libro.titulo} ({libro.año_publicacion})")
        
        print("\n🎉 ¡Datos de ejemplo creados exitosamente!")
        print("\n📊 Resumen:")
        print(f"   - Autores: 3")
        print(f"   - Libros: 5")
        print(f"   - Usuarios: 2")
        print(f"   - Préstamos: 2")
        
    except Exception as e:
        print(f"❌ Error al crear datos de ejemplo: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    crear_datos_ejemplo()
