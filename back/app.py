import sqlite3
from src.webserver import create_app
from src.domain.phones import PhonesRepository


database_path = "data/database_phones.db"

repositories = {
    "phones": PhonesRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
