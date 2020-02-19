from gendiff.constants import ADDED, DELETED, CHANGED


def plain_render(plain_list):
    '''
    Render difference to plain format
    :param plain_list: Difference in (path, operation, value) format
    :return: Plain text
    '''

    result_list = []
    for param in plain_list:
        path, operation, value = param
        if operation == CHANGED:
            result_list.append("Property '{}' was changed. "
                               "From '{}' to '{}'".format(path, value[0], value[1]))
        elif operation == ADDED:
            result_list.append("Property '{}' was added with value: "
                               "'{}'".format(path, 'complex value' if isinstance(value,
                                                                                 dict) else value))
        elif operation == DELETED:
            result_list.append("Property '{}' was removed".format(path))
    return '\n'.join(result_list)
