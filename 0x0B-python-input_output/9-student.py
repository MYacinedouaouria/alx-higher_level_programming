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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """

        dictio = {}
        dictio["first_name"] = self.first_name
        dictio["last_name"] = self.last_name
        dictio["age"] = self.age
        return dictio
