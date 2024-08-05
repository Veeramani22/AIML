#Python program - To check perfect number using loop
print(end="Enter the Number: ")
num = int(input())
sum = 0
for i in range(1, num):
	if num%i==0:
		sum = sum+i
if num==sum:
	print("\n" + str(num) + " is a Perfect Number")
else:
	print("\n" + str(num) + " is not a Perfect Number")
	