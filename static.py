#static method in pyclass student:
class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def printDetail(self):
		print("Name:",self.name,"age:",self.age)
	@staticmethod
	def welcome():
		print("welcome to our institutions")
s1=student("Ram",25)
s1.printDetail()
s1.welcome()

s2=student("Raja",29)
s2.printDetail()
s2.welcome()