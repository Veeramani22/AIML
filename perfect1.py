# Python program - To check perfect number using while loop
print(end="Enter the Number: ")
num = int(input())
sum = 0
i = 1
while i<num:
	if num%i==0:
		sum = sum+i
	i = i+1
if num==sum:
	print("\n" + str(num) + " is a Perfect Number")
else:
	print("\n" + str(num) + " is not a Perfect Number")