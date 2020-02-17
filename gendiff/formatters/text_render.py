import collections
from gendiff.formatters.construction_dictionary import construction_dictionary


def text_render(text_array):
    result_dict = collections.defaultdict(dict)
    for param in text_array:
        path, operation, new_value = param
        path_split = path.split('.')
        change_symbol = {'add': '+', 'del': '-', 'no_change': ' ', 'change': ''}
        path_split[-1] = '{} {}'.format(change_symbol[operation], path_split[-1])
        intermediate_dict = new_value
        result = construction_dictionary(path_split, intermediate_dict, result_dict)
    array = ['{']
    result = text_render_print(result, array, 1)
    result.append('}')
    return '\n'.join(result)


def text_render_print(dictionary, array, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            array.append('{}{}: {{'.format('  ' * indent, str(key)))
            text_render_print(value, array, indent + 2)
            array.append('  ' * indent + '}')
        elif '->' in str(value):
            for change_value, sign in zip(str(value).split('->'), ['-', '+']):
                array.append('{}{} {}: {}'.format('  ' * indent,
                                                  sign, key[1:], change_value))
        else:
            array.append('{}{}: {}'.format('  ' * indent, str(key), str(value)))
    return array
