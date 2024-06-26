# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from . import models

def get_atletas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Atleta).offset(skip).limit(limit).all()

def create_atleta(db: Session, atleta: models.Atleta):
    db.add(atleta)
    db.commit()
    db.refresh(atleta)
    return atleta

def get_atleta_by_cpf(db: Session, cpf: str):
    return db.query(models.Atleta).filter(models.Atleta.cpf == cpf).first()

