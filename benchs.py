# coding: utf-8
import cProfile
import timeit
from css_class_names import class_names

if __name__ == '__main__':
    target = "class_names('foo', {'bar': True}, [['foo', 'bar']], dedupe=True)"
    duration = timeit.timeit(target, globals={"class_names": class_names})
    print('Time: {}'.format(duration))
    cProfile.run(target)
