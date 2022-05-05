from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phones


def test_should_return_phones_proyects_and_costs():
    phone_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phone_repository})
    client = app.test_client()

    phone_one = Phones(id="bill-1", phone="1644541544", costs=35)
    phone_two = Phones(id="bill-2", phone="1644541545", costs=36)
    phone_repository.save(phone_one)
    phone_repository.save(phone_two)

    # ACT (when)
    response = client.get("/api/doc")

    # ASSERT (then)
    assert response.json == [
        {"id": "bill-1", "phone": "1644541544", "costs": 35},
        {"id": "bill-2", "phone": "1644541545", "costs": 36},
    ]
