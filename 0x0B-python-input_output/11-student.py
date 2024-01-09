#!/usr/bin/python3
"""Definition of a Student Class."""


class Student:
    """A Template of a Student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary representation of a Student. 

        Args:
            attrs (list): (Optional) The attributes to represent.
        """

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Method Replaces all attributes of the Student.

        Args:
            json (dict): The pairs to replace attributes with.
        """
        
        for k, v in json.items():
            setattr(self, k, v)
