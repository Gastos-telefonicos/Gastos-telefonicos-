from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones_and_cost import *


def test_should_return_phones_projects_and_costs():
    phone_repository = PhonesAndCostRepository(temp_file())
    app = create_app(repositories={"phonecost": phone_repository})
    client = app.test_client()

    phone_one = PhoneCost(phone="1644541544", cost="35.82")
    phone_two = PhoneCost(phone="1644541545", cost="23.45")
    phone_repository.save(phone_one)
    phone_repository.save(phone_two)

    # ACT (when)
    response = client.get("/api/pdfphones")

    # ASSERT (then)
    assert response.json == [
        {
            "phone": "1644541544",
            "cost": "35.82",
        },
        {
            "phone": "1644541545",
            "cost": "23.45",
        },
    ]
