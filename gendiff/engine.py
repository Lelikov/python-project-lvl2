import json
from gendiff.parsers import parse_json, parse_yaml


def generate_diff(path_to_file1, path_to_file2):
    if path_to_file1.endswith('.json') and path_to_file2.endswith('.json'):
        before, after = parse_json(path_to_file1, path_to_file2)
    if path_to_file1.endswith('.yml') and path_to_file2.endswith('.yml'):
        before, after = parse_yaml(path_to_file1, path_to_file2)
    array = ["{"]
    for key, value in before.items():
        if after.get(key) is not None:
            if before[key] == after[key]:
                array.append("  {}: {}".format(key, value))
            else:
                array.append("  + {}: {}".format(key, after[key]))
                array.append("  - {}: {}".format(key, value))
        else:
            array.append("  - {}: {}".format(key, value))
    for key, value in after.items():
        if before.get(key) is None:
            array.append("  + {}: {}".format(key, value))
    array.append("}")
    return '\n'.join(array)
