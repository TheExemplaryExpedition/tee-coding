import yaml


class ResumeReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dict_data = self.read_data()

    def read_data(self):
        with open(self.filepath, "r") as fh:
            dict_data = yaml.safe_load(fh)

        return dict_data

    def get_first_name(self):
        return self.dict_data["first_name"]

    def get_last_name(self):
        return self.dict_data["last_name"]

    def get_full_name(self):
        fn = self.get_first_name()
        ln = self.get_last_name()
        return f"{fn} {ln}"

    def get_phone_number(self):
        return self.dict_data["phone_number"]

    def get_email_address(self):
        return self.dict_data["email_address"]

    def get_github_username(self):
        return self.dict_data["github_username"]

    def get_linkedin_username(self):
        return self.dict_data["linkedin_username"]

    def get_experiences(self):
        return self.dict_data["experiences"]

    def get_exp_number_of_years(self):
        """
        Calculate total number of years based on the start and end dates
        Exclude present job and calculate till present
        :return:
        """
        number_of_years = 0
        for experience, details in self.dict_data["experiences"]:
            pass

        return number_of_years

    def get_date(self, dict_experience, prefix="start"):
        """
        Given a dictionary of experience, return start date if prefix=start
        :param dict_experience:
        :param prefix: "start" or "end"
        :return:
        """
        yyyy = dict_experience[f"{prefix}_year"]
        mm = dict_experience[f"{prefix}_month"]
        dd = dict_experience.get(f"{prefix}_day", 1)
        return self.get_formatted_date(yyyy, mm, dd)

    def get_formatted_date(self, yyyy, mm, dd=1):
        """
        Support multiple formatting options
        :param yyyy:
        :param mm:
        :param dd:
        :return:
        """
        return f"{yyyy}-{mm:02}-{dd:02}"

    def get_education(self):
        return self.dict_data["education"]

    def get_skills(self):
        return self.dict_data["skills"]


def main():
    filepath = "yaml_files/minimalist_resume.yaml"
    obj_rr = ResumeReader(filepath)
    print(obj_rr.dict_data)
    print(obj_rr.get_full_name())


if __name__ == '__main__':
    main()
