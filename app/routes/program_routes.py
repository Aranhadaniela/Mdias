from fastapi import APIRouter, HTTPException
from app.schemas.program_schema import ProgramaRequest
from app.services.program_service import (
    create_programa,
    list_programas,
    get_programa_by_id,
    deactivate_programa,
    get_programa_com_contagem
)

router = APIRouter(
    tags=["Programas de Doação"]
)

@router.post("/programas")
def create_programa_route(data: ProgramaRequest):
    result = create_programa(data)
    return {
        "success": True,
        "message": "Programa criado com sucesso.",
        "data": result
    }

@router.get("/programas")
def get_programas(apenas_ativos: bool = True):
    result = list_programas(apenas_ativos)
    return {
        "success": True,
        "total": len(result),
        "data": result
    }

@router.get("/programas/{programa_id}")
def get_programa(programa_id: int):
    result = get_programa_by_id(programa_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Programa não encontrado."
        )
    return {
        "success": True,
        "data": result
    }

@router.delete("/programas/{programa_id}")
def deactivate_programa_route(programa_id: int):
    sucesso = deactivate_programa(programa_id)
    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Programa não encontrado."
        )
    return {
        "success": True,
        "message": "Programa desativado com sucesso."
    }

@router.get("/programas/relatorio/contagem")
def get_contagem_solicitacoes():
    result = get_programa_com_contagem()
    return {
        "success": True,
        "data": result
    }