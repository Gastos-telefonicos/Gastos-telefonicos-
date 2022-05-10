from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.phones import PhonesRepository, Phone


def test_should_save_contact():

    # ARRANGE (given)

    phones_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phones_repository})
    client = app.test_client()

    # ACT (when)
    body = [
        {"id": "bill-1", "phone": "1644541544", "costs": 35, "proyect": "GEN1234"},
        {"id": "bill-2", "phone": "6496856935", "costs": 50, "proyect": "GEN5678"},
    ]

    response = client.post("/api/doc", json=body)

    # ASSERT (then)

    assert response.status_code == 200

    response_get = client.get("/api/doc")

    assert response_get.json == [
        {"id": "bill-1", "phone": "1644541544", "costs": 35, "proyect": "GEN1234"},
        {"id": "bill-2", "phone": "6496856935", "costs": 50, "proyect": "GEN5678"},
    ]
