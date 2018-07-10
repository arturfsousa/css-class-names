# coding: utf-8

def _get_values(*args):
    values = []
    for arg in args:
        if isinstance(arg, bool):
            continue
        if isinstance(arg, (list, tuple, set)):
            values.extend(_get_values(*arg))
            continue
        if arg is None:
            continue
        value = str(arg).strip()
        if value:
            values.append(value)
    return values


def class_names(*args):
    names = _get_values(*args)
    return ' '.join(names)
