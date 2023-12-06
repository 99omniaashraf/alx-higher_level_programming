#!/usr/bin/python3
"""class module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialized method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrievers a dictionary representation of student instance.


        Args:
            attrs: attributes

        Return: dictionary
        """
        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance.


        Args;
            json: dictionary of attributes
        """
        for x in json:
            self.__dict__.update({x: json[x]})
