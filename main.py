from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import add_pagination, Page, paginate
from database import SessionLocal, engine
import models
import schemas
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/atletas/", response_model=schemas.Atleta)
def create_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_atleta(db=db, atleta=atleta)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
                            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")

@app.get("/atletas/", response_model=Page[schemas.Atleta])
def read_atletas(nome: str = None, cpf: str = None, db: Session = Depends(get_db)):
    atletas = crud.get_atletas(db, nome=nome, cpf=cpf)
    return paginate(atletas)

add_pagination(app)

