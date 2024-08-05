# Python program to find average of n numbers using while loop
print("Enter the Value of n: ", end="")
n = int(input())
print("Enter " +str(n)+ " Numbers: ", end="")
nums = []
i = 0
while i<n:
	nums.append(int(input()))
	i = i+1

sum = 0
i = 0
while i<n:
	sum = sum+nums[i]
	i = i+1
	
avg = sum/n
print("\nAverage = ", avg)