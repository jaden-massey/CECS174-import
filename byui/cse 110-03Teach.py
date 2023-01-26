import math

shapes = ['square', 'rectangle', 'circle', None]

def calculate_shape(shape, length, width=None):
    if shape == 'square':
        return length ** 2
    if shape == 'rectangle':
        return length * width
    if shape == 'circle':
        return math.pi * (length ** 2)
    if shape == None:
        aSq = length ** 2
        aCi = math.pi * (length ** 2)
        vCu = length ** 3
        vSp = (4/3) * math.pi * (length ** 3)
        print(f'''
        Area----------
        Square: {aSq}
        Circle: {aCi}
        Volume--------
        Cube: {vCu}
        Sphere: {vSp}''')


def convert(centimeter):
    pass


def get_input():
    for shape in shapes:
        if shape == 'square':
            sLength = float(input('What is the legnth of a side of the square? '))
            print(f' The area of the sqaure is: {calculate_shape(shape, sLength)}')
        if shape == 'rectangle':
            rLength = float(input('What is the length of rectangle? '))
            rWidth = float(input('What is the width of rectangle? '))
            print(f'The area of the rectangle is: {calculate_shape(shape, rLength, rWidth)}')
        if shape == 'circle':
            cRadius = float(input('What is the radius of the circle? '))
            print(f'The area of the circle is: {calculate_shape(shape, cRadius)}')
        if shape == None:
            nLength = float(input('Enter a length: '))
            calculate_shape(shape, nLength)
    
get_input()