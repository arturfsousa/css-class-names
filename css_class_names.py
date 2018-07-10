# coding: utf-8

def class_names(*args):
    names = []
    for arg in args:
        names.append(arg)
    return ' '.join(names)
