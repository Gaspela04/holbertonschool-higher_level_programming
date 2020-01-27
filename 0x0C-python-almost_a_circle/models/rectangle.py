#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    """*********************"""
    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    """*********************"""
    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    """*********************"""
    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Ser x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    """*********************"""
    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    """*********************"""

    def area(self):
        """
        Area width * height
        """
        return self.width * self.height
    """*********************"""

    def display(self):
        """
        For i in j
        """
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)
    """*********************"""

    def __str__(self):
        """
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
    """*********************"""

    def update(self, *args, **kwargs):
        """
        adding the public method def update(self, *args):
        that assigns an argument to each attribute
        """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
        
