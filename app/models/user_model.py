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
    estado: bool



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

      
