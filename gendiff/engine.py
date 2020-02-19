from gendiff.parsers import parse_json, parse_yaml
from gendiff.formatters import json_render, plain_render, text_render
import os.path
from gendiff.constructors import difference_constructor

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
        result = RENDER[format](difference_constructor(first_file, second_file, '', diff_list))

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
