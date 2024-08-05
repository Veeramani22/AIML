# Python math: Get the nth tetrahedral number from a given integer(n) value
def test(n):
	return (n * (n + 1) * (n + 2)) / 6
n = 1
print("\nOriginal Number:",n)
print("Tetrahedral number:",test(n))
n = 2
print("\nOriginal Number:",n)
print("Tetrahedral number:",test(n))
n = 6
print("\nOriginal Number:",n)
print("Tetrahedral number:",test(n))