# Python program to convert two lists into dictionary
listR = ["Mon", "Tue", "Wed"]
listS = [3, 6, 5]
# Given lists
print("list of R : ", listR)
print("list of S : ", listS)
# Empty dictionary
res = {}
# Convert to dictionary
for key in listR:
	for value in listS:
		res[key] = value
		listS.remove(value)
		break
print("Dictionary from lists :\n ",res)