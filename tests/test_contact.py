import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from pydantic import ValidationError

from app.routers.contact import send_message
from app.schemas import ContactMessage
from app.services import contact_service


class ContactTestCase(unittest.TestCase):
    def test_send_message_saves_contact(self):
        payload = {
            "name": "Alif",
            "email": "alif.rafayel@hotmail.fr",
            "subject": "Bonjour",
            "message": "Votre portfolio est intéressant.",
        }

        with TemporaryDirectory() as directory:
            contact_file = Path(directory) / "contact.json"

            with patch.object(contact_service, "FILE_PATH", contact_file):
                response = send_message(ContactMessage(**payload))

            self.assertEqual(response, {"status": "Message reçu", "data": payload})
            self.assertEqual(
                json.loads(contact_file.read_text(encoding="utf-8")),
                [payload],
            )

    def test_contact_rejects_invalid_email(self):
        with self.assertRaises(ValidationError):
            ContactMessage(
                name="Alif",
                email="email-invalide",
                subject="Bonjour",
                message="Test",
            )


if __name__ == "__main__":
    unittest.main()
