# Python math: Roundup a number to specified digits
import math
def roundup(a, digits=0):
	n = 10**-digits
	return round(math.ceil(a / n) * n, digits)
x = 123.08435
print("Original Number: ",x)
print(roundup(x, 0))
print(roundup(x, 1))
print(roundup(x, 2))
print(roundup(x, 3))