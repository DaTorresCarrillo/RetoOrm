from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func
from models import Autor, Libro, Usuario, Prestamo
from typing import List, Optional, Dict, Any
from datetime import datetime, date

# CRUD para Autores
def crear_autor(db: Session, nombre: str, nacionalidad: str = None) -> Autor:
    autor = Autor(nombre=nombre, nacionalidad=nacionalidad)
    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor

def obtener_autor(db: Session, autor_id: int) -> Optional[Autor]:
    return db.query(Autor).filter(Autor.id == autor_id).first()

def obtener_autores(db: Session, skip: int = 0, limit: int = 100) -> List[Autor]:
    return db.query(Autor).offset(skip).limit(limit).all()

def actualizar_autor(db: Session, autor_id: int, **kwargs) -> Optional[Autor]:
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        for key, value in kwargs.items():
            if hasattr(autor, key):
                setattr(autor, key, value)
        db.commit()
        db.refresh(autor)
    return autor

def eliminar_autor(db: Session, autor_id: int) -> bool:
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        db.delete(autor)
        db.commit()
        return True
    return False

# CRUD para Libros
def crear_libro(db: Session, titulo: str, autor_id: int, genero: str = None, año_publicacion: int = None) -> Libro:
    libro = Libro(titulo=titulo, autor_id=autor_id, genero=genero, año_publicacion=año_publicacion)
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro

def obtener_libro(db: Session, libro_id: int) -> Optional[Libro]:
    return db.query(Libro).filter(Libro.id == libro_id).first()

def obtener_libros(db: Session, skip: int = 0, limit: int = 100) -> List[Libro]:
    return db.query(Libro).offset(skip).limit(limit).all()

def actualizar_libro(db: Session, libro_id: int, **kwargs) -> Optional[Libro]:
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        for key, value in kwargs.items():
            if hasattr(libro, key):
                setattr(libro, key, value)
        db.commit()
        db.refresh(libro)
    return libro

def eliminar_libro(db: Session, libro_id: int) -> bool:
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
        return True
    return False

# CRUD para Usuarios
def crear_usuario(db: Session, nombre: str, email: str, telefono: str = None) -> Usuario:
    usuario = Usuario(nombre=nombre, email=email, telefono=telefono)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def obtener_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuarios(db: Session, skip: int = 0, limit: int = 100) -> List[Usuario]:
    return db.query(Usuario).offset(skip).limit(limit).all()

def actualizar_usuario(db: Session, usuario_id: int, **kwargs) -> Optional[Usuario]:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        for key, value in kwargs.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)
        db.commit()
        db.refresh(usuario)
    return usuario

def eliminar_usuario(db: Session, usuario_id: int) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False

# CRUD para Préstamos
def crear_prestamo(db: Session, libro_id: int, usuario_id: int, fecha_devolucion: date) -> Prestamo:
    prestamo = Prestamo(
        libro_id=libro_id,
        usuario_id=usuario_id,
        fecha_prestamo=date.today(),
        fecha_devolucion=fecha_devolucion
    )
    db.add(prestamo)
    db.commit()
    db.refresh(prestamo)
    return prestamo

def obtener_prestamo(db: Session, prestamo_id: int) -> Optional[Prestamo]:
    return db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()

def obtener_prestamos(db: Session, skip: int = 0, limit: int = 100) -> List[Prestamo]:
    return db.query(Prestamo).offset(skip).limit(limit).all()

def devolver_libro(db: Session, prestamo_id: int) -> Optional[Prestamo]:
    prestamo = db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()
    if prestamo and not prestamo.devuelto:
        prestamo.fecha_entrega = date.today()
        db.commit()
        db.refresh(prestamo)
    return prestamo

def eliminar_prestamo(db: Session, prestamo_id: int) -> bool:
    prestamo = db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()
    if prestamo:
        db.delete(prestamo)
        db.commit()
        return True
    return False

# Funciones de búsqueda
def buscar_libros_por_titulo(db: Session, titulo: str) -> List[Libro]:
    return db.query(Libro).filter(Libro.titulo.ilike(f"%{titulo}%")).all()

def buscar_libros_por_autor(db: Session, nombre_autor: str) -> List[Libro]:
    return db.query(Libro).join(Autor).filter(Autor.nombre.ilike(f"%{nombre_autor}%")).all()

def buscar_libros_por_genero(db: Session, genero: str) -> List[Libro]:
    return db.query(Libro).filter(Libro.genero.ilike(f"%{genero}%")).all()

def buscar_libros_prestados_actualmente(db: Session) -> List[Prestamo]:
    return db.query(Prestamo).filter(Prestamo.fecha_entrega.is_(None)).all()

# Consultas avanzadas
def autor_con_mas_libros(db: Session) -> Optional[Dict[str, Any]]:
    resultado = db.query(
        Autor.nombre,
        func.count(Libro.id).label('cantidad_libros')
    ).join(Libro).group_by(Autor.id).order_by(func.count(Libro.id).desc()).first()
    
    if resultado:
        return {
            'nombre': resultado.nombre,
            'cantidad_libros': resultado.cantidad_libros
        }
    return None

def usuarios_con_prestamos_vencidos(db: Session) -> List[Dict[str, Any]]:
    prestamos_vencidos = db.query(Prestamo).filter(
        and_(
            Prestamo.fecha_entrega.is_(None),
            Prestamo.fecha_devolucion < date.today()
        )
    ).all()
    
    return [
        {
            'usuario_id': prestamo.usuario_id,
            'usuario_nombre': prestamo.usuario.nombre,
            'libro_titulo': prestamo.libro.titulo,
            'fecha_devolucion': prestamo.fecha_devolucion.isoformat(),
            'dias_vencido': (date.today() - prestamo.fecha_devolucion).days
        }
        for prestamo in prestamos_vencidos
    ]
