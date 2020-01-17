#!/usr/bin/python3
class Rectangle:
    """Create class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter"""
        if self.area() is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        newstring = ""
        if self.width is 0 or self.height is 0:
            return newstring
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        return "Rectangle(%s, %s)" % (self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
