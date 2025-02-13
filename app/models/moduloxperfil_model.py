from pydantic import BaseModel
from typing import List, Optional

class ModuloxPerfil(BaseModel):

    id: int = None
    id_rol: int = None
    id_modulo: List[int]
    estado: bool

class Buscar_id (BaseModel):

    id_modulo: int = None


class Buscar_id_rol (BaseModel):

    id_rol: int
   
    
