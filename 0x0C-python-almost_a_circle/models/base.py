#!/usr/bin/python3

""" The Module Handles the creation of a Base Class """

import json
import csv
import turtle

class Base():
    """ The Base class of this for all the other Class to inherit from

        Attributes:
            class_attributes:
                __nb_objects(int): The Class Variable of the Class

            instance_attributes:
                identity(int): Instance variables of the Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the Base Class"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json Serialization of list_dictionaries"""

        if list_dictionaries == None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class that saves to a file
            Args:
                list_objs: The list of objects to be converted to dictionary
        """
        dic_list = [obj.to_dictionary() for obj in list_objs]
        cls.to_json_string(dic_list)

        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as file:
            json.dump(dic_list, file)

    @staticmethod
    def from_json_string(json_string):
        """ Deserializes a json string

            Args:
                json_string: The Json strings
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        Returns:
            A new Class 
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1, 1)
            else:
                new_class = cls(1)
            new_class.update(**dictionary)
            return new_class
        
    
    @classmethod
    def load_from_file(cls):
        """
        Return a list of instantiated class from a file of JSON strings.
       
        Returns:
            an empty list - If the file does not exist
            Else - a list of instantiated classes.
        """

        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dictionary = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dictionary]
        except IOError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves CSV serialized list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """

        file_name = cls.__name__ + ".csv"

        with open(file_name, "w", newline="") as csvFile:
            if list_objs is None or list_objs == []:
                csvFile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldNames = ["id", "width", "height", "x", "y"]
                else:
                    fieldNames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvFile, fieldNames=fieldNames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instantiated classes from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            an empty list - If the file does not exist
            Else - a list of instantiated classes.
        """

        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvFile:
                if cls.__name__ == "Rectangle":
                    fieldNames = ["id", "width", "height", "x", "y"]
                else:
                    fieldNames = ["id", "size", "x", "y"]
                list_dictionary = csv.DictReader(csvFile, fieldNames=fieldNames)
                list_dictionary = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dictionary]
                return [cls.create(**d) for d in list_dictionary]
        except IOError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turtle_ = turtle.Turtle()
        turtle_.screen.bgcolor("#b7312c")
        turtle_.pensize(3)
        turtle_.shape("turtle")

        turtle_.color("#ffffff")
        for rect in list_rectangles:
            turtle_.showturtle()
            turtle_.up()
            turtle_.goto(rect.x, rect.y)
            turtle_.down()
            for i in range(2):
                turtle_.forward(rect.width)
                turtle_.left(90)
                turtle_.forward(rect.height)
                turtle_.left(90)
            turtle_.hideturtle()

        turtle_.color("#b5e3d8")
        for sqr in list_squares:
            turtle_.showturtle()
            turtle_.up()
            turtle_.goto(sqr.x, sqr.y)
            turtle_.down()
            for i in range(2):
                turtle_.forward(sqr.width)
                turtle_.left(90)
                turtle_.forward(sqr.height)
                turtle_.left(90)
            turtle_.hideturtle()

        turtle.exitonclick()