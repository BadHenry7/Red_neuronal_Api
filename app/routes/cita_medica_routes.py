from fastapi import APIRouter, HTTPException
from app.controllers.cita_medica_controller import *
from app.models.citas_medicas_model import Citasm,Buscar, EditarCita,Chaocita,Upditon

router = APIRouter()

nueva_cita = citaController() #definido donde

@router.post("/create_cita/")
async def create_cita(cita: Citasm):
    rpta = nueva_cita.create_cita(cita)
    return rpta


@router.get("/get_cita/{cita_id}",response_model=Citasm)
async def get_cita(cita_id: int):
    rpta = nueva_cita.get_cita(cita_id)
    return rpta

@router.post("/post_citas_users/")
async def post_citas_users(cita: Buscar):
    rpta = nueva_cita.post_citas_users(cita)
    return rpta



@router.post("/post_citas_doctor")
async def post_citas_doctor(cita: Buscar):
    rpta = nueva_cita.post_citas_doctor(cita)
    return rpta


@router.post("/editar_cita/")
async def editar_cita(cita: EditarCita):
    rpta = nueva_cita.editar_cita(cita)
    return rpta

@router.get("/get_citas/")
async def get_citas():
    rpta = nueva_cita.get_citas()
    return rpta

@router.get("/get_cita_admin/")
async def get_cita_admin():
    rpta = nueva_cita.get_cita_admin()
    return rpta
    

@router.put("/update_cita")
async def update_cita(cita: Upditon,):
    rpta = nueva_cita.update_cita(cita)
    return rpta 

@router.put("/eliminar_cita")
async def delete_cita(cita: Chaocita):
    rpta = nueva_cita.delete_cita(cita)
    return rpta 


@router.post("/reportes_citas/")
async def reportes_citas(cita: Reportesss):
    rpta = nueva_cita.reportes_citas(cita)
    return rpta

@router.post("/reportes_citas_medicos")
async def reportes_citas_medicos(cita:Reportes_medico):
    rpta = nueva_cita.reportes_citas_medicos(cita)
    return rpta

#-------------Estadisticas

@router.get("/estadisticas_citas")
async def estadisticas_citas():
    rpta = nueva_cita.estadisticas_citas()
    return rpta


@router.get("/estadisticas2_citas")
async def estadisticas2_citas():
    rpta = nueva_cita.estadisticas2_citas()
    return rpta

@router.get("/estadisticas3_citas")
async def estadisticas3_citas():
    rpta = nueva_cita.estadisticas3_citas()
    return rpta

@router.get("/estadisticas4_citas")
async def estadisticas4_citas():
    rpta = nueva_cita.estadisticas4_citas()
    return rpta

@router.get("/estadisticas_citas_activas")
async def estadisticas_citas_activas():
    rpta = nueva_cita.estadisticas_citas_activas()
    return rpta


@router.get("/estadisticas_citas_desactivado")
async def estadisticas_citas_desactivado():
    rpta = nueva_cita.estadisticas_citas_desactivado()
    return rpta


@router.post("/estadisticas_avg_citas")
async def estadisticas_avg_citas(cita: Reportesss):
    rpta = nueva_cita.estadisticas_avg_citas(cita)
    return rpta


@router.post("/historia_clinica")
async def historia_clinica(historia_clinica: Buscar):
    rpta = nueva_cita.historia_clinica(historia_clinica)
    return rpta



@router.post("/historia_clinica_user")
async def historia_clinica_user(historia_clinica: Buscar):
    rpta = nueva_cita.historia_clinica_user(historia_clinica)
    return rpta


#--------------Ruta para el chatbox
@router.post("/get_ultima_cita")
async def get_ultima_cita(cita: Buscar_cedula):
    rpta = nueva_cita.get_ultima_cita(cita)
    return rpta

@router.post("/get_diagnosticos_chatbox")
async def get_diagnosticos_chatbox(cita: Buscar_cedula):
    rpta = nueva_cita.get_diagnosticos_chatbox(cita)
    return rpta

@router.post("/get_recomendaciones_chatbox")
async def get_recomendaciones_chatbox(cita: Buscar_cedula):
    rpta = nueva_cita.get_recomendaciones_chatbox(cita)
    return rpta

@router.post("/get_sintomas_chatbox")
async def get_sintomas_chatbox(cita: Buscar_cedula):
    rpta = nueva_cita.get_sintomas_chatbox(cita)
    return rpta

@router.post("/get_ubicacion_chatbox")
async def get_ubicacion_chatbox(cita: Buscar_cedula):
    rpta = nueva_cita.get_ubicacion_chatbox(cita)
    return rpta

@router.post("/HistorialCitas")
async def HistorialCitas(user: Buscar):
    rpta = nueva_cita.HistorialCitas(user)
    return rpta 

@router.get("/ValidarHora")
async def ValidarHora():
    rpta = nueva_cita.ValidarHora()
    return rpta 

   