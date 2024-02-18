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

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of object to a file in json format,
        first : creates a list of dictionaries using to_dictionary
        , then dump the list into a json file"""

        if ((list_objs is None) or (len(list_objs) == 0)):
            with open(
                    f"{cls.__name__}.json", "w", encoding="utf-8"
                 ) as file:
                list_dict_obj = []
                json_dictionary = Base.to_json_string(list_dict_obj)
                file.write(json_dictionary)
        else:
            list_dict_obj = []
            list_dict_obj = [obj.to_dictionary() for obj in list_objs]
            json_dictionary = Base.to_json_string(list_dict_obj)
            with open(
                    f"{cls.__name__}.json", "w", encoding="utf-8"
                 ) as file:
                file.write(json_dictionary)
