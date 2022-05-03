from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phones


def test_should_return_phones_proyects_and_costs():
    phone_repository = PhonesRepository(temp_file())
    app = create_app(repositories={"phones": phone_repository})
    client = app.test_client()

    phone = Phones(phone="1644541544", proyect="GEN8458", costs=35)
    phone_repository.save(phone)

    # ACT (when)
    response = client.get("/api/doc/doc-1")

    # ASSERT (then)
    assert response.json == [{"phone": "1644541544", "proyect": "GEN8458", "costs": 35}]
