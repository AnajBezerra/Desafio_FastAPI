from sqlalchemy.orm import Session
import models
import schemas

def create_atleta(db: Session, atleta: schemas.AtletaCreate):
    db_atleta = models.Atleta(**atleta.dict())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

def get_atletas(db: Session, nome: str = None, cpf: str = None):
    query = db.query(models.Atleta)
    if nome:
        query = query.filter(models.Atleta.nome == nome)
    if cpf:
        query = query.filter(models.Atleta.cpf == cpf)
    return query.all()
