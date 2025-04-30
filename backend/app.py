from flask import Flask
from backend.extensions import mysql
from backend.admin.routes import admin_bp
from backend.auth.routes import auth_bp
from backend.student.routes import student_bp
from backend.teacher.routes import teacher_bp

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'project_tdah'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.secret_key = "ricardo"

    # Inicializar extensiones
    mysql.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(teacher_bp, url_prefix='/teacher')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)