from app import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    alunos = db.relationship('Aluno', backref='turma', lazy=True)
