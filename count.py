# Python program - To count total digits in a number using while loop
print(end="Enter the Number: ")
num = int(input())
tot = 0

while num:
	num = int(num/10)
	tot = tot+1
	
if tot>1:
	print("\nThere are " +str(tot)+ " digits available in the number")
elif tot==1:
	print("\nIt is a single digit number")
	