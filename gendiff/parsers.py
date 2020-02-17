import json
import yaml


def parse_json():
    '''
    Parse JSON into dictionary
    :return: Dictionary
    '''
    return lambda file_path: json.load(open(file_path, 'r'))


def parse_yaml():
    '''
    Parse YAML into dictionary
    :return: Dictionary
    '''
    return lambda file_path: yaml.safe_load(open(file_path, 'r'))
