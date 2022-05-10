from PyPDF2 import PdfFileReader

# falta meter elm pedf por lo tanto la ruta es inventada pero yo lo he probado y funciona

pdf_file = open("pdf/factura-de-prueba.pdf", "rb")
pdf_reader = PdfFileReader(pdf_file)


numOfPages = pdf_reader.getNumPages()

for i in range(0, numOfPages):
    print("Page Number: " + str(i))
    print("- - - - - - - - - - - - - - - - - - - -")
    pageObj = pdf_reader.getPage(i)
    print(pageObj.extractText())
    print("- - - - - - - - - - - - - - - - - - - -")

pdf_file.close()
