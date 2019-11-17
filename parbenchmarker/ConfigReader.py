import yaml


class ConfigReader():
    file_path = ""

    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_config(self):
        result = {}
        with open(self.file_path) as config:
            result = yaml.safe_load(config)
        return result


if __name__ == "__main__":
    c = ConfigReader("./config.yaml")
    print(c.read_config())

