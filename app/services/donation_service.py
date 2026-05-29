from datetime import datetime
from app.schemas.donation_schema import DonationFormRequest


def create_donation_form(data: DonationFormRequest):
    donation_data = data.model_dump()

    donation_data["status"] = "recebido"
    donation_data["criado_em"] = datetime.now().isoformat()

    print("Nova solicitação de doação recebida:")
    print(donation_data)

    return donation_data