#Python program to find the circumference and area of a rectangle with a given length
import math
l = int(input("Input the length of the rectangle: "))
h = int(input("Input the height of the rectangle: "))
c = 2 * (l + h)
area = l * h
print("The circumference of the rectangle is: ", c)
print("The area of the rectangle is: ", area)