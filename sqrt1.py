# Python programs to find square root using math.sqrt() inbuilt function
import math

print("Enter a Number: ", end="")
try:
	num = int(input())
	res = math.sqrt(num)
	print("\nSquare Root of " +str(num)+ " = " +str(res))
except ValueError:
	print("\nInvalid Input!")