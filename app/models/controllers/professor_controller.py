from app import db
from app.models.professor import Professor

def get_all_professores():
    return Professor.query.all()

def get_professor_by_id(professor_id):
    return Professor.query.get(professor_id)

def create_professor(data):
    novo = Professor(**data)
    db.session.add(novo)
    db.session.commit()
    return novo

def update_professor(professor_id, data):
    professor = Professor.query.get(professor_id)
    if not professor:
        return None
    for key, value in data.items():
        setattr(professor, key, value)
    db.session.commit()
    return professor

def delete_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        return None
    db.session.delete(professor)
    db.session.commit()
    return True
