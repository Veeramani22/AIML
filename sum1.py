# Python program to sum of first and last digit of a number enters a invalid input
print("Enter a Number: ", end="")
try:
	num = int(input())
	
	count = 0
	while num != 0:
		if count == 0:
			last = num % 10
			count = count + 1
		rem = num % 10
		num = int(num / 10)
	
	print("\nFirst Digit (", rem, ") + Last Digit (", last, ") =", rem + last)
	
except ValueError:
	print("\nInvalid Input!")