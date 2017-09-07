import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import csv
def convert_pdf_2_text(path, name):
    parser = PDFParser(open(path + name, "rb"))
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    if(not doc.is_extractable):
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):
                    with open(path + name[:-4] + ".txt", 'a') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + "\n")

if __name__ == '__main__':
    filePath = "C:\\Users\\sunjiayu\\Desktop\\gov\\data\\"
    papers = csv.reader(open("list.csv", "r", encoding="gb2312"))
    for paper in papers:
        convert_pdf_2_text(filePath, paper[0])
    
