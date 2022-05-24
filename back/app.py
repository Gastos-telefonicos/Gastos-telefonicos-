import sqlite3
from src.webserver import create_app
from src.domain.phones import PhonesRepository
from src.domain.phones_and_cost import PhonesAndCostRepository


database_path = "data/database_phones.db"

repositories = {
    "phones": PhonesRepository(database_path),
    "phones_cost": PhonesAndCostRepository(database_path),
}


app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
