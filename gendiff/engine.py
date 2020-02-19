from gendiff.parsers import parse_json, parse_yaml
from gendiff.formatters import json_render, plain_render, text_render
import os.path
from gendiff.constants import ADDED, DELETED, CHANGED, NO_CHANGED

RENDER = {
    'text': text_render.text_render,
    'plain': plain_render.plain_render,
    'json': json_render.json_render
}

FILE_TYPE = {
    '.json': parse_json,
    '.yml': parse_yaml
}

PROBLEM = {
    'Not_found': 'File not found',
    'Unsupported': 'Unsupported type of file. Supported .json and .yml'
}


def generate_diff(path_to_file1, path_to_file2, format):
    '''
    Generating difference between two files. Print in plain, text or JSON format
    :param path_to_file1: Path to first file
    :param path_to_file2: Path to second file
    :param format: Output format. Plain, text or JSON
    :return: Difference between two files
    '''
    first_file_extension = os.path.splitext(path_to_file1)[1]
    second_file_extension = os.path.splitext(path_to_file1)[1]
    problem = ''

    try:
        first_file = FILE_TYPE[first_file_extension](path_to_file1)
        second_file = FILE_TYPE[second_file_extension](path_to_file2)
        diff_list = []
        result = RENDER[format](constructor_diff(first_file, second_file, '', diff_list))
    except FileNotFoundError:
        problem = PROBLEM['Not_found']
    except KeyError:
        problem = PROBLEM['Unsupported']

    if not problem:
        print(result)
        return result
    else:
        print(problem)
        return problem


def constructor_diff(first_file, second_file, path, diff_list):
    first_file_keys = first_file.keys()
    second_file_keys = second_file.keys()

    def add(diff_key, operation, value):
        diff_list.append(('{}.{}'.format(path, diff_key)[1:], operation, value))

    for diff_key in second_file_keys - first_file_keys:
        add(diff_key, ADDED, second_file[diff_key])

    for diff_key in first_file_keys - second_file_keys:
        add(diff_key, DELETED, first_file[diff_key])

    for diff_key in second_file_keys & first_file_keys:
        if second_file[diff_key] == first_file[diff_key]:
            add(diff_key, NO_CHANGED, second_file[diff_key])
        elif isinstance(first_file[diff_key], dict) and (isinstance(second_file[diff_key], dict)):
            constructor_diff(first_file[diff_key], second_file[diff_key], '{}.{}'.format(path, diff_key), diff_list)
        else:
            add(diff_key, CHANGED, (first_file[diff_key], second_file[diff_key]))
    diff_list.sort()
    return diff_list

generate_diff('/Users/alexandrlelikov/PycharmProjects/python-project-lvl2/tests/fixtures/before.json',
              '/Users/alexandrlelikov/PycharmProjects/python-project-lvl2/tests/fixtures/after.json',
              'json')