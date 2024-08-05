#Python program to find the Fibonacci Series up to N Term
a = 0 
b = 1
c = 0
print("Enter the Value of n: ", end="")
n = int(input())
print("\nFibonacci series:", a, b, end=" ")
c = a+b
n=n-1
while n>0:
	print(c, end=" ")
	a = b #a=1 a=1
	b = c #b=0 b=1
	c = a+b #1+0=1   1+1=2 2+1=3
	n=n-1