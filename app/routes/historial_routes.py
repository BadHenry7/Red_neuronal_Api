from fastapi import APIRouter, HTTPException
from app.controllers.historial_controller import *
from app.models.historial_model import Historial

router = APIRouter()

nuevo_historial = historial_Controller() #definido donde

@router.post("/create_historial/")
async def create_historial(historial: Historial):
    rpta = nuevo_historial.create_historial(historial)
    return rpta


@router.get("/get_historial/{historial_id}",response_model=Historial)
async def get_historial(historial_id: int):
    rpta = nuevo_historial.get_historial(historial_id)
    return rpta

@router.get("/get_historiales/")
async def get_historiales():
    rpta = nuevo_historial.get_historiales()
    return rpta

    

@router.put("/update_historial/{historial_id}")
async def update_historial(historial_id: int, historial: Historial):
    rpta = nuevo_historial.update_historial(historial_id, historial)
    return rpta 

@router.delete("/delete_historial/{historial_id}")
async def delete_historial(historial_id: int):
    rpta = nuevo_historial.delete_historial(historial_id)
    
    return rpta 


@router.post("/reportes_historial/")
async def reportes_historial(historial: Reportesss):
    rpta = nuevo_historial.reportes_historial(historial)
    return rpta