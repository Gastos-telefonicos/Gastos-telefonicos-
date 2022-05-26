from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.phones import PhonesRepository, Phone


def test_should_update_projets():
    phone_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phone_repository})
    client = app.test_client()

    phone_one = Phone(phone="164454154", project="GEN1234", description="JOSEBA")
    phone_repository.save(phone_one)

    body = {
        "phone": "164454154",
        "project": "GEN4567",
        "description": "JOSEBA",
    }

    response = client.put("/api/phones/164454154", json=body)

    assert response.status_code == 200
    response_get = client.get("/api/phones")

    assert response_get.json == [
        {
            "phone": "164454154",
            "project": "GEN4567",
            "description": "JOSEBA",
        }
    ]
