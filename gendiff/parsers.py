import json
import yaml


def parse_json():
    return lambda file_path: json.load(open(file_path, 'r'))


def parse_yaml():
    return lambda file_path: yaml.safe_load(open(file_path, 'r'))
