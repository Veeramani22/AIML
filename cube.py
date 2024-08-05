# Python program exception handling(try, except, finally, raise)
print("Enter a number: ", end="")
num = input()

try:
	num = int(num)
	cub = num*num*num
	print("\nCube =", cub)
except:
	print("\nInvalid Input!")
	