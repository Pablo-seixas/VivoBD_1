﻿# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
