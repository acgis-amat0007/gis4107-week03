"""module to calculate area"""
from math import pi

def get_circle_area(radius):
    """Returns the area of a circle of the given radius
    """
    return(pi*(radius**2))

def get_square_area(side):
    """Returns the area of a square of the given side length"""
    
    return(side**2)

def get_rectangle_area(width, height):
    """Returns the area of a recatangle of given height and width"""
    
    return(width * height)    
