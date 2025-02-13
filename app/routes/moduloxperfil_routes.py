from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controllers.moduloxperfil_controller import *
from app.models.moduloxperfil_model import *


router = APIRouter()

nuevo_modulo = ModuloxPerfilController()

@router.post("/create_moduloxperfil")
async def create_moduloxperfil(moduloxperfil : ModuloxPerfil):
    rpta = nuevo_modulo.create_moduloxperfil(moduloxperfil)
    return rpta

@router.get("/get_modulosxperfil")
async def get_modulos():
    rpta = nuevo_modulo.get_modulos()
    return rpta

@router.get("/get_moduloxperfil")
async def get_modulo(moduloxperfil: Buscar_id):
    rpta = nuevo_modulo.get_modulo(moduloxperfil)
    return rpta

@router.post("/get_mxp_id")
async def get_mxp_id(moduloxperfil: Buscar_id_rol):
    rpta = nuevo_modulo.get_mxp_id(moduloxperfil)
    return rpta

@router.put("/update_moduloxperfil")
async def Update_modulo(moduloxperfil: ModuloxPerfil):
    rpta = nuevo_modulo.update_modulo(moduloxperfil)
    return rpta

@router.put("/desactivar_moduloxperfil")
async def Desactivar_modulo(moduloxperfil: Buscar_id):
    rpta = nuevo_modulo.desactivar_modulo(moduloxperfil)
    return rpta