print("Enter the Unicode Value: ", end="")
u = int(input())
try:
	ch = chr(u)
	print("\nEquivalent Character =", ch)
except ValueError:
	print("\nInvalid Unicode!")