#!/usr/bin/python3

""" Test model for the Base Class"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test Model for the base class """
    def setUp(self) -> None:
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base()

    def test_num_of_obj(self):
        """ The test_num_of_obj method"""
        self.assertEqual(self.base3.id, self.base2.id + 1)

    def test_num_of_obj2(self):
        """ The test_num_of_obj2 method"""
        self.assertEqual(self.base3.id, self.base1.id + 2)

    def test_accessing_nb_objects(self):
        """ The test_accessing_nb_objects method """
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_passing_unrequired_arg(self):
        """ The test_passing_unrequired_arg method"""
        with self.assertRaises(TypeError):
            Base(3, 2)

    def test_from_json_string(self):
        """ The test_from_json_string method"""
        # Test case when the input is a valid JSON string
        json_str = '[{"name": "John", "age": 25},{"name": "Alice", "age": 30}]'
        result = Base.from_json_string(json_str)
        expected_result = [{'name': 'John', 'age': 25},
                           {'name': 'Alice', 'age': 30}]
        self.assertEqual(result, expected_result)

        # Test case when the input is an empty JSON string
        result_empty = Base.from_json_string('')
        self.assertEqual(result_empty, [])

        # Test case when the input is None
        result_none = Base.from_json_string(None)
        self.assertEqual(result_none, [])
