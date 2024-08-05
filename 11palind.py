# Python math: Find the next smallest palindrome of a specified number
import sys
def Next_smallest_Palindrome(num):
	numstr = str(num)
	for i in range(num+1,sys.maxsize):
		if str(i) == str(i)[::-1]:
			return i
print(Next_smallest_Palindrome(99));
print(Next_smallest_Palindrome(1221));

# Find the next previous pallindrome of a specified number
def Previous_Palindrome(num):
	for x in range(num-1,0,-1):
		if str(x) == str(x)[::-1]:
			return x
print(Previous_Palindrome(99));
print(Previous_Palindrome(1221));