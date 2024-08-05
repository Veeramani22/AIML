# Python program - property decorator
class PixelTechz:
	def __init__(self, val):
		self.v = val
		
	@property
	def val(self):
		print("\nGetting the Value")
		return self.v
		
	@val.setter
	def val(self, val):
		print("\nNow Setting the Value to \"", val, "\"", sep="")
		self.v = val
		
	@val.deleter
	def val(self):
		print("\nDeleting the Value")
		del self.v
		
a = PixelTechz("Python is fun!")
print(a.val)

a.val = "Python is an Object-oriented PL"
print(a.val)

del a.val