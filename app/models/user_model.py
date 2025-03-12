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
    
class Login(BaseModel):
    usuario: str
    password: str 


class Buscar(BaseModel):
    id: int= None

class Buscar_document(BaseModel):
    documento: str



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
    password:str
    telefono:str



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
