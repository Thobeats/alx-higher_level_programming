#!/usr/bin/python3
import unittest
import pep8

from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_base_instantiation(self):
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

    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base.py', 'models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")
