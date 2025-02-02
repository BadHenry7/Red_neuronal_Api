from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controllers.modulo_controller import *
from app.models.modulo_model import *

router = APIRouter()

nuevo_modulo = ModuloController()

@router.post("/create_modulo")
async def create_modulo(modulo : Modulo):
    rpta = nuevo_modulo.create_modulo(modulo)
    return rpta

@router.get("/get_modulos")
async def get_modulos():
    rpta = nuevo_modulo.get_modulos()
    return rpta

@router.get("/get_modulo")
async def get_modulo(modulo: Buscarid):
    rpta = nuevo_modulo.get_modulo(modulo)
    return rpta

#
@router.post("/get_modulos_asignado")
async def get_modulos_asignado(modulo: Buscarid):
    rpta = nuevo_modulo.get_modulos_asignado(modulo)
    return rpta


@router.put("/update_modulo")
async def Update_modulo(modulo: Modulo):
    rpta = nuevo_modulo.update_modulo(modulo)
    return rpta

@router.put("/update_modulo_seleccionado")
async def update_modulo_seleccionado(modulo: Modelito):
    rpta = nuevo_modulo.update_modulo_seleccionado(modulo)
    return rpta




@router.put("/desactivar_modulo")
async def Desactivar_modulo(modulo: Buscarid):
    rpta = nuevo_modulo.desactivar_modulo(modulo)
    return rpta