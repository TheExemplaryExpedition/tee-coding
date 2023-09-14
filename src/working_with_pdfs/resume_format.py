from reportlab.pdfgen import canvas
import os

DIR_OUTPUT = "../../outputs"
PS_FONT_NAME = "Helvetica"
FONT_SIZE = 12
LINE_WIDTH = 10
LINE_CAP = ""
LINE_JOIN = ""
MITER_LIMIT = 0
PAGE_SIZE = (595.26, 841.88)  # page size for A4 -- points 1/72 inch


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

        self.draw_guiding_box()
        self.init_doc_properties()

    def draw_guiding_box(self):
        # Guiding box
        x = 25  # round(PAGE_SIZE[0] // 2, 2)
        y = 25  # round(PAGE_SIZE[1] // 2, 2)
        width = PAGE_SIZE[0] - 50
        height = PAGE_SIZE[1] - 50

        # Draw a rectangle to get the reference of where the text fits
        self.rfc.rect(x, y, width, height, stroke=1, fill=0)

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
                "font_size": 16
            },

            "subtitle": {
                "font_name": PS_FONT_NAME,
                "font_size": 12
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

        coord_x = round(PAGE_SIZE[0] // 2, 2)
        coord_y = PAGE_SIZE[1] - 25

        self.rfc.drawCentredString(coord_x, coord_y, str_title)

        return self

    def add_subtitle(self, str_sub_title, line_num=2):
        """
        Add sub title for the resume
        :param str_sub_title:
        :param line_num:
        :return:
        """
        self.set_font_style(text_type="subtitle")

        coord_x = round(PAGE_SIZE[0] // 2, 2)
        coord_y = PAGE_SIZE[1] - line_num * 25

        self.rfc.drawCentredString(coord_x, coord_y, str_sub_title)

        return self

    def add_heading(self, str_heading, line_num=3):
        """
        Add heading for a section of the resume
        :param str_heading:
        :param line_num:
        :return:
        """
        self.set_font_style(text_type="heading")

        coord_x = 25
        coord_y = PAGE_SIZE[1] - line_num * 25

        self.rfc.drawString(coord_x, coord_y, str_heading)

        return self

    def add_description(self, str_left, str_right, line_num=4):
        """
        Common type of Descriptions have str_left and str_right.
        Sometimes str_right can be empty, so it's fine.
        :param str_left:
        :param str_right:
        :param line_num:
        :return:
        """
        self.set_font_style(text_type="description")

        coord_x_left = 25
        coord_x_right = PAGE_SIZE[0] - 25
        coord_y = PAGE_SIZE[1] - line_num * 25

        self.rfc.drawString(coord_x_left, coord_y, str_left)
        self.rfc.drawRightString(coord_x_right, coord_y, str_right)

        return self

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
            "str_heading": "Experience",
            "line_num": 3
        }
        return dict_values

    def get_description(self):
        dict_values = {
            "str_left": "CompanyName",
            "str_right": "Location",
            "line_num": 4
        }
        return dict_values


def main():
    obj_rf = ResumeFormat("xyz.pdf")
    obj_rd = ResumeData()

    obj_rf.add_title("FirstName", "LastName")

    obj_rf.add_subtitle(obj_rd.get_subtitle())
    obj_rf.add_heading(**obj_rd.get_heading())
    obj_rf.add_description(**obj_rd.get_description())

    obj_rf.save_resume()


if __name__ == '__main__':
    main()
