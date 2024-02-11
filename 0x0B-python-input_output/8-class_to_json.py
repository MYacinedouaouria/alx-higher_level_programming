#!/usr/bin/python3
""" this module suplies on functio, class_to_json()"""


def class_to_json(obj):
    """
        serializes a instance of a class into a dictionary suitable for json
        serialisation
        Args:
            obj: an instance of a class
        Returns: A dictionary representation of the object.
    """

    attributes = obj.__dict__
    serialized = {}
    for key, value in attributes.items():
        if (isinstance(value, (str, int, bool))):
            serialized[key] = value
        elif (isinstance(value, dict)):
            serialized[key] = value.copy()
        elif (isinstance(value, list)):
            serialized[key] = value.copy()
    return serialized
