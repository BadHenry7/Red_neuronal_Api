from fastapi import APIRouter, HTTPException
from app.controllers.sintomas_controller import *
from app.models.sintomas_model import Sintomas

router = APIRouter()

nueva_sintomas = sintomasController() #definido donde

@router.post("/create_sintomas")
async def create_sintomas(sintomas: Sintomas):
    rpta = nueva_sintomas.create_sintomas(sintomas)
    return rpta


@router.get("/get_sintoma/{sintomas_id}",response_model=Sintomas)
async def get_sintoma(sintomas_id: int):
    rpta = nueva_sintomas.get_sintoma(sintomas_id)
    return rpta

@router.get("/get_sintomas/")
async def get_sintomas():
    rpta = nueva_sintomas.get_sintomas()
    return rpta

    

@router.put("/update_sintomas/{sintomas_id}")
async def update_sintomas(sintomas_id: int ,sintomas: Sintomas,):
    rpta = nueva_sintomas.update_sintomas(sintomas_id, sintomas)
    return rpta 

@router.delete("/delete_sintomas/{sintomas_id}")
async def delete_sintomas(sintomas_id: int):
    rpta = nueva_sintomas.delete_sintomas(sintomas_id)
    
    return rpta 