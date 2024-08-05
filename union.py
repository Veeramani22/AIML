# Python program to find union of sets
print("Enter Size of Set A: ", end="")
try:
	tota = int(input())
	print("Enter", tota, "Elements: ", end="")
	numsOne = []
	for i in range(tota):
		numsOne.append(input())
	setOne = set(numsOne)
	
	print("\nEnter Size of Set B: ", end="")
	try:
		totb = int(input())
		print("Enter", totb, "Elements: ", end="")
		numsTwo = []
		for i in range(totb):
			numsTwo.append(input())
		setTwo = set(numsTwo)
		
		unionSet = setOne | setTwo 
		print("\nSet A: ", "{", ', '.join(setOne), "}")
		print("Set B: ", "{", ', '.join(setTwo), "}")
		print("\nUnion of A and B =", "{", ', '.join(unionSet), "}")
	except ValueError:
		print("\nInvalid Input!")
except ValueError:
	print("\nInvalid Input!")