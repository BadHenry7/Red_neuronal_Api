from pydantic import BaseModel

class Citasm(BaseModel):
   
    id: int= None
    fecha: str
    hora: str
    id_usuario:int
    estado: bool
    id_paciente:int
    ubicacion: str=None

class Buscar(BaseModel):
    id_paciente:int=None
    id_cita:int=None

class Buscar_cedula(BaseModel):
    cedula:str



class Reportesss(BaseModel):
    fecha: str
    fecha2: str

class Reportes_medico(BaseModel):
    fecha: str
    fecha2: str  
    id: int  


class EditarCita(BaseModel):
    id:int  = None  
        

class Upditon(BaseModel):
    id: int= None
    fecha: str
    hora: str
    id_usuario:int
    ubicacion:str= None
    salas:str= None

       
class Chaocita(BaseModel):
    id:int=None

class ValidaHora(BaseModel):
    hora: str

class DiagnosticoSintomas(BaseModel):
    id_diagnostico: int = None
    id_cita: int
    resultado: str
    descripcion: str
    Observacion: str = None
    fecha_diagnostico: str = None
    id_sintomas: int = None
    id_cita: int
    nombre: str
    descripcion: str