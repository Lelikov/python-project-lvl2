import itertools
import collections
from gendiff.constants import DELETED, ADDED, NO_CHANGED, CHANGED


def dictionary_constructor(path_split, value, result_dict):
    '''
    Constructing path into {a: {b: {...}} view
    :param path_split: Array of the path to the parameter
    :param value: Value
    :param result_dict: Summary dictionary
    :return: Summary dictionary
    '''
    start_value = value
    for key in reversed(path_split):
        value = {key: value}
    if len(path_split) == 1:
        result_dict[path_split[0]] = start_value
    else:
        for key, value in itertools.chain(value.items(), result_dict.items()):
            result_dict[key].update(value)
    return result_dict


def dictionary_constructor_for_json(text_list):
    '''
    Constructing dictionary for json render
    :param text_list: Difference in (path, operation, value) format
    :return: Dictionary
    '''
    result_dict = collections.defaultdict(dict)

    def add(path, new_value, result):
        return dictionary_constructor(path, new_value, result)

    for param in text_list:
        path, operation, value = param
        path_split = path.split('.')
        if isinstance(value, dict):
            while isinstance(value, dict):
                key, value = list(value.keys())[0], list(value.values())[0]
                add(path_split, {key: value}, result_dict)
            add(path_split, {key: {value: operation}}, result_dict)
        elif isinstance(value, tuple):
            add(path_split, {str(value[0]): DELETED, str(value[1]): ADDED}, result_dict)
        else:
            add(path_split, {str(value): operation}, result_dict)
    return result_dict


def difference_constructor(first_file, second_file, path, diff_list):
    '''
    Constructing list in (path, operation, value) format
    :param first_file: Path to first file
    :param second_file: Path to second file
    :param path: Path to parameter
    :return: List in (path, operation, value) format
    '''
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
            difference_constructor(first_file[diff_key], second_file[diff_key],
                                   '{}.{}'.format(path, diff_key), diff_list)
        else:
            add(diff_key, CHANGED, (first_file[diff_key], second_file[diff_key]))
    diff_list.sort()
    return diff_list
