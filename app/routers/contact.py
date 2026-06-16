from fastapi import APIRouter
from app.schemas.contact import ContactMessage
from app.services.contact_service import save_contact

router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)


@router.post("/", status_code=201)
def send_message(contact: ContactMessage):
    return {
        "status": "Message reçu",
        "data": save_contact(contact)
    }
