#Python program to calculate the SI
def calculateSI(a, b, c):
	return (a*b*c)/100
print(end="Enter the Amount: ")
p = int(input())
print(end="Enter the Rate of Interest: ")
r = float(input())
print(end="Enter the Time: ")
t = float(input())
si = calculateSI(p, r, t)
print("\nSimple Interest = " + str(si))