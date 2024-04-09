#!/usr/bin/python3
""" unit test for the rectangle class """


import unittest
import pep8

from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """ tests for the rectangle class """

    def setUp(self):
        """
        Instantiate a new rectangle
        """
        self.rect = Rectangle(5, 3)
        self.rct = Rectangle(5, 3, 2, 2)

    def test_rectangle_instantiation(self):
        """
        different tests for the id property
        test for id is None and id has a value
        """
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

        r2 = Rectangle(11, 14)
        self.assertEqual(r2.width, 11)
        self.assertEqual(r2.height, 14)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(12, 15, 5)
        self.assertEqual(r3.width, 12)
        self.assertEqual(r3.height, 15)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 0)

        r4 = Rectangle(12, 15, 5, 6)
        self.assertEqual(r4.width, 12)
        self.assertEqual(r4.height, 15)
        self.assertEqual(r4.x, 5)
        self.assertEqual(r4.y, 6)

        with self.assertRaises(TypeError):
            r5 = Rectangle("12", 15)
        
        with self.assertRaises(TypeError):
            r6 = Rectangle(12, "15")

        with self.assertRaises(TypeError):
            r7 = Rectangle(12, 15, "5")

        with self.assertRaises(TypeError):
            r8 = Rectangle(12, 15, 5, "6")

        with self.assertRaises(ValueError):
            r5 = Rectangle(-12, 15)

        with self.assertRaises(ValueError):
            r6 = Rectangle(12, -15)
        
        with self.assertRaises(ValueError):
            r9 = Rectangle(0, 15)

        with self.assertRaises(ValueError):
            r10 = Rectangle(12, 0)
        
        with self.assertRaises(ValueError):
            r7 = Rectangle(12, 15, -5)

        with self.assertRaises(ValueError):
            r8 = Rectangle(12, 15, 5, -3)
        
    
    def test_rectangle_area(self):
        """
            test the area of the rectangle instance
        """
        r2 = Rectangle(20, 10)
        area = r2.area()
        self.assertEqual(area, 200)
    
    def test_rectangle_update(self):
        """
        test the update function of the rectangle
        class
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (33) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/1")

        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/5 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_rectangle_display(self, mock_stdout):
        """
        test the display function
        """
        expected_output = "#####\n#####\n#####\n"
        self.rect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rectangle_display2(self, mock_stdout):
        """
        test the display function
        """
        expected_output = "\n\n  #####\n  #####\n  #####\n"
        self.rct.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_create():
        """
        test the create function
        """
        dictionaryOne = { 'id': 89 }
        


    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")
