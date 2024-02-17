#!/usr/bin/python3
import unittest
import pep8

from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    
    def test__init__(self):
        """
        different tests for the id property
        test for id is None and id has a value
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)
    
    def test_to_json_string(self):
        """
        test the to json string function in the Base Class
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertDictEqual(dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")
