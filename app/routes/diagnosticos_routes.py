from fastapi import APIRouter, HTTPException
from app.controllers.diagnosticos_controller import *
from app.models.diagnosticos_model import Diagnosticos

router = APIRouter()

nuevo_diagnostico = diagnosticoController()


@router.post("/create_diagnosticos")
async def create_diagnosticos(diagnosticos: Diagnosticos):
    rpta = nuevo_diagnostico.create_diagnosticos(diagnosticos)
    return rpta


@router.get("/get_diagnostico/{diagnosticos_id}",response_model=Diagnosticos)
async def get_diagnostico(diagnosticos_id: int):
    rpta = nuevo_diagnostico.get_diagnostico(diagnosticos_id)
    return rpta

@router.get("/get_diagnosticos/")
async def get_diagnosticos():
    rpta = nuevo_diagnostico.get_diagnosticos()
    return rpta

    

@router.put("/update_diagnosticos/{diagnosticos_id}")
async def update_diagnosticos(diagnosticos_id: int,diagnosticos: Diagnosticos,):
    rpta = nuevo_diagnostico.update_diagnosticos(diagnosticos_id,diagnosticos) 
    return rpta 

@router.delete("/delete_diagnosticos/{diagnosticos_id}")
async def delete_diagnosticos(diagnosticos_id: int):
    rpta = nuevo_diagnostico.delete_diagnosticos(diagnosticos_id)
    return rpta 


@router.post("/reportes_diagnosticos/")
async def reportes_diagnosticos(diagnosticos: Reportesss):
    rpta = nuevo_diagnostico.reportes_diagnosticos(diagnosticos)
    return rpta