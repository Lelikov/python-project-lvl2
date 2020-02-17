def plain_render(plain_array):
    array = []
    for param in plain_array:
        path, operation, value = param
        if operation == 'change':
            before_change, after_change = value.split('->')
            array.append("Property '{}' was changed. "
                         "From '{}' to '{}'".format(path, before_change, after_change))
            continue
        elif operation == 'no_change':
            continue
        oper = {
            'del': "Property '{}' was removed".format(path),
            'add': "Property '{}' was added with value: "
                   "'{}'".format(path, 'complex value' if isinstance(value, dict) else value),
        }
        array.append(oper[operation])
    return '\n'.join(array)
