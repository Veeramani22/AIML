# Python program to find the value of permutaion
import math

print("Enter the Value of n: ", end="")
try:
  n = int(input())
  print("Enter the Value of r: ", end="")
  try:
    r = int(input())
	
    numerator = math.factorial(n)
    denominator = math.factorial(n-r)
    perm = numerator/denominator
	
    print("\nPermutation =", perm)
  except ValueError:
    print("\nInvalid Input!")
except ValueError:
  print("\nInvalid Input!")