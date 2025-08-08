from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controllers.user_controller import *
from app.models.user_model import User,Estado,Login,Buscar,Actualizar,Buscar_document
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt 

security = HTTPBearer()
SECRET_KEY = "your-secret-key" 
ALGORITHM = "HS256"


router = APIRouter()

nuevo_usuario = UserController()

#   token = credentials.credentials  # Aquí tienes el token que mandaron
#     print("Token recibido:", token)
    
  
#     try:
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
#     # Ya todo ok, crear usuario

@router.post("/create_user")
async def create_user(user: User):
  
    rpta = nuevo_usuario.create_user(user)
    return rpta

@router.post("/get_user")
async def get_user(user: Buscar):
    rpta = nuevo_usuario.get_user(user)
    return rpta

@router.post("/get_medico_especialidad")
async def get_medico_especialidad(user: Buscar):
    rpta = nuevo_usuario.get_medico_especialidad(user)
    return rpta

@router.post("/get_user_document")
async def get_user_document(user: Buscar_document):
    rpta = nuevo_usuario.get_user_document(user)
    return rpta


@router.get("/get_users")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta



@router.get("/get_medicos")
async def get_medicos():
    rpta = nuevo_usuario.get_medicos()
    return rpta


@router.get("/getpaciente")
async def get_paciente():
    rpta = nuevo_usuario.get_paciente()
    return rpta


@router.get("/getmedico")
async def get_medico():
    rpta = nuevo_usuario.get_medico()
    return rpta


@router.put("/actualizaruser")
async def update_user(user :Actualizar):
    rpta = nuevo_usuario.update_user(user)
    return rpta 


@router.put("/update_adm")
async def update_adm(adm :ActualizarAdm):
    rpta = nuevo_usuario.update_adm(adm)
    return rpta 


@router.delete("/eliminarusuario/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    return rpta 


@router.post("/create_user_masivo")
async def create_user_masivo(file: UploadFile = File(...)):
    rpta = nuevo_usuario.create_user_masivo(file)  # Esto está bien
    return rpta


@router.post("/login")
async def login(user: Login):
    rpta = nuevo_usuario.login(user)
    return rpta

@router.post("/verif_user")
async def verif_user(user: Verif_user):
    rpta = nuevo_usuario.verif_user(user)
    return rpta


@router.put("/estado_user")
async def estado_user(user: Estado):
    rpta = nuevo_usuario.estado_user(user)
    return rpta 


@router.post("/Altura_paciente")
async def Estatura_user(user: Estatura):
    rpta = nuevo_usuario.Estatura_user(user)
    return rpta 


@router.get("/video_feed")
async def video_feed(id: int):
    rpta = nuevo_usuario.video_feed(id)
    return rpta 

@router.get("/Actualizar_estatura")
async def Actualizar_estatura(user: Estatura_user):
    rpta = nuevo_usuario.Actualizar_estatura(user)
    return rpta 



@router.put("/telegram_id_user")
async def telegram_id_user(user: Buscar):
    rpta = nuevo_usuario.telegram_id_user(user)
    return rpta 


#v_usuario   