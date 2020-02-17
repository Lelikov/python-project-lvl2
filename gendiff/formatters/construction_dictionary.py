import itertools


def construction_dictionary(path_split, value, result_dict):
    '''
    Constructing path into {a: {b: {...}} view
    :param path_split: Array of the path to the parameter
    :param value: Value
    :param result_dict: Summary dictionary
    :return: Summary dictionary
    '''
    start_value = value
    for key in reversed(path_split):
        value = {key: value}
    if len(path_split) == 1:
        result_dict[path_split[0]] = start_value
    else:
        for key, value in itertools.chain(value.items(), result_dict.items()):
            result_dict[key].update(value)
    return result_dict
