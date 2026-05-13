from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from config.database import engine
from models import Usuario
from utils.crud import crear_usuario, obtener_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@usuarios_bp.route('/')
def lista_usuarios():
    db = SessionLocal()
    try:
        usuarios = obtener_usuarios(db)
        return render_template('usuarios/lista.html', usuarios=usuarios)
    finally:
        db.close()

@usuarios_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        db = SessionLocal()
        try:
            nombre = request.form['nombre']
            email = request.form['email']
            telefono = request.form.get('telefono', '')
            
            usuario = crear_usuario(db, nombre, email, telefono)
            flash('Usuario creado exitosamente', 'success')
            return redirect(url_for('usuarios.lista_usuarios'))
        except Exception as e:
            flash(f'Error al crear usuario: {str(e)}', 'error')
            return render_template('usuarios/formulario.html')
        finally:
            db.close()
    
    return render_template('usuarios/formulario.html')

@usuarios_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario(id):
    db = SessionLocal()
    try:
        usuario = obtener_usuario(db, id)
        if not usuario:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('usuarios.lista_usuarios'))
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            telefono = request.form.get('telefono', '')
            
            actualizar_usuario(db, id, nombre=nombre, email=email, telefono=telefono)
            flash('Usuario actualizado exitosamente', 'success')
            return redirect(url_for('usuarios.lista_usuarios'))
        
        return render_template('usuarios/formulario.html', usuario=usuario)
    finally:
        db.close()

@usuarios_bp.route('/<int:id>/eliminar', methods=['POST'])
def eliminar_usuario_route(id):
    db = SessionLocal()
    try:
        if eliminar_usuario(db, id):
            flash('Usuario eliminado exitosamente', 'success')
        else:
            flash('No se pudo eliminar el usuario', 'error')
        return redirect(url_for('usuarios.lista_usuarios'))
    finally:
        db.close()
