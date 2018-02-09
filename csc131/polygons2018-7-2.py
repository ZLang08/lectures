from turtle import Turtle


def square(t: Turtle, length: int) -> None:

    """
    Draw a square with a given length
    :param t: an instance of a Turtle used to render a square
    :param length: the length of the side of a rendered square
    :return: None
    """

    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t: Turtle, length: int) -> None:

    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used to render a square
    :param length: the length of the side of a rendered square
    :return: None
    """

    for count in range(6):
        t.forward(length)
        t.left(60)


def triangle(t: Turtle, length: int) -> None:

    """
    Draw a triangle with a given length
    :param t: an instance of a Turtle used to render a triangle
    :param length: the length of the side of a rendered triangle
    :return: None
    """

    for count in range(3):
        t.forward(length)
        t.left(120)


def octagon(t: Turtle, length: int) -> None:

    """
    Draw an octagon with a given length
    :param t: an instance of a Turtle used to render a octagon
    :param length: the length of the side of a rendered octagon
    :return: None
    """

    for count in range(8):
        t.forward(length)
        t.left(45)


def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:

    """
    Draws a radial pattern of n shapes with the given length
    :param t: a Turtle instance
    :param n: number of shapes
    :param length: length of a shape side
    :param shape: a function for drawing some shape
    :return: None
    """
    for count in range(n):
        shape(t, length)
        t.left(360/n)