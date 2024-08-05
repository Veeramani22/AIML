# Python program - to find and print ASCII value of a character
print("Enter a Character: ", end="")
ch = input()

chlen = len(ch)
if chlen==1:
	asc = ord(ch)
	print("\nASCII Value of \"" +(ch)+ "\" = " +str(asc))
else:
	print("\nInvalid Input!")