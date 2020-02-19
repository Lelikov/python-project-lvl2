import json
import yaml


def parse_json(path_to_file):
    '''
    Parse JSON into dictionary
    :return: Dictionary
    '''
    return json.load(open(path_to_file, 'r'))


def parse_yaml(path_to_file):
    '''
    Parse YAML into dictionary
    :return: Dictionary
    '''
    return yaml.safe_load(open(path_to_file, 'r'))
