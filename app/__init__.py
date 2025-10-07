from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa extensões
    db.init_app(app)
    ma.init_app(app)

    # Importa e registra rotas
    from app.routes.professor_routes import professor_bp
    from app.routes.turma_routes import turma_bp
    from app.routes.aluno_routes import aluno_bp

    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)

    return app
