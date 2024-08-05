# Python program to sum of first and last digit of a number
print("Enter a Number: ")
num = int(input())

count = 0
while num!=0:
	if count==0:
		last = num%10
		count = count+1
	rem = num%10
	num = int(num/10)
	
sum = rem + last
print("\nSum of first and Last digit =", sum)