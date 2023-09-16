from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Preformatted
import os
from reportlab.pdfgen import canvas

DIR_OUTPUT = "../../outputs"


def get_para():
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Code']
    text = '''
    class XPreformatted(Paragraph):
        def __init__(self, text, style, bulletText = None, frags=None, caseSensitive=1):
            self.caseSensitive = caseSensitive
            if maximumLineLength and text:
                text = self.stopLine(text, maximumLineLength, splitCharacters)
            cleaner = lambda text, dedent=dedent: ''.join(_dedenter(text or '',dedent))
            self._setup(text, style, bulletText, frags, cleaner)
    '''
    t = Preformatted(text, normalStyle, maxLineLength=60, newLineChars='> ')
    # t.draw()
    print(t)
    return t


def format_resume(rl_cs):
    # Guiding box
    # x = 25  # round(PAGE_SIZE[0] // 2, 2)
    # y = 25  # round(PAGE_SIZE[1] // 2, 2)
    # width = PAGE_SIZE[0] - 50
    # height = PAGE_SIZE[1] - 50
    # rl_cs.rect(x, y, width, height, stroke=1, fill=0)
    #
    # draw_components(rl_cs)
    # rl_cs.drawText(get_para())
    get_para()
    rl_cs.showPage()
    rl_cs.save()


def create_formatted_pdf(filename="code.pdf"):
    filepath = os.path.join(DIR_OUTPUT, filename)
    c = canvas.Canvas(filepath)

    format_resume(c)


def main():
    create_formatted_pdf()


if __name__ == '__main__':
    get_para()
