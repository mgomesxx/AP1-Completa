from app import db
from app.models.turma import Turma

def get_all_turmas():
    return Turma.query.all()

def get_turma_by_id(turma_id):
    return Turma.query.get(turma_id)

def create_turma(data):
    nova = Turma(**data)
    db.session.add(nova)
    db.session.commit()
    return nova

def update_turma(turma_id, data):
    turma = Turma.query.get(turma_id)
    if not turma:
        return None
    for key, value in data.items():
        setattr(turma, key, value)
    db.session.commit()
    return turma

def delete_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        return None
    db.session.delete(turma)
    db.session.commit()
    return True
