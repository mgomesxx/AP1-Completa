from flask import Blueprint

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas')
def listar_turmas():
    return {"mensagem": "Lista de turmas"}
