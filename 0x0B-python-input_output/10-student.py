#!/usr/bin/python3
"""
    this module defines a class Student
"""


class Student:
    """ defines a student by:
        Public instance attributes:
                              first_name
                              last_name
                              age
        Public instance method: to_json()
    """

    def __init__(self, first_name, last_name, age):
        """ initializes a Studend"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""

        dictio = {}
        if attrs is None:
            return self.__dict__
        elif (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            for a in attrs:
                if hasattr(self, a):
                    dictio[a] = getattr(self, a)
                    return dictio
        else:
            return self.__dict__
