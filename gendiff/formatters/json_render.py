import collections
from gendiff.formatters.construction_dictionary import construction_dictionary


def json_render(text_array):
    result_dict = collections.defaultdict(dict)
    for param in text_array:
        path, operation, value = param
        path_split = path.split('.')
        if isinstance(value, dict):
            intermediate_dict = {str(value).replace('\'', ''): operation}
        else:
            intermediate_dict = {str(value): operation}
        result = construction_dictionary(path_split,
                                         intermediate_dict, result_dict)
    result = str(result)[:-1]
    return result[result.find('{'):].replace('\'', '"')
