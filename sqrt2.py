# Python program to find Square Root using math.pow()
import math

print("Enter a Number: ", end="")
num = int(input())

res = math.pow(num, 0.5)
print("\nSquare Root of %0.2f = %0.2f" %(num,res))
