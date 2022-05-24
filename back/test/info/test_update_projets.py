from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.phones import PhonesRepository, Phone


def test_should_update_projets():
    phones_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phones_repository})
    client = app.test_client()

    phone_one = Phone(phone="1644541544", project="GEN1234", description="JOSEBA")
    phones_repository.save(phone_one)

    body = {
        "phone": "1644541544",
        "project": "GEN4567",
        "description": "JOSEBA",
    }
    response = client.put("/api/phones/1644541544", json=body)

    assert response.status_code == 200
    response_get = client.get("/api/phones")

    assert response_get.json == [
        {
            "phone": "1644541544",
            "project": "GEN4567",
            "description": "JOSEBA",
        }
    ]
