import yaml

def read_config(file_path):
    result = {}
    with open(file_path) as config:
        result = yaml.safe_load(config)
    return result