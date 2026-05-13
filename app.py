from flask import Flask, render_template, redirect, url_for
from routes.autores import autores_bp
from routes.libros import libros_bp
from routes.usuarios import usuarios_bp
from routes.prestamos import prestamos_bp
from config.database import init_db, test_connection

def create_app():
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta_aqui'
    
    # Registrar blueprints
    app.register_blueprint(autores_bp)
    app.register_blueprint(libros_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(prestamos_bp)
    
    # Ruta principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Inicializar la base de datos
    with app.app_context():
        if test_connection():
            init_db()
        else:
            print("No se pudo conectar a la base de datos")
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
