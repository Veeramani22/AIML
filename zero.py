#zero error
try:
	a=[10,20,30,40]
	print(a[10])
except IndexError as e:
	print("Invalid Index")
