from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from config.database import engine
from models import Prestamo, Libro, Usuario
from utils.crud import (
    crear_prestamo, obtener_prestamo, obtener_prestamos, 
    devolver_libro, eliminar_prestamo, buscar_libros_prestados_actualmente,
    usuarios_con_prestamos_vencidos, autor_con_mas_libros,
    obtener_estadisticas_generales, obtener_prestamos_activos_count
)

prestamos_bp = Blueprint('prestamos', __name__, url_prefix='/prestamos')

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@prestamos_bp.route('/')
def lista_prestamos():
    db = SessionLocal()
    try:
        prestamos = obtener_prestamos(db)
        return render_template('prestamos/lista.html', prestamos=prestamos)
    finally:
        db.close()

@prestamos_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_prestamo():
    db = SessionLocal()
    try:
        if request.method == 'POST':
            libro_id = request.form['libro_id']
            usuario_id = request.form['usuario_id']
            dias_prestamo = int(request.form.get('dias_prestamo', 7))
            
            fecha_devolucion = datetime.now().date() + timedelta(days=dias_prestamo)
            
            prestamo = crear_prestamo(db, int(libro_id), int(usuario_id), fecha_devolucion)
            flash('Préstamo registrado exitosamente', 'success')
            return redirect(url_for('prestamos.lista_prestamos'))
        
        libros = db.query(Libro).all()
        usuarios = db.query(Usuario).all()
        return render_template('prestamos/formulario.html', libros=libros, usuarios=usuarios)
    finally:
        db.close()

@prestamos_bp.route('/<int:id>/devolver', methods=['POST'])
def devolver_libro_route(id):
    db = SessionLocal()
    try:
        prestamo = devolver_libro(db, id)
        if prestamo:
            flash('Libro devuelto exitosamente', 'success')
        else:
            flash('No se pudo devolver el libro', 'error')
        return redirect(url_for('prestamos.lista_prestamos'))
    finally:
        db.close()

@prestamos_bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar_prestamo_route(id):
    db = SessionLocal()
    try:
        if eliminar_prestamo(db, id):
            flash('Préstamo eliminado exitosamente', 'success')
        else:
            flash('No se pudo eliminar el préstamo', 'error')
        return redirect(url_for('prestamos.lista_prestamos'))
    finally:
        db.close()

@prestamos_bp.route('/activos')
def prestamos_activos():
    db = SessionLocal()
    try:
        prestamos = buscar_libros_prestados_actualmente(db)
        return render_template('prestamos/activos.html', prestamos=prestamos)
    finally:
        db.close()

@prestamos_bp.route('/vencidos')
def prestamos_vencidos():
    db = SessionLocal()
    try:
        vencidos = usuarios_con_prestamos_vencidos(db)
        return render_template('prestamos/vencidos.html', vencidos=vencidos)
    finally:
        db.close()

@prestamos_bp.route('/reportes')
def reportes():
    db = SessionLocal()
    try:
        autor_mas_libros = autor_con_mas_libros(db)
        vencidos = usuarios_con_prestamos_vencidos(db)
        estadisticas = obtener_estadisticas_generales(db)
        prestamos_activos = obtener_prestamos_activos_count(db)
        
        return render_template('prestamos/reportes.html', 
                             autor_mas_libros=autor_mas_libros, 
                             vencidos=vencidos,
                             estadisticas=estadisticas,
                             prestamos_activos=prestamos_activos)
    finally:
        db.close()
