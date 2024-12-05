from fastapi import APIRouter, HTTPException
from app.controllers.atributoxusuario_controller import *
from app.models.atributoxusuario_model import Atributoxusuario, BuscarAtributoxusuario, UpdateAtributoxusuario

router = APIRouter()

nuevo_atributo = AtributoxusuarioController()

@router.post("/create_atributoxusuario")
async def create_atributoxusuario(atributoxusuario: Atributoxusuario):
    rpta = nuevo_atributo.create_atributoxusuario(atributoxusuario)
    return rpta

"""@router.get("/get_atributoxusuario/{atributoxusuario_id}",response_model=Atributoxusuario)
async def get_atributoxusuario(atributoxusuario_id: int):
    rpta = nuevo_atributo.get_atributoxusuario(atributoxusuario_id)
    return rpta
"""

@router.post("/get_atributoxusuario")
async def get_atributoxusuario(atributoxusuario: BuscarAtributoxusuario):
    rpta = nuevo_atributo.get_atributoxusuario(atributoxusuario)
    return rpta

@router.put("/updateatributoxusuario")
async def updateatributoxusuario(atributoxusuario: UpdateAtributoxusuario):
    rpta = nuevo_atributo.updateatributoxusuario(atributoxusuario)
    return rpta



@router.get("/get_atributoxusuarios")
async def get_atributoxusuarios():
    rpta = nuevo_atributo.get_atributoxusuarios()
    return rpta

"""@router.put("/update_atributosxusuario/{atributoxusuario_id}")
async def update_atributoxusuarios(atributoxusuario_id: int, atributoxusuario: Atributoxusuario):
    rpta = nuevo_atributo.update_atributoxusuarios(atributoxusuario_id, atributoxusuario)
    return rpta"""

@router.delete("/delete_atributoxusuario/{atributoxusuario_id}")
async def delete_atributoxusuario(atributoxusuario_id: int):
    rpta = nuevo_atributo.delete_atributoxusuarios(atributoxusuario_id)
    return rpta 