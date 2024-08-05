# Python program to print multiplication table using recursion 
def tableFun(n, i):
	if(i>10):
		return
	print(n, "*", i, "=", n*i)
	return tableFun(n, i+1)
	
print("Enter a Number: ", end="")
try:
	num = int(input())
	print("\n------Table of", num,"-------")
	tableFun(num, 1)
except ValueError:
	print("\nInvalid Input!")