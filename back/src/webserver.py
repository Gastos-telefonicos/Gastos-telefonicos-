from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.phones import Phone
from src.domain.services.bill_services import *


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
        pdf_invoice = Pdf_Invoice(body.pdf)
        mobile_and_costs = pdf_invoice.get_text_from_all_pdf_pages()
        print("THESE ARE MOBILES NUMBERS AND COST FROM FRONT ", mobile_and_costs)
        return mobile_and_costs

    return app
