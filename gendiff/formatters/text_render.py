from gendiff.constructors import dictionary_constructor
import collections
from gendiff.constants import ADDED, DELETED, CHANGED, NO_CHANGED

CHANGE_SYMBOL = {
    ADDED: '+',
    DELETED: '-',
    NO_CHANGED: ' ',
    CHANGED: ''
}


def text_render(text_list):
    '''
    Render difference to text format
    :param text_list: Difference in (path, operation, value) format
    :return: Text
    '''
    result_dict = collections.defaultdict(dict)
    for param in text_list:
        path, operation, value = param
        path_split = path.split('.')
        path_split[-1] = '{} {}'.format(CHANGE_SYMBOL[operation], path_split[-1])
        result_dict = dictionary_constructor(path_split, value, result_dict)
    result_list = ['{']
    result_list = text_render_print(result_dict, result_list, 1)
    result_list.append('}')
    return '\n'.join(result_list)


def text_render_print(dictionary, result_list, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result_list.append('{}{}: {{'.format('  ' * indent, str(key)))
            text_render_print(value, result_list, indent + 2)
            result_list.append('  ' * indent + '}')
        elif isinstance(value, tuple):
            def add(sign, value):
                result_list.append('{}{} {}: {}'.format('  ' * indent, sign, key[1:], value))

            add('-', value[0])
            add('+', value[1])
        else:
            result_list.append('{}{}: {}'.format('  ' * indent, str(key), str(value)))
    return result_list
