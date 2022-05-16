from PyPDF2 import PdfFileReader
import PyPDF2
import re

pdf = "bill/factura-de-prueba.pdf"


def get_mobile_numbers_and_their_cost(text):
    pattern = r"([6|7]\d{2} \d{3} \d{3})\n(-?\d{1,4},\d{1,4}\n)*(\d{1,4},\d{1,4}) •"
    match = re.findall(pattern, text)

    print(match)
    if match:
        print("Yes, there is at least one match!")
    else:
        print("No match")


def get_text_from_all_pdf_pages(pdf):
    pdf_file = open(pdf, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.getNumPages()
    whole_text = ""
    for page in range(num_pages):
        page_obj = pdf_reader.getPage(page)
        catched_text = page_obj.extractText()
        whole_text += catched_text
    with open("/tmp/pdf.txt", "w") as f:
        print(
            "****************************************** ALL TEXT ", whole_text, file=f
        )
    a = get_mobile_numbers_and_their_cost(whole_text)
    pdf_file.close()
    return a


pdf = "bill/factura-de-prueba.pdf"
a = get_text_from_all_pdf_pages(pdf)
print(a)
