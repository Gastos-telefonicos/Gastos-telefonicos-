import pandas as pd
import os.path
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.excel import ExcelRepository, Excel


def test_post_excel_info():
    excel_repository = ExcelRepository(temp_file())
    app = create_app(repositories={"excels": excel_repository})
    client = app.test_client()
    data = {
        "id": "factura-1",
        "Números": {0: "612232323", 1: "616634335", 2: "656544337"},
        "Coste": {
            0: "97.00",
            1: "42.00",
            2: "19.00",
        },
    }
    excel_test = Excel("factura-1", data["Números"], data["Coste"])
    excel_repository.save(excel_test)
    response = client.get("/api/excels")
    assert response.json == [
        {
            "id": "factura-1",
            "Números": {0: "612232323", 1: 616634335, 2: "656544337"},
            "Coste": {
                0: "97.00",
                1: "42.00",
                2: "19.00",
            },
        }
    ]


# df = pd.DataFrame(data)


#     file_name = "test_file.xlsx"
#     df.to_excel(file_name)
#     assert os.path.exists(file_name) == False
