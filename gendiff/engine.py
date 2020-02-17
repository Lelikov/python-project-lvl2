from gendiff.parsers import parse_json, parse_yaml
from gendiff.formatters import json_render, plain_render, text_render


def constructor_diff(before, after, path, diff_array):
    before_keys = set(before.keys())
    after_keys = set(after.keys())
    for diff_key in after_keys - before_keys:
        diff_array.append(('{}.{}'.format(path, diff_key)[1:],
                           'add', after[diff_key]))
    for diff_key in before_keys - after_keys:
        diff_array.append(('{}.{}'.format(path, diff_key)[1:],
                           'del', before[diff_key]))
    for diff_key in after_keys & before_keys:
        if isinstance(before[diff_key], dict):
            constructor_diff(before[diff_key], after[diff_key],
                             '{}.{}'.format(path, diff_key), diff_array)
        elif after[diff_key] == before[diff_key]:
            diff_array.append(('{}.{}'.format(path, diff_key)[1:],
                               'no_change', after[diff_key]))
        else:
            diff_array.append(('{}.{}'.format(path, diff_key)[1:], 'change',
                               '{}->{}'.format(before[diff_key],
                                               after[diff_key])))
    return sorted(diff_array)


def generate_diff(path_to_file1, path_to_file2, format):
    first_file_extension = path_to_file1[path_to_file1.rfind('.'):]
    second_file_extension = path_to_file2[path_to_file2.rfind('.'):]

    extension = ['.json', '.yml']
    if not (first_file_extension or second_file_extension) in extension:
        print('Unsupported type of files. Supported only .json and .yml')
        return 'Unsupported type of files'

    file_type = {
        '.json': parse_json(),
        '.yml': parse_yaml()
    }
    try:
        before = file_type[first_file_extension](path_to_file1)
    except FileNotFoundError:
        print('First file not found')
        return 'First file not found'
    try:
        after = file_type[second_file_extension](path_to_file2)
    except FileNotFoundError:
        print('Second file not found')
        return 'Second file not found'

    render = {
        'text': text_render.text_render,
        'plain': plain_render.plain_render,
        'json': json_render.json_render
    }
    try:
        diff_array = []
        result = render[format](constructor_diff(before, after, '', diff_array))
    except KeyError:
        print('Incorrect output format. Choose plain, text or json')
        return 'Incorrect output format'
    print(result)
    return result
