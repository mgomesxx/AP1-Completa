from app import ma
from app.models.aluno import Aluno

class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aluno
        load_instance = True
