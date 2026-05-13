from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import os

# Configuración de la base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:perroperro@localhost/biblioteca"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Función para inicializar la base de datos
def init_db():
    try:
        # Crear todas las tablas
        Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente")
    except SQLAlchemyError as e:
        print(f"Error al inicializar la base de datos: {e}")
        raise

# Función para probar la conexión
def test_connection():
    try:
        with engine.connect() as connection:
            from sqlalchemy import text
            result = connection.execute(text("SELECT 1"))
            print("Conexión a la base de datos exitosa")
            return True
    except SQLAlchemyError as e:
        print(f"Error de conexión a la base de datos: {e}")
        return False
