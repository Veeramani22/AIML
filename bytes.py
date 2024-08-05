# Python program to represent the character of a byte for ASCII code
print("Enter the String: ", end="")
s = input()

s = bytes(s, "utf-8")
print(list(s))