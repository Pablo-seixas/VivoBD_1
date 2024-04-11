# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI()

# Incluir rotas do arquivo routes.py
app.include_router(api_router, prefix="/api")

# Definir rota raiz
@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}
