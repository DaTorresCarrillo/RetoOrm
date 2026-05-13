from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from config.database import engine
from models import Libro, Autor
from utils.crud import crear_libro, obtener_libro, obtener_libros, actualizar_libro, eliminar_libro

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@libros_bp.route('/')
def lista_libros():
    db = SessionLocal()
    try:
        libros = obtener_libros(db)
        return render_template('libros/lista.html', libros=libros)
    finally:
        db.close()

@libros_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_libro():
    db = SessionLocal()
    try:
        if request.method == 'POST':
            titulo = request.form['titulo']
            autor_id = request.form['autor_id']
            genero = request.form.get('genero', '')
            año_publicacion = request.form.get('año_publicacion', '')
            
            libro = crear_libro(
                db, titulo, int(autor_id), genero, 
                int(año_publicacion) if año_publicacion else None
            )
            flash('Libro creado exitosamente', 'success')
            return redirect(url_for('libros.lista_libros'))
        
        autores = db.query(Autor).all()
        return render_template('libros/formulario.html', autores=autores)
    finally:
        db.close()

@libros_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_libro(id):
    db = SessionLocal()
    try:
        libro = obtener_libro(db, id)
        if not libro:
            flash('Libro no encontrado', 'error')
            return redirect(url_for('libros.lista_libros'))
        
        if request.method == 'POST':
            titulo = request.form['titulo']
            autor_id = request.form['autor_id']
            genero = request.form.get('genero', '')
            año_publicacion = request.form.get('año_publicacion', '')
            
            actualizar_libro(
                db, id, titulo=titulo, autor_id=int(autor_id), 
                genero=genero, 
                año_publicacion=int(año_publicacion) if año_publicacion else None
            )
            flash('Libro actualizado exitosamente', 'success')
            return redirect(url_for('libros.lista_libros'))
        
        autores = db.query(Autor).all()
        return render_template('libros/formulario.html', libro=libro, autores=autores)
    finally:
        db.close()

@libros_bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar_libro_route(id):
    db = SessionLocal()
    try:
        if eliminar_libro(db, id):
            flash('Libro eliminado exitosamente', 'success')
        else:
            flash('No se pudo eliminar el libro', 'error')
        return redirect(url_for('libros.lista_libros'))
    finally:
        db.close()

@libros_bp.route('/buscar', methods=['GET', 'POST'])
def buscar_libros():
    db = SessionLocal()
    try:
        if request.method == 'POST':
            tipo_busqueda = request.form['tipo_busqueda']
            termino = request.form['termino']
            
            if tipo_busqueda == 'titulo':
                from utils.crud import buscar_libros_por_titulo
                libros = buscar_libros_por_titulo(db, termino)
            elif tipo_busqueda == 'autor':
                from utils.crud import buscar_libros_por_autor
                libros = buscar_libros_por_autor(db, termino)
            elif tipo_busqueda == 'genero':
                from utils.crud import buscar_libros_por_genero
                libros = buscar_libros_por_genero(db, termino)
            else:
                libros = []
            
            return render_template('libros/busqueda.html', libros=libros, 
                                 tipo_busqueda=tipo_busqueda, termino=termino)
        
        return render_template('libros/busqueda.html')
    finally:
        db.close()
