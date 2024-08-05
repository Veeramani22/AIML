#try
print("---------------try-----------")
try:
	x=10
	print(x)
except:
	print("an exception occured")
	print(x)
print("-------------many exception----------")
try:
	print(x)
except NameError:
	print("variable x is not defined")
except:
	print("something else went wrong")
print("------------else----------")
try:
	print(x)
except:
	print("variable x is not defined")
else:
	print("something went wrong")
print("-------------finally----------")
try:
	print(a)
except:
	print("something went wrong")
finally:
	print("the 'try except' is finished")
