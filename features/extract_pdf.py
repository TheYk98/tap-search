from PyPDF2 import PdfFileReader

with open("D://tap chief/features/sample.pdf", 'rb') as f:
    pdf = PdfFileReader(f)
        # get the first page
    page = pdf.getPage(0)
    print(page)
    
    text = page.extractText()
    print(text)
    