import PyPDF2
import re
import base64


class Pdf_Invoice:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def convert_base64_to_pdf(self, base64_string):
        with open(self.pdf_path, "wb") as the_file:
            the_file.write(base64.b64decode(base64_string))

        pfd_num_and_cost = self.get_text_from_all_pdf_pages()
        object_list = self.convert_tuple_list_to_object_list(pfd_num_and_cost)
        final_list = []
        for object in object_list:
            object["phone"] = object["phone"].replace(" ", "")
            final_list.append(object)
        return final_list

    def get_mobile_numbers_and_their_cost(self, text):
        pattern = r"([6|7]\d{2} \d{3} \d{3})\n(-?\d{1,4},\d{1,4}\n)*(\d{1,4},\d{1,4}) •"
        match = re.findall(pattern, text)
        return match

    def get_text_from_all_pdf_pages(self):
        pdf_file = open(self.pdf_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()
        whole_text = ""
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            catched_text = page_obj.extractText()
            whole_text += catched_text
        list_of_phones_and_cost = self.get_mobile_numbers_and_their_cost(whole_text)
        pdf_file.close()
        return list_of_phones_and_cost

    def convert_tuple_list_to_object_list(self, tuple_list):
        object_list = []
        for each_tuple in tuple_list:
            object_list.append({"phone": each_tuple[0], "cost": each_tuple[2]})
        return object_list
