from app import ma
from app.models.turma import Turma

class TurmaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Turma
        load_instance = True
