#!/usr/bin/python3
""" test for the Square Class """


import unittest
import pep8

from models.square import Square


class TestSquare(unittest.TestCase):
    """ tests for the square class """

    def test_square_instantiation(self):
        """
        different tests for the id property
        test for id is None and id has a value
        """
        r3 = Square(24, 45, 16, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 24)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)
    
    def test_square_area(self):
        """
            test the area of the square instance
        """

        r2 = Square(20)
        area = r2.area()
        self.assertEqual(area, 400)
        # self.assertEqual(r2.id, 9)

    # def test_square_update(self):
    #     """
    #     test the update function of the sqaure
    #     class
    #     """

    #     r1 = Square(5)
    #     self.assertEqual(r1.__str__(), "[Square] (10) 0/0 - 5")

    #     r1.update(10)
    #     self.assertEqual(r1.__str__(), "[Square] (10) 0/0 - 5")

    #     r1.update(1, 2)
    #     self.assertEqual(r1.__str__(), "[Square] (1) 0/0 - 2")

    #     r1.update(1, 2, 3)
    #     self.assertEqual(r1.__str__(), "[Square] (1) 3/0 - 2")

    #     r1.update(1, 2, 3, 4)
    #     self.assertEqual(r1.__str__(), "[Square] (1) 3/4 - 2")

    #     r1.update(x=12)
    #     self.assertEqual(r1.__str__(), "[Square] (1) 12/4 - 2")

    #     r1.update(size=7, y=1)
    #     self.assertEqual(r1.__str__(), "[Square] (1) 12/1 - 7")

    #     r1.update(size=7, id=89, y=1)
    #     self.assertEqual(r1.__str__(), "[Square] (89) 12/1 - 7")

    
    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")