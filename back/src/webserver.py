from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json

from src.domain.phones import Phones


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/doc", methods=["GET"])
    def phones_get_doc():
        phone = repositories["phones"].get_doc()
        return object_to_json(phone)

    @app.route("/api/doc", methods=["POST"])
    def phone_post():
        body = request.json
        phone = Phones(**body)
        repositories["phones"].save(phone)

        return ""

    return app
