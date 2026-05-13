#!/usr/bin/env python3
"""
Script para inicializar la base de datos y crear las tablas
"""

from config.database import init_db, test_connection

def main():
    """Inicializa la base de datos completa"""
    print("🚀 Inicializando base de datos del Sistema de Biblioteca...")
    print("=" * 60)
    
    # Probar conexión
    if not test_connection():
        print("❌ No se pudo conectar a la base de datos")
        return False
    
    # Crear tablas
    try:
        init_db()
        print("✅ Tablas creadas exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
        return False

if __name__ == "__main__":
    if main():
        print("\n🎉 Base de datos inicializada correctamente!")
        print("\n📝 Siguientes pasos:")
        print("   1. python sample_data.py  # Cargar datos de ejemplo")
        print("   2. python app.py          # Iniciar aplicación web")
    else:
        print("\n❌ No se pudo inicializar la base de datos")
