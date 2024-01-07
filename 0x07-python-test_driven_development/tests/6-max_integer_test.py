#!/usr/bin/python3

"""An Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""    

    def test_empty_list(self):
        """Tests an empty list."""
        emptyList = []
        self.assertEqual(max_integer(emptyList), None)

    def test_one_element_list(self):
        """A list with a single element."""
        oneElement = [7]
        self.assertEqual(max_integer(oneElement), 7)
    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [5, 4, 3, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_string(self):
        """Test a string."""
        string = "Nnaji"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Nnaji", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
