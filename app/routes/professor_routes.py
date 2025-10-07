from flask import Blueprint

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/professores')
def listar_professores():
    return {"mensagem": "Lista de professores"}
