# Python program to solve quadratic equations
import math

# Solving Quadratic Equation
print("Enter 'a', 'b', and 'c' values to solve the quadratic equation (precise value)")

# User input
a = int(input('Enter "a" value: '))
b = int(input('Enter "b" value: '))
c = int(input('Enter "c" value: '))

# Solving the equation
val1 = b * -1
val2 = (b**2) - (4 * a * c)
val3 = math.sqrt(val2)
val4 = val1 + val3
val5 = val1 - val3
val6 = 2 * a
finalAns = val4 / val6
finalAns2 = val5 / val6

# Printing final answers
print("Root 1:", finalAns)
print("Root 2:", finalAns2)
