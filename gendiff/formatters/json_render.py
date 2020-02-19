import collections
from gendiff.dictionary_constructor import dictionary_constructor
import json


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
        result_dict = dictionary_constructor(path_split, {str(value): operation}, result_dict)
    return json.dumps(result_dict)
