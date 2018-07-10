# coding: utf-8

def class_names(*args):
    names = []
    for arg in args:
        if isinstance(arg, bool):
            continue
        if arg is None:
            continue
        value = str(arg).strip()
        if value:
            names.append(value)
    return ' '.join(names)
