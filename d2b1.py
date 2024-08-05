# Python program to convert dnum to bnum using list
print("Enter Decimal Number: ",end="")
d = int(input())
i = 0
b = []
while d!=0:  
	b.insert(i, d % 2)  
	i = i+1 
	d = int(d / 2)
	
i = i-1 
print(end="\nEquivalent Binary Value = ")
while i>=0:
	print(end=str(b[i]))
	i =i-1
print()