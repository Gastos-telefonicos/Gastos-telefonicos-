from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.phones import Phone
from src.domain.services.bill_services import *
import base64


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

    @app.route("/api/docs", methods=["POST"])
    def phone_post():
        body = request.json
        print(body)
        base64_string = body["pdf"].split(",")[1]
        pdf_invoice = Pdf_Invoice("./temp.pdf")
        pdf_numbers_with_cost = pdf_invoice.convert_base64_to_pdf(base64_string)
        return ""

    return app
