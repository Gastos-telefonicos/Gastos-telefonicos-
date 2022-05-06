import pandas as pd
import os.path
from src.lib.utils import temp_file
from src.webserver import create_app


def test_post_excel_info():

    data = {
        "id": "factura-1",
        "Números": {0: "612232323", 1: "616634335", 2: "656544337"},
        "Coste": {
            0: "97.00",
            1: "42.00",
            2: "19.00",
        },
    }
