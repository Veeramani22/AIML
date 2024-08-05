#Python program to find the volume and area of a sphere with a given radius
import math
r = float(input("Input the radius of the sphere: "))
c = 4/3 * math.pi * r * r * r
area = 4 * math.pi * r * r
print("The circumference of the sphere is: ", c)
print("The area of the sphere is: ", area)
