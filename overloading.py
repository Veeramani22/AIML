#operators overloading in py

a=10
b=20
print(a+b)
a="madhu"
b="priya"
print(a+b)
class Addition:
	def __init__(self,a):
		self.a=a
	def __add__(o1,o2):
		return o1.a+o2.a
	def __sub__(o1,o2):
		return o1.a-o2.a
o1=Addition(10)
o2=Addition(20)
print("Total:",(o1+o2))
print("Difference:",(o1-o2))

		