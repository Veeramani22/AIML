#Python program to display the given integer in reverse manner
number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0): #25!=0
	digit = number%10 #25%10=5  2
	rev = (rev*10)+digit #0*10+5=5 2
	number = number//10  #25/10
print(rev)
