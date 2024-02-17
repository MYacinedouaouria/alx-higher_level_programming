#!/usr/bin/python3
""" this module defines a class called 'Base'"""

import json


class Base:
    """ defines class Base with:
        private class attribute : __nb_objects initialized to 0
        class constructor: def __init__(self, id=None):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a Base instance,
        if id is not None then we assign the public instance attribute id
        with this argument value
        otherwise, we increment __nb_objects and assign the new value to the
        public instance attribute id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset_nb_objects(cls):
        """ reset the counter of objects to 0"""

        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""

        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
