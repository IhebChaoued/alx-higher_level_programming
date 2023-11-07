#!/usr/bin/python3
"""Student class definition"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
