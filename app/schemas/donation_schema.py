from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


class DonationFormRequest(BaseModel):
    cnpj: str = Field(..., min_length=14, max_length=18)
    razao_social: str
    representante_instituicao: str
    email: EmailStr
    telefone: str

    pessoas_beneficiadas: int

    tipo_doacao: str
    itens_receber: List[str]
    quantidade_doacao: str

    uf: str
    observacoes: Optional[str] = None