from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phone


def test_should_save_phone():
    phone_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phone_repository})
    client = app.test_client()

    body = {"phone": "747 458 001", "description": "JOSU", "project": "GEN2231"}

    response = client.post("/api/phones", json=body)

    # ASSERT (then)

    assert response.status_code == 200

    response_get = client.get("/api/phones")

    phones = response_get.json
    assert phones == [
        {"phone": "747 458 001", "description": "JOSU", "project": "GEN2231"}
    ]
