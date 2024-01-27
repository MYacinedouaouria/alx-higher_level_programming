#!/usr/bin/python3
"""this module provides the definition of class Square"""


class Square:
    """defines a simple Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrives the size of the square"""

        return self.__size

    @property
    def position(self):
        """retrives tha position of the square"""

        return self.__position

    @size.setter
    def size(self, size=0):
        """sets the size of the square"""

        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, position=(0, 0)):
        """sets the position of the square"""

        if (isinstance(position, tuple) and len(position) == 2):
            if (isinstance(position[0], int) and isinstance(position[1], int)):
                if (position[0] >= 0 and position[1] >= 0):
                    self.__position = position
                else:
                    p1 = "position must be a tuple of 2 positive integers"
                    raise TypeError(p1)
            else:
                p2 = "position must be a tuple of 2 positive integers"
                raise TypeError(p2)
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ returns the current square area"""

        return self.size ** 2

    def my_print(self):
        """prints a square with caracter # in a given position"""

        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for m in range(self.size - 1):
                    print("#", end="")
                print("#")
