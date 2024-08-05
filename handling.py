#handling multiple exception
try:
	a=10/20
	print(a)
	b=[10,20,30,40]
	print(b[1])
except ZeroDivisionError:
	print("denominator can't be zero")
except IndexError:
	print("Invalid Index")