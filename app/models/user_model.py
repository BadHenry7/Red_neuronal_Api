from pydantic import BaseModel

class User(BaseModel):
       
    usuario: str
    password: str 
    id: int= None
    nombre: str
    apellido: str
    documento: str
    telefono:str
    id_rol: int
    estado:bool
    genero: str= None
    edad: int = None
    completado: bool=None
    
class Login(BaseModel):
    usuario: str
    password: str 


class Buscar(BaseModel):
    id: int= None
    id_telegram: int=None

class Buscar_document(BaseModel):
    documento: str
    id_doctor: int=None



class Actualizar(BaseModel):
    usuario: str
    id: int= None
    nombre: str
    apellido: str
    documento: str
    telefono:str
    id_rol:int
    estado: bool
    genero: str= None
    edad: int = None
    password: str= None
    



class ActualizarAdm(BaseModel):
    usuario: str
    id: int= None
    nombre: str
    apellido: str
    documento: str
    telefono:str
    id_rol:int
    estado: bool
    genero: str= None
    edad: int = None
    password: str= None
    estatura: str=None



class Estado(BaseModel):
    id: int= None
    estado:bool

  
class Token(BaseModel):
    token: str

      
class Verif_user(BaseModel):
    id: int= None
    id_usuario: int= None
    google_id: str
    foto: str
    access_token: str
    estado: bool
    usuario: str
    nombre: str
    apellido: str


class login_google(BaseModel):
    verif_user: Verif_user
    user: User


class Estatura (BaseModel):
    image: str

class Estatura_user (BaseModel):
    id: int
    estatura: str


class ValidarIncapacidad(BaseModel):
    id: int
    cedula: str