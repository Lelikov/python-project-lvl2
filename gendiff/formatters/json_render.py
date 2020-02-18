import collections
from gendiff.formatters.construction_dictionary import construction_dictionary
import json


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
    print(result[result.find('{'):].replace('\'', '"'))
    return result[result.find('{'):].replace('\'', '"')


a = [('common.setting1', 'no_change', 'Value 1'), ('common.setting2', 'del', '200'),
     ('common.setting3', 'no_change', True), ('common.setting4', 'add', 'blah blah'),
     ('common.setting5', 'add', {'key5': 'value5'}), ('common.setting6', 'del', {'key': 'value'}),
     ('group1.baz', 'change', 'bas->bars'), ('group1.foo', 'no_change', 'bar'), ('group2', 'del', {'abc': '12345'}),
     ('group3', 'add', {'fee': '100500'})]

json_render(a)

# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'), sort_keys=True, indent=4))
print(json.dumps([{'common': {'setting1': {'Value 1': 'no_change'}}}], separators=(',', ':')))#, sort_keys=True, indent=4))
