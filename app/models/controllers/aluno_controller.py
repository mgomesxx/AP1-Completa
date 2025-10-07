from app import db
from app.models.aluno import Aluno

def get_all_alunos():
    return Aluno.query.all()

def get_aluno_by_id(aluno_id):
    return Aluno.query.get(aluno_id)

def create_aluno(data):
    novo = Aluno(**data)
    db.session.add(novo)
    db.session.commit()
    return novo

def update_aluno(aluno_id, data):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return None
    for key, value in data.items():
        setattr(aluno, key, value)
    db.session.commit()
    return aluno

def delete_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return None
    db.session.delete(aluno)
    db.session.commit()
    return True
