from fastapi import APIRouter
from app.schemas.donation_schema import DonationFormRequest
from app.services.donation_service import create_donation_form

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