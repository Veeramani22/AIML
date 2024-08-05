#Python program to find the perimeter and area of a triangle with a given height
import math
b = float(input("Input the base of the triangle: "))
a = float(input("Input the side of the triangle: "))
c = float(input("Input the side of the triangle: "))
p = a + b + c
h = int(input("Input height of the triangle: ")) 
area = 1/2 * b* h
print("The perimeter of the triangle is: ", p)
print("The area of the triangle is: ", area)