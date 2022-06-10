from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phone


def test_should_delete_a_phone():
    phone_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phone_repository})
    client = app.test_client()

    phone_one = Phone(
        phone="1644541544", project="GEN1234", description="JOSEBA", subaccount="628"
    )
    phone_two = Phone(
        phone="1644541545", project="GEN5678", description="JOSU", subaccount="628"
    )
    phone_repository.save(phone_one)
    phone_repository.save(phone_two)

    # ACT (when)

    body = {
        "phone": "1644541544",
        "project": "GEN1234",
        "description": "JOSEBA",
        "subaccount": "628",
    }

    response_delete = client.delete("/api/phones", json=body)
    assert response_delete.status_code == 200

    # ASSERT (then)
    response = client.get("/api/phones")
    assert response.json == [
        {
            "phone": "1644541545",
            "project": "GEN5678",
            "description": "JOSU",
            "subaccount": "628",
        },
    ]
