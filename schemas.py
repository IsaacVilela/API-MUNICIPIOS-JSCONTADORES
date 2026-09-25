from typing import List
from pydantic import BaseModel

class MunicipioResposta(BaseModel):
    codigo:int
    descricao:str

    class Config:
        from_atributes=True

class MunicipioRespostaPagina(BaseModel):
    total:int
    pagina:int
    tamanho_pagina:int
    itens:List[MunicipioResposta]   