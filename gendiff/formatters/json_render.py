import json
from gendiff.constructors import dictionary_constructor_for_json


def json_render(text_list):
    '''
    Render difference to JSON format
    :param text_list: Difference in (path, operation, value) format
    :return: JSON
    '''
    return json.dumps(dictionary_constructor_for_json(text_list))
