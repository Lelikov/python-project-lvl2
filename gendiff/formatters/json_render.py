import collections
from gendiff.dictionary_constructor import dictionary_constructor
import json
from gendiff.constants import DELETED, ADDED


def json_render(text_list):
    '''
    Render difference to JSON format
    :param text_list: Difference in (path, operation, value) format
    :return: JSON
    '''
    result_dict = collections.defaultdict(dict)
    for param in text_list:
        path, operation, value = param
        path_split = path.split('.')
        if isinstance(value, dict):
            while isinstance(value, dict):
                for new_key, new_value in value.items():
                    value = new_value
                result_dict = dictionary_constructor(path_split, {new_key: new_value}, result_dict)
            result_dict = dictionary_constructor(path_split, {new_key: {new_value: operation}},
                                                 result_dict)
        elif isinstance(value, tuple):
            result_dict = dictionary_constructor(path_split, {str(value[0]): DELETED, str(value[1]): ADDED}, result_dict)
        else:
            result_dict = dictionary_constructor(path_split, {str(value): operation}, result_dict)
    return json.dumps(result_dict)