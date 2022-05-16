from PyPDF2 import PdfFileReader
import re

pdf_file = open("scripts/factura-de-prueba.pdf", "rb")
pdf_reader = PdfFileReader(pdf_file)


def get_text_from_all_pdf_pages(pdf_file):

    num_pages = pdf_reader.getNumPages()

    whole_text = ""

    for i in range(8, num_pages):
        page_obj = pdf_reader.getPage(i)
        catched_text = page_obj.extractText()
        whole_text += catched_text

    resultado = re.search("Móvil", whole_text)

    pdf_file.close()

    return resultado


print(get_text_from_all_pdf_pages(pdf_file))
