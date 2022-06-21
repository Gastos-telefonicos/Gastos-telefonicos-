from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phone
from src.domain.phones_and_cost import PhonesAndCostRepository
from script.body_base64 import body_2

def setup():
    phone_repository = PhonesAndCostRepository(temp_file())
    app = create_app(repositories={"phones_cost": phone_repository})
    client = app.test_client()
    return client


def test_should_return_phones_projects_and_costs():
    client = setup()
    body_1 = {
        "pdf": body_2['pdf']
    }

    response_1 = client.post("/api/docs", json=body_1, content_type="application/json")
    assert response_1.status_code == 200
    assert response_1.json == [
    {"phone": "605713419", "cost": "0,0000"},
    {"phone":"605713420","cost":"18,6595"},
    {"phone":"605719309","cost":"10,4381"}
    ]


def test_delete_db_and_insert_new_phones():
    client = setup()
    body_1 = {
        "pdf": body_2['pdf']
    }
    client.post("/api/docs", json=body_1, content_type="application/json")
    sec_body = {
        "pdf": body_2['pdf']
    }
    response = client.post("/api/docs", json=sec_body, content_type="application/json")
    assert response.status_code == 200
    assert response.json == [
        {"phone": "605713419", "cost": "0,0000"},
    {"phone":"605713420","cost":"18,6595"},
    {"phone":"605719309","cost":"10,4381"}
    ]
