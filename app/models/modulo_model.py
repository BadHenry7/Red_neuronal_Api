from pydantic import BaseModel
from typing import List, Optional

class Modulo(BaseModel):

    id: int = None
    nombre: str
    submodulos : str
    url : str
    descripcion: str
    estado: bool


class Buscarid(BaseModel):
    id: int = None


class Modelito(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    estado: bool
    modulo_seleccionado:List[int]



