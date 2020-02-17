import itertools


def construction_dictionary(path_split, value, result_dict):
    '''
    Constructing path into {a: {b: {...}} view
    :param path_split: Array of the path to the parameter
    :param value: Value
    :param result_dict: Summary dictionary
    :return: Summary dictionary
    '''
    for key in reversed(path_split):
        value = {key: value}
    for key, value in itertools.chain(value.items(), result_dict.items()):
        result_dict[key].update(value)
    return result_dict
