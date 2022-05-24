from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from src.lib.utils import object_to_json
from src.domain.phones import Phone
from src.domain.services.bill_services import *


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/phones", methods=["GET"])
    def phones_get_doc():
        phone = repositories["phones"].get_phones()
        return object_to_json(phone)

    @app.route("/api/docs", methods=["POST"])
    def pdf_post():
        body = request.json
        base64_string = ""
        try:
            base64_string = body["pdf"].split(",")[1]
        except:
            base64_string = body["pdf"]
        pdf_invoice = Pdf_Invoice("./temp.pdf")
        pdf_numbers_with_cost = pdf_invoice.convert_base64_to_pdf(base64_string)
        return jsonify(pdf_numbers_with_cost)

    @app.route("/api/phones", methods=["POST"])
    def phone_post():
        body = request.json
        phone = Phone(**body)
        repositories["phones"].save(phone)
        return ""

    return app
