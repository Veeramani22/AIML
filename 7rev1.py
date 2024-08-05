# Python program to check reverse equals original
print(end="Enter the Number: ")
n = int(input())

rev = 0
o = n
while n>0:
	rem = n % 10 #4 2
	rev = rem + (rev*10) #4+(0*10)=4 2
	n = int(n / 10)

if o==rev:
	print("\n" +str(o)+ " (Original) = " +str(rev)+ " (Reverse)")
else: 
	print("\n" +str(o)+ " (Original) != " +str(rev)+ " (Reverse)")