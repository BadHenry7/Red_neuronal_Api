from fastapi import APIRouter, HTTPException
from app.controllers.rol_controller import *
from app.models.rol_model import Rol

router = APIRouter()

nuevo_rol = RolController() #definido donde

@router.get('/')
def home():
    return ('+page.svelte')


@router.post("/create_rol")
async def create_rol(rol: Rol):
    rpta = nuevo_rol.create_rol(rol)
    return rpta


@router.get("/get_rol/{rol_id}",response_model=Rol)
async def get_rol(rol_id: int):
    rpta = nuevo_rol.get_rol(rol_id)
    return rpta

@router.get("/roles_get")
async def roles_get():
    rpta = nuevo_rol.roles_get()
    return rpta


@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_rol.get_roles()
    return rpta


@router.put("/updaterol/{rol_id}")
async def update_rol(rol_id: int,rol: Rol,):
    rpta = nuevo_rol.update_rol(rol_id,rol)
    
    return rpta 

@router.delete("/eliminarrol/{rol_id}")
async def delete_rol(rol_id: int):
    rpta = nuevo_rol.delete_rol(rol_id)
    
    return rpta 

