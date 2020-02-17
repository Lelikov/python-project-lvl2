import itertools


def construction_dictionary(path_split, intermediate_dict, result_dict):
    for key in reversed(path_split):
        intermediate_dict = {key: intermediate_dict}
    for key, value in itertools.chain(intermediate_dict.items(), result_dict.items()):
        result_dict[key].update(value)
    return result_dict
