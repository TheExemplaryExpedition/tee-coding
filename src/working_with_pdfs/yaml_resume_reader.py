import yaml


class ResumeReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dict_data = self.read_data()

    def read_data(self):
        with open(self.filepath, "r") as fh:
            dict_data = yaml.safe_load(fh)

        return dict_data


def main():
    filepath = "yaml_files/sample_resume.yaml"
    obj_rr = ResumeReader(filepath)
    print(obj_rr.dict_data)


if __name__ == '__main__':
    main()
