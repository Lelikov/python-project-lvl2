import collections
from gendiff.formatters.construction_dictionary import construction_dictionary


def json_render(text_array):
    '''
    Render difference to JSON format
    :param text_array: Difference in (path, operation, value) format
    :return: JSON
    '''
    result_dict = collections.defaultdict(dict)
    for param in text_array:
        path, operation, value = param
        path_split = path.split('.')
        if isinstance(value, dict):
            new_value = {str(value).replace('\'', ''): operation}
        else:
            new_value = {str(value): operation}
        result = construction_dictionary(path_split,
                                         new_value, result_dict)
    result = str(result)[:-1]
    return result[result.find('{'):].replace('\'', '"')
