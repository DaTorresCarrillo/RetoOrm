from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from config.database import engine
from models import Autor
from utils.crud import crear_autor, obtener_autor, obtener_autores, actualizar_autor, eliminar_autor

autores_bp = Blueprint('autores', __name__, url_prefix='/autores')

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@autores_bp.route('/')
def lista_autores():
    db = SessionLocal()
    try:
        autores = obtener_autores(db)
        return render_template('autores/lista.html', autores=autores)
    finally:
        db.close()

@autores_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_autor():
    if request.method == 'POST':
        db = SessionLocal()
        try:
            nombre = request.form['nombre']
            nacionalidad = request.form.get('nacionalidad', '')
            
            autor = crear_autor(db, nombre, nacionalidad)
            flash('Autor creado exitosamente', 'success')
            return redirect(url_for('autores.lista_autores'))
        except Exception as e:
            flash(f'Error al crear autor: {str(e)}', 'error')
            return render_template('autores/formulario.html')
        finally:
            db.close()
    
    return render_template('autores/formulario.html')

@autores_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_autor(id):
    db = SessionLocal()
    try:
        autor = obtener_autor(db, id)
        if not autor:
            flash('Autor no encontrado', 'error')
            return redirect(url_for('autores.lista_autores'))
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            nacionalidad = request.form.get('nacionalidad', '')
            
            actualizar_autor(db, id, nombre=nombre, nacionalidad=nacionalidad)
            flash('Autor actualizado exitosamente', 'success')
            return redirect(url_for('autores.lista_autores'))
        
        return render_template('autores/formulario.html', autor=autor)
    finally:
        db.close()

@autores_bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar_autor_route(id):
    db = SessionLocal()
    try:
        if eliminar_autor(db, id):
            flash('Autor eliminado exitosamente', 'success')
        else:
            flash('No se pudo eliminar el autor', 'error')
        return redirect(url_for('autores.lista_autores'))
    finally:
        db.close()
