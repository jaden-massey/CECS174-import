# ax^2 + bx + c = 0

import math

print('Welcome to my Quadratic Solver! \n '
      '\na, b, and c and the coefficients found in the standard quadratic equation, ax^2+bx+c \n '
      '\nPlease input them in the prompts below: \n')

numA = float(input('What is the coefficient of the first term? (a) \n'))
numB = float(input('What is the coefficient of the second term? (b) \n'))
numC = float(input('What is the coefficient of the second term? (c) \n'))

discriminant = numB ** 2 - 4 * numA * numC

if discriminant < 0:
    print('This quadratic has no real solution')
    exit(1)
    # Prevents negatives under the square root

elif numA == 0:
    print('Error: This is not a quadratic')
    exit(1)
    # Prevents division by 0 in the quadratic formula

else:

    x1 = (-numB + math.sqrt(discriminant)) / (2 * numA)
    x2 = (-numB - math.sqrt(discriminant)) / (2 * numA)

    x1 = round(x1, 3)
    x2 = round(x2, 3)

    print(f'The solutions to the quadratic equation, {numA}x^2 + {numB}x + {numC}, are the x values: ({x1},{x2})')