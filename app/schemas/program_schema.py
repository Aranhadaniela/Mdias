from pydantic import BaseModel, Field
from typing import Optional

class ProgramaRequest(BaseModel):
    nome_programa: str = Field(..., min_length=3, max_length=100)
    objetivo: str
    descricao: Optional[str] = None
    ativo: bool = True

class ProgramaResponse(ProgramaRequest):
    id: int