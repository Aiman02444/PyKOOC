# coding: utf-8
# Calculating the area and circumference of a circle
import math  # importing math module of Python for using pi

def circle(radius):  # defining a function called circle
    """Calculates area and circumference of a circle with a radidus""" # a docstring
    
    return math.pi*radius**2, 2*math.pi*radius    # End of a function
def main():
    """An excercise of main function"""
    print(f'The area and circumference of a circle with {x}cm radius\
    are {circle(x)[0]:.2f}cm squared and {circle(x)[1]:.3f}cm.')
    print('Main function is executed!')
    
if __name__ == '__main__':
    x=4
    main()
