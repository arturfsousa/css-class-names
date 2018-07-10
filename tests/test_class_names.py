# coding: utf-8
from unittest import TestCase
from css_class_names import class_names


class ClassNamesStringsTestCase(TestCase):

    def test_simple_case(self):
        names = class_names('foo', 'bar')
        self.assertEqual(names, 'foo bar')

    def test_removes_empty_spaces(self):
        names = class_names('  foo  ', '   bar  ')
        self.assertEqual(names, 'foo bar')

    def test_removes_empty(self):
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

    def test_removes_true(self):
        names = class_names('foo', True)
        self.assertEqual(names, 'foo')

    def test_removes_false(self):
        names = class_names('foo', False)
        self.assertEqual(names, 'foo')


class ClassNamesNoneTestCase(TestCase):

    def test_removes_none(self):
        names = class_names('foo', None)
        self.assertEqual(names, 'foo')


class ClassNamesListTestCase(TestCase):

    def test_simple(self):
        names = class_names('foo', ['bar', 'foobar'])
        self.assertEqual(names, 'foo bar foobar')

    def test_removes_empty(self):
        names = class_names('foo', [], 'bar')
        self.assertEqual(names, 'foo bar')

    def test_deep(self):
        names = class_names('foo', ['bar', ['second', 'deep'], 'foobar'])
        self.assertEqual(names, 'foo bar second deep foobar')

    def test_tuple(self):
        names = class_names('foo', ('bar', ['second', 'deep'], 'foobar'))
        self.assertEqual(names, 'foo bar second deep foobar')

    def test_set(self):
        names = class_names('foo', ('bar', set(['second', 'deep']), 'foobar'))
        self.assertEqual(names, 'foo bar second deep foobar')
