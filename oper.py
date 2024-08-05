# Python program to find all four Operations on two sets
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
		intersectionSet = setOne & setTwo
		diffSet = setOne - setTwo
		symDiffSet = setOne ^ setTwo
		print("\nSet A: ", "{", ', '.join(setOne), "}")
		print("Set B: ", "{", ', '.join(setTwo), "}")
		print("\nUnion of A and B =", "{", ', '.join(unionSet), "}")
		print("\nIntersection of A and B =", "{", ', '.join(intersectionSet), "}")
		print("\nDifference of A and B =", "{", ', '.join(diffSet), "}")
		print("\nSymmetric Difference of A and B =", "{", ', '.join(symDiffSet), "}")
	except ValueError:
		print("\nInvalid Input!")
except ValueError:
	print("\nInvalid Input!")