from pydantic import BaseModel

class Sintomas(BaseModel):
    id: int= None
    nombre: str
    descripcion: str
    estado: bool    	
    id_cita: int				