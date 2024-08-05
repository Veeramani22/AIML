# 1.name error exception
try:
	print(a)
except NameError as e:
	print("A is not defined")
try:
	print(10/0)
except ZeroDivisionError as e:
	print("denominator can't be Zero")
try:
	a=int("ram")
except ValueError as e:
	print("please enter numbers only")