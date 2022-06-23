from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phone
from src.domain.phones_and_cost import PhonesAndCostRepository, PhoneCost


def test_should_return_phone_project_description_and_cost():
    database = temp_file()
    phone_and_cost_repository = PhonesAndCostRepository(database)
    app_2 = create_app(repositories={"phones_cost": phone_and_cost_repository})
    client_two = app_2.test_client()
    phone_repository = PhonesRepository(database)
    app_1 = create_app(repositories={"phones": phone_repository})
    client_one = app_1.test_client()

    phone_one = Phone(
        phone="747 458 001", project="GEN1234", description="JOSEBA", subaccount="628"
    )
    phone_two = Phone(
        phone="1644541545", project="GEN5678", description="JOSU", subaccount="628"
    )
    phone_repository.save(phone_one)
    phone_repository.save(phone_two)

    phone_cost_one = PhoneCost(phone="747 458 001", cost="40")
    phone_and_cost_repository.save(phone_cost_one)
    phone_cost_two = PhoneCost(phone="1644541545", cost="90")
    phone_and_cost_repository.save(phone_cost_two)

    response_1 = client_one.get("/api/phones/full-data")

    # ASSERT (then)
    assert response_1.json['phones'] == [
        {
            "phone": "747 458 001",
            "project": "GEN1234",
            "description": "JOSEBA",
            "subaccount": "628",
            "cost": "40",
            "no_assigned_phone":"747 458 001"
        },
        {
            "phone": "1644541545",
            "project": "GEN5678",
            "description": "JOSU",
            "subaccount": "628",
            "cost": "90",
            "no_assigned_phone":"1644541545"
        },
    ]
    print(response_1.json)
    