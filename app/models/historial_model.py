from pydantic import BaseModel

class Historial(BaseModel):
    id: int= None
    id_usuario: int
    id_sintoma: int
    fecha:str
    estado:bool
    
class Reportesss(BaseModel):
    fecha: str
    fecha2: str  