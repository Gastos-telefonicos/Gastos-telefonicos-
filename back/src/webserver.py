from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/excels", methods=["GET"])
    def excels_get():
        excels = repositories["excels"].get_excels()
        return object_to_json(excels)

    return app
