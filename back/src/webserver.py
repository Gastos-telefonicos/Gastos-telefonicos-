from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from src.domain.phones_and_cost import PhoneCost, PhonesAndCostRepository
from src.lib.utils import object_to_json
from src.domain.phones import Phone
from src.domain.services.bill_services import *
import os
import dotenv
def create_app(repositories):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    app = Flask(__name__)
    CORS(app)
    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/phones", methods=["POST"])
    def phone_post():
        body = request.json
        phone = Phone(**body)
        repositories["phones"].save(phone)
        return ""

    @app.route("/api/phones", methods=["GET"])
    def phones_get_doc():
        phone = repositories["phones"].get_phones()
        return object_to_json(phone)

    @app.route("/api/phones", methods=["DELETE"])
    def delete_phone():
        body = request.json
        phone = body["phone"]
        repositories["phones"].delete_phones(phone)
        return "", 200

    @app.route("/api/phones/full-data", methods=["GET"])
    def get_full_data_phone():
        print("ejecuto el full-data")
        phone = repositories["phones"].get_full_data_phone()
        config = dotenv.dotenv_values(".env")
        print(config['TOTAL'],"soy el totalprice del fulldata")
        return jsonify({
            "phones":phone,
            "total":config['TOTAL']
        })

    @app.route("/api/docs", methods=["POST"])
    def pdf_post():
        print("ejecuto el post")
        body = request.json
        base64_string = ""
        try:
            base64_string = body["pdf"].split(",")[1]
        except:
            base64_string = body["pdf"]
        pdf_invoice = Pdf_Invoice("./temp.pdf")
        pdf_numbers_with_cost = pdf_invoice.convert_base64_to_pdf(base64_string)
        dotenv.set_key(dotenv_file, "TOTAL", pdf_numbers_with_cost['total'].group(0))
        repositories["phones_cost"].delete_table()
        for phone in pdf_numbers_with_cost['phones_list']:
            phone_cost = PhoneCost(**phone)
            repositories["phones_cost"].save(phone_cost)
        return jsonify(pdf_numbers_with_cost['phones_list'])

    @app.route("/api/phones", methods=["PUT"])
    def projects_put():
        body = request.json
        phone = Phone(**body)

        repositories["phones"].save_by_phone(phone)
        return "", 200

    return app
