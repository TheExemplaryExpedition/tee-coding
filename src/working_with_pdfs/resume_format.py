from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
import os

DIR_OUTPUT = "../../outputs"
PS_FONT_NAME = "Helvetica"
FONT_SIZE = 12
LINE_WIDTH = 10
LINE_CAP = ""
LINE_JOIN = ""
MITER_LIMIT = 0
PAGE_SIZE = (595.26, 841.88)  # page size for A4 -- points 1/72 inch
LINE_HEIGHT = 12
MARGIN = 25

dict_indent_levels = {
    "headers": MARGIN + 10,
    "bullet": MARGIN + 20
}


# class SingletonClass(object):
#   def __new__(cls):
#     if not hasattr(cls, 'instance'):
#       cls.instance = super(SingletonClass, cls).__new__(cls)
#     return cls.instance


class LineCounter:
    """
    Create a singleton class to keep track of the current line in a page
    Reference: https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LineCounter, cls).__new__(cls)
            cls.line_counter = 0
            cls.coord_y = PAGE_SIZE[1]
        return cls.instance

    def next_line(self):
        if self.line_counter == 0:
            self.line_counter += 1
            self.coord_y -= self.line_counter * 3 * LINE_HEIGHT
        else:
            self.coord_y -= LINE_HEIGHT
            self.line_counter += 1
        return self.coord_y


class ResumeFormat:
    """
    A class to abstract the details of creating a formatted resume.
    """

    def __init__(self, filename="formatted.pdf"):
        """
        Initialize a canvas with filename and use it for creating the resume.
        :param filename:
        """
        self.filepath = os.path.join(DIR_OUTPUT, filename)
        # Create a Resume Format Canvas object named as rfc
        self.rfc = canvas.Canvas(self.filepath)
        self.lc = LineCounter()

        self.draw_guiding_lines()
        self.init_doc_properties()

    def draw_guiding_lines(self):
        # Guiding box
        x = MARGIN  # round(PAGE_SIZE[0] // 2, 2)
        y = MARGIN  # round(PAGE_SIZE[1] // 2, 2)
        width = PAGE_SIZE[0] - 2 * MARGIN
        height = PAGE_SIZE[1] - 2 * MARGIN

        # Draw a rectangle to get the reference of where the text fits
        # self.rfc.rect(x, y, width, height, stroke=1, fill=0)

        # self.rfc.lines(linelist)
        list_x = [50 * ith for ith in range(1, 12)]
        list_y = [50 * ith for ith in range(1, 16)]
        # self.rfc.grid(list_x, list_y)

    def draw_horizontal_line(self, x_left=None, x_right=None, y=None):
        """
        Draw a horizontal line separator to distinguish sections.
        :param y: fixed because we need horizontal line
        :param x_left: left end of the line segment
        :param x_right: right end of the line segment
        :return:
        """
        self.rfc.setLineWidth(0.5)
        if x_left is None:
            x_left = MARGIN - 5
        if x_right is None:
            x_right = PAGE_SIZE[0] - MARGIN + 5
        if y is None:
            y = self.lc.next_line() + LINE_HEIGHT // 2
        self.rfc.line(x_left, y, x_right, y)
        return self

    def init_doc_properties(self):
        # To check the available font styles list
        # avail_fonts = c.getAvailableFonts()

        self.rfc.setLineWidth(LINE_WIDTH)
        self.rfc.setPageSize(PAGE_SIZE)
        # canvas.setLineCap(LINE_CAP)
        # canvas.setLineJoin(LINE_JOIN)
        # canvas.setMiterLimit(MITER_LIMIT)
        # canvas.setDash(self, array=[], phase=0)

    def set_font_style(self, text_type="title"):
        """
        Set font style based on the context of the resume
        :param text_type:
        :return:
        """
        dict_font_styles = {
            "title": {
                "font_name": "Times-Roman",
                "font_size": 20
            },

            "subtitle": {
                "font_name": PS_FONT_NAME,
                "font_size": 10
            },

            "heading": {
                "font_name": PS_FONT_NAME,
                "font_size": 10
            },

            "description": {
                "font_name": PS_FONT_NAME,
                "font_size": 8
            },

        }
        self.rfc.setFont(dict_font_styles[text_type]["font_name"],
                         dict_font_styles[text_type]["font_size"],
                         leading=None)

        return self

    def add_title(self, firstname, lastname):
        """
        Add title in the top row and center of the page.
        :param firstname:
        :param lastname:
        :return:
        """
        self.set_font_style(text_type="title")
        str_title = f"{firstname} {lastname}"

        coord_x = round(PAGE_SIZE[0] / 2, 2)
        coord_y = self.lc.next_line() + LINE_HEIGHT * 3 // 4

        self.rfc.drawCentredString(coord_x, coord_y, str_title)

        return self

    def add_subtitle(self, str_sub_title):
        """
        Add sub title for the resume
        :param str_sub_title:
        :return:
        """
        self.set_font_style(text_type="subtitle")

        coord_x = round(PAGE_SIZE[0] / 2, 2)
        coord_y = self.lc.next_line()

        self.rfc.drawCentredString(coord_x, coord_y, str_sub_title)

        return self

    def add_heading(self, str_heading):
        """
        Add heading for a section of the resume
        :param str_heading:
        :return:
        """
        self.set_font_style(text_type="heading")

        coord_x = MARGIN
        coord_y = self.lc.next_line()

        self.rfc.drawString(coord_x, coord_y, str_heading)

        return self

    def add_experience_header(self, str_left, str_right):
        """
        Common type of Descriptions have str_left and str_right.
        Sometimes str_right can be empty, so it's fine.
        :param str_left:
        :param str_right:
        :return:
        """
        self.set_font_style(text_type="description")

        coord_x_left = dict_indent_levels["headers"]
        coord_x_right = PAGE_SIZE[0] - MARGIN
        coord_y = self.lc.next_line()

        self.rfc.drawString(coord_x_left, coord_y, str_left)
        self.rfc.drawRightString(coord_x_right, coord_y, str_right)

        return self

    def add_bullet_point(self, str_text, bullet="circle", fill=0):

        coord_x = dict_indent_levels["bullet"]
        coord_y = self.lc.next_line()
        coord_by = coord_y + LINE_HEIGHT // 4

        if bullet == "circle":
            self.rfc.circle(coord_x, coord_by, 2, stroke=1, fill=fill)

        elif bullet == "round_rect":
            coord_bx = coord_x - 3
            coord_by = coord_y + LINE_HEIGHT // 4
            self.rfc.roundRect(coord_bx, coord_y, 6, 4, 1, stroke=1, fill=fill)

        coord_x += 5
        self.rfc.drawString(coord_x, coord_y, str_text)

    def add_skills(self, title, list_skills, bullet="circle", fill=0):
        str_text = Paragraph(f'<b>{title}</b>: {list_skills}')

        coord_x = dict_indent_levels["bullet"]
        coord_y = self.lc.next_line()
        coord_by = coord_y + LINE_HEIGHT // 4

        if bullet == "circle":
            self.rfc.circle(coord_x, coord_by, 2, stroke=1, fill=fill)

        elif bullet == "round_rect":
            coord_bx = coord_x - 3
            coord_by = coord_y + LINE_HEIGHT // 4
            self.rfc.roundRect(coord_bx, coord_y, 6, 4, 1, stroke=1, fill=fill)

        coord_x += 5
        # TODO: Parameterize the wrap to fit the text appropriately
        str_text.wrap(200, 200)
        str_text.drawOn(self.rfc, coord_x, coord_y)
        # self.rfc.drawString(coord_x, coord_y, str_text)

    def save_resume(self):
        self.rfc.showPage()
        self.rfc.save()


class ResumeData:
    def __init__(self):
        pass

    def get_subtitle(self):
        phone_num = "(123)-456-7890"
        email_address = "abcdefgh.jklmnopqr@stuvw.xyz"
        github_link = "github.com/resume"
        linkedin_link = "linkedin.com/iam"
        subtitle = f"{phone_num} | {email_address} | {github_link} | {linkedin_link}"
        return subtitle

    def get_heading(self):
        dict_values = {
            "str_heading": "Experience"
        }
        return dict_values

    def get_description(self):
        dict_values = {
            "str_left": "COMPANY NAME | Machine Learning Engineer",
            "str_right": "Location | MMM. YYYY -- MMM. YYYY"
        }
        return dict_values

    def get_bullet(self):
        return "".join(["abda"] * 10)


def main():
    obj_rf = ResumeFormat("xyz.pdf")
    obj_rd = ResumeData()

    obj_rf.add_title("FirstName", "LastName")
    obj_rf.add_subtitle(obj_rd.get_subtitle())
    obj_rf.draw_horizontal_line()

    obj_rf.add_heading(**obj_rd.get_heading())
    obj_rf.add_experience_header(**obj_rd.get_description())
    obj_rf.add_bullet_point(obj_rd.get_bullet(), "circle")
    obj_rf.add_bullet_point(obj_rd.get_bullet(), "round_rect")
    obj_rf.draw_horizontal_line()

    skill = "Coding"
    list_skills = ["Python", "R", "SQL"]
    obj_rf.add_heading("SKILLS")
    obj_rf.add_skills(skill, list_skills, "circle")
    obj_rf.add_skills(skill, list_skills, "round_rect")
    obj_rf.draw_horizontal_line()

    obj_rf.save_resume()


def check_line_counter():
    lc = LineCounter()
    print(lc.next_line())
    print(lc.next_line())
    print(lc.next_line())

    lc2 = LineCounter()
    print(lc2.next_line())
    print(lc2.next_line())
    print(lc2.next_line())


if __name__ == '__main__':
    main()
