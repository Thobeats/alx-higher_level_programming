#!/usr/bin/python3
""" unit test for the rectangle class """


import unittest
import pep8

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ tests for the rectangle class """

    def test_rectangle_instantiation(self):
        """
        different tests for the id property
        test for id is None and id has a value
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 3)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
    
    def test_rectangle_properties(self):
        """
            test the setter and getter functions for
            the width property
        """
        r1 = Rectangle(10, 13, 2, 4, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 3)
    
    def test_rectangle_area(self):
        """
            test the area of the rectangle instance
        """

        r2 = Rectangle(20, 10)
        area = r2.area()
        self.assertEqual(area, 200)
        self.assertEqual(r2.id, 1)
    
    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base.py', 'models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")
