#try except in py
try:
	value=100/2
	num=int(input("Enter the number:"))
	print(num)
except ZeroDivisionError:
	print("dividing by 0")
except ValueError:
	print("Invalid Input")
finally:
	print("Thanking you")