from flask import Blueprint

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/alunos')
def listar_alunos():
    return {"mensagem": "Lista de alunos"}
