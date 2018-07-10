# coding: utf-8
from unittest import TestCase
from css_class_names import class_names


class CssClassNamesTestCase(TestCase):

    def test_primitive_values(self):
        names = class_names('foo', 'bar')
        self.assertEqual(names, 'foo bar')
