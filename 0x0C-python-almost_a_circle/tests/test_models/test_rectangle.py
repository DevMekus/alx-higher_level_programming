#!/usr/bin/python3
""" The test module for the different tests for the Rectangle Class"""


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    """Several Test Cases for the Rectangle"""

    def setUp(self):
        """ The test setup method"""
        self.rectangle1 = Rectangle(4, 6, 2, 1, 12)
        self.rectangle2 = Rectangle(1, 1)
        self.rectangle3 = Rectangle(1, 1)
        self.rectangle4 = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        """ The teardown method"""
        pass

    def test_unrecognized_class_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, 3, 4, 2)

    def test_no_class_arguement(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_skip_width_arg(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1)

    def test_equal_values(self):
        "The test_equal_values method"
        self.assertEqual(self.rectangle1.width, 4)

    def test_instantiation_width_value_error(self):
        """ The test_instantiation_width_value_error method"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def stest_instantiation_height_value_error(self):
        """ The test_instantiation_height_value_error method"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_instantiation_x_value_error(self):
        """The test_instantiation_x_value_error method"""
        with self.assertRaises(ValueError):
            Rectangle(1, 3, x=-1)

    def test_instantiation_y_value_error(self):
        """The test_instantiation_y_value_error method"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, y=-1)

    def test_instantiation_width_type_error(self):
        """The test_instantiation_width_type_error method"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_set_not_isinstance_height(self):
        """The test_set_not_isinstnace_height method"""
        with self.assertRaises(TypeError):
            self.rectangle2.height = "b"

    def test_set_not_isinstance_x(self):
        """The test_set_not_isinstance_x method"""
        with self.assertRaises(TypeError):
            self.rectangle2.x = "l"

    def test_set_not_isinstance_y(self):
        """The test_set_not_isinstance_y method"""
        with self.assertRaises(TypeError):
            self.rectangle2.y = "j"

    def test_instantiation_height_type_error(self):
        """The test_instantiation_height_type_error method"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_instantiation_x_type_error(self):
        """The test_instantiation_x_type_error method"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, x="b")

    def test_instantiation_y_type_error(self):
        """The test_instantiation_y_type_error method"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, x=4, y="b")

    def test_set_not_isinstnace_width(self):
        """The test_set_not_isinstnace_width method"""
        with self.assertRaises(TypeError):
            self.rectangle2.width = "a"

    

    def test_set_not_zero_height(self):
        """The test_set_not_zero_height method"""
        with self.assertRaises(ValueError):
            self.rectangle3.height = 0

    def test_set_not_zero_width(self):
        """The test_set_not_zero_width method"""
        with self.assertRaises(ValueError):
            self.rectangle3.width = 0

    def test_area(self):
        """ The test_area module"""
        self.assertEqual(self.rectangle1.area(), 24)

    def test_unrecognized_area_arg(self):
        """The Unrecognized_area_arg method"""
        with self.assertRaises(TypeError):
            self.rectangle1.area(2)

    def test_update_values(self):
        self.rectangle4.update(89)
        self.assertEqual(
            str(self.rectangle4),
            "[Rectangle] (89) 10/10 - 10/10"
        )

    def test_set_not_zero_x(self):
        """The test_set_not_zero_x method"""
        with self.assertRaises(ValueError):
            self.rectangle3.x = -1
            self.asser

    def test_set_not_zero_y(self):
        """The test_set_not_zero_y method"""
        with self.assertRaises(ValueError):
            self.rectangle3.y = -1

    def test_overide_str(self):
        """The test_overide_str method"""
        self.assertEqual(str(self.rectangle1), "[Rectangle] (12) 2/1 - 4/6")

    def test_overide_str2(self):
        """The test_overide_str2 method"""
        self.assertEqual(str(Rectangle(1, 1, 1, 1, 1)),
                         "[Rectangle] (1) 1/1 - 1/1")

   

    def test_unrecognized_display_arg(self):
        with self.assertRaises(TypeError):
            self.rectangle1.display(3)
            self.rectangle1.to_dictionary(2, 1)    

    def test_update_value(self):
        self.rectangle1.update(1, 2, 3, 4)
        self.assertEqual(
            str(self.rectangle1),
            "[Rectangle] (1) 4/1 - 2/3"
        )

    def test_to_dictionary_value(self):
        self.assertEqual(
            self.rectangle1.to_dictionary(),
            {'id': 12, 'width': 4, 'height': 4, 'x': 2, 'y': 1}
        )

    
