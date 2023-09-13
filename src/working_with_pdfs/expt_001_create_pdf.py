"""
Tutorial to create a pdf from scratch
"""

import pypdf as pdf
from reportlab.pdfgen import canvas
import os

DIR_OUTPUT = "../../outputs"


# def create_page(str_out):
#     page = pdf.PageObject()
#     page.create_blank_page()
#     # page.
#     return page
#
#
# def create_pdf(filename="first.pdf"):
#     str_out = "First sentence"
#     page = create_page(str_out)
#     with open(filename, 'wb') as fh:
#         pdf_writer = pdf.PdfWriter()
#         pdf_writer.add_page(page)
#         pdf_writer.write(fh)


def draw(c):
    c.drawString(100, 100, "Hello World")


def create_pdf(filename="hello.pdf"):
    filepath = os.path.join(DIR_OUTPUT, filename)
    c = canvas.Canvas(filepath)
    draw(c)
    c.showPage()
    c.save()


def main():
    create_pdf()


if __name__ == '__main__':
    main()
