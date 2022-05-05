import sqlite3
from src.webserver import create_app
from src.domain.info import InfoRepository
from src.domain.phones import PhonesRepository
from src.domain.excel import ExcelRepository

database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "phones": PhonesRepository(database_path),
    "excels": ExcelRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
