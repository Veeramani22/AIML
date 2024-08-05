# Python program - To print ASCII values of all characters
print("Enter a String: ", end="")
text = input()

textlen = len(text)
for ch in text:
	asc = ord(ch)
	print(ch, "\t", asc)