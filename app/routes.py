# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, database

router = APIRouter()

@router.post("/atletas/", response_model=models.Atleta)
def create_atleta(atleta: models.Atleta, db: Session = Depends(database.SessionLocal)):
    db_atleta = crud.get_atleta_by_cpf(db, cpf=atleta.cpf)
    if db_atleta:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    return crud.create_atleta(db=db, atleta=atleta)

@router.get("/atletas/", response_model=List[models.Atleta])
def read_atletas(skip: int = 0, limit: int = 10, db: Session = Depends(database.SessionLocal)):
    atletas = crud.get_atletas(db, skip=skip, limit=limit)
    return atletas

from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")
