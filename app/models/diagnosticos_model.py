from pydantic import BaseModel

class Diagnosticos(BaseModel):
    
    id: int= None
    id_cita: int
    resultado: str
    descripcion: str
    Observacion: str
    fecha_diagnostico: str=None
    estado: bool
    



class Reportesss(BaseModel):
    fecha: str
    fecha2: str