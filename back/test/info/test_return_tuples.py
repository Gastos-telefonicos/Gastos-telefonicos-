from src.domain.services.bill_services import Pdf_Invoice

from src.webserver import create_app


def test_should_return_a_list_of_dictionaries():

    body = """VHJ1a2F0dXRha28gZGF0dS1ib2x1bWVuYS9Wb2x1bWVuIGRlIGRhdG9zIGludGVyY2FtYmlhZG8gKDI1ODc0LDU4NDBNQikNCjc0NyA0NTggMDAxDQoNCjYsMTMyMiDigqw="""

    tuples = Pdf_Invoice("./temp.pdf")
    data = tuples.convert_base64_to_pdf(body)

    assert data == [{"phone": "747 458 001", "cost": "6,1322 €"}]
