from PyPDF2 import PdfFileReader
class pdf2string:
    def convert_file(file_name):

        with open(file_name, 'rb') as f:
            pdf = PdfFileReader(f)
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                text = page.extractText()+"\r\n"
        
        return text
        