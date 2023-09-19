"""module to calculate area"""
from math import pi

def get_circle_area(radius):
    """Returns the area of a circle of the given radius
    """
    circle_area=pi*(radius**2)
    print(f'{circle_area} m2')

def get_square_area(side):
    """Returns the area of a square of the given side length"""
    square_area=side**2
    print(square_area)
    
