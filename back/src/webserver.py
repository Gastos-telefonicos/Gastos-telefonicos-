from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json

from src.domain.phones import Phone


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/doc", methods=["GET"])
    def phones_get_doc():
        phone = repositories["phones"].get_doc()
        return object_to_json(phone)

    @app.route("/api/doc", methods=["POST"])
    def phone_post():
        body = request.json
        phone = Phone(**body)
        repositories["phones"].save(phone)

        return ""

    return app
