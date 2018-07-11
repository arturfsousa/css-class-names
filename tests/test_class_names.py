# coding: utf-8
from unittest import TestCase
from css_class_names import class_names


class ClassNamesStringsTestCase(TestCase):

    def test_simple_case(self):
        names = class_names('foo', 'bar')
        self.assertEqual(names, 'foo bar')

    def test_ignores_empty_spaces(self):
        names = class_names('  foo  ', '   bar  ')
        self.assertEqual(names, 'foo bar')

    def test_ignores_empty(self):
        names = class_names('', 'bar')
        self.assertEqual(names, 'bar')


class ClassNamesNumberTestCase(TestCase):

    def test_simple_case(self):
        names = class_names('foo', 100, 2)
        self.assertEqual(names, 'foo 100 2')

    def test_negative(self):
        names = class_names('foo', -10)
        self.assertEqual(names, 'foo -10')

    def test_zero(self):
        names = class_names('foo', 0)
        self.assertEqual(names, 'foo 0')

    def test_float(self):
        names = class_names('foo', 10.12)
        self.assertEqual(names, 'foo 10.12')


class ClassNamesBoolTestCase(TestCase):

    def test_ignores_true(self):
        names = class_names('foo', True)
        self.assertEqual(names, 'foo')

    def test_ignores_false(self):
        names = class_names('foo', False)
        self.assertEqual(names, 'foo')


class ClassNamesNoneTestCase(TestCase):

    def test_ignores_none(self):
        names = class_names('foo', None)
        self.assertEqual(names, 'foo')


class ClassNamesListTestCase(TestCase):

    def test_simple(self):
        names = class_names('foo', ['bar', 'foobar'])
        self.assertEqual(names, 'foo bar foobar')

    def test_ignores_empty(self):
        names = class_names('foo', [], 'bar')
        self.assertEqual(names, 'foo bar')

    def test_deep(self):
        names = class_names('foo', ['bar', ['second', 'deep'], 'foobar'])
        self.assertEqual(names, 'foo bar second deep foobar')

    def test_tuple(self):
        names = class_names('foo', ('bar', ['second', 'deep'], 'foobar'))
        self.assertEqual(names, 'foo bar second deep foobar')

    def test_ignores_set(self):
        names = class_names('foo', ('bar', set(['second', 'deep']), 'foobar'))
        self.assertEqual(names, 'foo bar foobar')


class ClassNamesDictTestCase(TestCase):

    def test_simple(self):
        names = class_names('foo', {'bar': True})
        self.assertEqual(names, 'foo bar')

    def test_ingnores_falsy_false(self):
        names = class_names('foo', {'bar': False})
        self.assertEqual(names, 'foo')

    def test_ingnores_falsy_none(self):
        names = class_names('foo', {'bar': None})
        self.assertEqual(names, 'foo')

    def test_ingnores_falsy_0(self):
        names = class_names('foo', {'bar': 0})
        self.assertEqual(names, 'foo')

    def test_expressions(self):
        names = class_names('foo', {'bar': 1 == 2})
        self.assertEqual(names, 'foo')


class ClassNamesDedupeTestCase(TestCase):

    def test_without_dedupe(self):
        names = class_names('foo', 'foo', 'bar')
        self.assertEqual(names, 'foo foo bar')

    def test_with_dedupe(self):
        args = ('foo', 'foo', 'bar', {'bar': True}, ['foo'])
        names = class_names(*args, dedupe=True)
        self.assertEqual(names, 'foo bar')


class ClassNamesPrefixTestCase(TestCase):

    def test_adds_prefix(self):
        names = class_names('foo', {'bar': True}, prefix='prefix__')
        self.assertEqual(names, 'prefix__foo prefix__bar')
