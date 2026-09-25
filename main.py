from fastapi import FastAPI, HTTPException, status, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
import schemas

app = FastAPI(
    title = "API de consulta a código de municipios"
)

@app.get("/")
def home():
    return {"Message":"API de conulta à códigos de municipios"}

@app.get("/municipio/codigo/{codigo}")
async def buscar_municipios_codigo(codigo:str, db:Session=Depends(get_db)):
    codigos = (
        db.query(models.MUNICIPIOS)
        .filter(models.MUNICIPIOS.codigo == codigo)
        .all()
    )
    
    if not codigos:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f'{codigo} não foi encontrado.',
        )
    return codigos

@app.get("/municipio/descricao/{descricao}")
async def buscar_municipios_descricao(descricao:str, db:Session=Depends(get_db)):
    descricoes = (
        db.query(models.MUNICIPIOS)
        .filter(models.MUNICIPIOS.descricao.ilike(f'%{descricao}%'))
        .all()
    )
    
    if not descricoes:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f'{descricao} não foi encontrado.',
        )
    return descricoes
