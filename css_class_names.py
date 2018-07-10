# coding: utf-8

def _get_values(*args):
    values = []
    for arg in args:
        if isinstance(arg, bool):
            continue
        elif isinstance(arg, (list, tuple)):
            values.extend(_get_values(*arg))
            continue
        elif arg is None:
            continue
        elif isinstance(arg, (str, int, float)):
            value = str(arg).strip()
            if value:
                values.append(value)
    return values


def class_names(*args):
    names = _get_values(*args)
    return ' '.join(names)
