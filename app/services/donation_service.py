from datetime import datetime
from uuid import uuid4
from app.schemas.donation_schema import DonationFormRequest

donation_forms = []


def create_donation_form(data: DonationFormRequest):
    donation_data = data.model_dump()

    donation_data["id"] = str(uuid4())
    donation_data["status"] = "recebido"
    donation_data["criado_em"] = datetime.now().isoformat()

    donation_forms.append(donation_data)

    print("Nova solicitação de doação recebida:")
    print(donation_data)
    return {
        "id": donation_data["id"],
        "status": donation_data["status"],
    }



def list_donation_forms():
    return donation_forms


def get_donation_form_by_id(donation_id: int):
    for donation in donation_forms:
        if donation["id"] == donation_id:
            return donation

    return None
