#!/usr/bin/env python3
"""
Script para crear la base de datos MySQL 'biblioteca'
"""

import pymysql
import sys

def create_database():
    """Crea la base de datos si no existe"""
    try:
        # Conectarse a MySQL sin especificar base de datos
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='perroperro',
            charset='utf8mb4'
        )
        
        print("🔗 Conectado a MySQL exitosamente")
        
        with connection.cursor() as cursor:
            # Crear la base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✅ Base de datos 'biblioteca' creada exitosamente")
            
            # Verificar que la base de datos existe
            cursor.execute("SHOW DATABASES LIKE 'biblioteca'")
            result = cursor.fetchone()
            
            if result:
                print("🎉 Base de datos 'biblioteca' verificada y lista para usar")
            else:
                print("❌ Error: No se pudo crear la base de datos")
                return False
                
    except pymysql.Error as e:
        print(f"❌ Error de MySQL: {e}")
        print("\n🔧 Soluciones posibles:")
        print("1. Verifica que MySQL esté instalado y en ejecución")
        print("2. Verifica que el usuario 'root' exista con la contraseña 'perroperro'")
        print("3. Verifica que el usuario tenga permisos para crear bases de datos")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
        
    finally:
        if 'connection' in locals():
            connection.close()
            print("🔌 Conexión cerrada")
    
    return True

if __name__ == "__main__":
    print("🚀 Creando base de datos para el Sistema de Biblioteca...")
    print("=" * 50)
    
    if create_database():
        print("\n✨ ¡Base de datos lista! Ahora puedes ejecutar:")
        print("   python sample_data.py  # Para cargar datos de ejemplo")
        print("   python app.py          # Para iniciar la aplicación web")
    else:
        print("\n❌ No se pudo crear la base de datos. Revisa los errores above.")
        sys.exit(1)
