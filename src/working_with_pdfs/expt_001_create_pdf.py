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
    str_out = "".join(["a"] * 100)
    # c.setTitle("Trial")

    c.drawRightString(100, 400, str_out)
    c.drawAlignedString(100, 600, str_out)
    c.drawCentredString(100, 500, str_out)
    c.drawString(100, 100, "Hello World")
    c.drawString(400, 100, str_out)

    # textobject = canvas.beginText(x, y)
    # canvas.drawText(textobject)


PS_FONT_NAME = "Times-Roman"
FONT_SIZE = 12
LINE_WIDTH = 10
LINE_CAP = ""
LINE_JOIN = ""
MITER_LIMIT = 0
PAGE_SIZE = (595.26, 841.88)  # page size for A4 -- points 1/72 inch


def page_setup(c):
    # To check the available font styles list
    # avail_fonts = c.getAvailableFonts()

    # Guiding box
    x = 25  # round(PAGE_SIZE[0] // 2, 2)
    y = 25  # round(PAGE_SIZE[1] // 2, 2)
    width = PAGE_SIZE[0] - 50
    height = PAGE_SIZE[1] - 50
    c.rect(x, y, width, height, stroke=1, fill=0)

    c.setFont(PS_FONT_NAME, FONT_SIZE, leading=None)
    c.setLineWidth(LINE_WIDTH)
    c.setPageSize(PAGE_SIZE)
    # canvas.setLineCap(LINE_CAP)
    # canvas.setLineJoin(LINE_JOIN)
    # canvas.setMiterLimit(MITER_LIMIT)
    # canvas.setDash(self, array=[], phase=0)


def create_pdf(filename="hello.pdf"):
    filepath = os.path.join(DIR_OUTPUT, filename)
    c = canvas.Canvas(filepath)

    page_setup(c)
    draw(c)
    c.showPage()
    c.save()


def main():
    create_pdf()


if __name__ == '__main__':
    main()
