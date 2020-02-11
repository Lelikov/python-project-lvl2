import json
import yaml

def parse_json(path_to_file1, path_to_file2):
    before = json.load(open(path_to_file1))
    after = json.load(open(path_to_file2))
    return before, after

def parse_yaml(path_to_file1, path_to_file2):
    before = open(path_to_file1, "r")
    after = open(path_to_file2, "r")
    return yaml.safe_load(before), yaml.safe_load(after)
