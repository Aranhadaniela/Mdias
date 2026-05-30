from fastapi import APIRouter, HTTPException

from app.schemas.donation_schema import DonationFormRequest
from app.services.donation_service import (
    create_donation_form,
    list_donation_forms,
    get_donation_form_by_id
)

router = APIRouter(
    tags=["Formulário de Doação"]
)


@router.post("/formulario-doacao")
def submit_donation_form(data: DonationFormRequest):
    result = create_donation_form(data)

    return {
        "success": True,
        "message": "Formulário de doação enviado com sucesso.",
        "data": result
    }


@router.get("/formulario-doacao")
def get_donation_forms():
    result = list_donation_forms()

    return {
        "success": True,
        "total": len(result),
        "data": result
    }


@router.get("/formulario-doacao/{donation_id}")
def get_donation_form(donation_id: str):
    result = get_donation_form_by_id(donation_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Solicitação de doação não encontrada."
        )

    return {
        "success": True,
        "data": result
    }