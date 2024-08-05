#handling diamond problem in py
class A:
	def display(self)
		print("i am the display of class A")
class B(A):
	def display(self):
		print("i am the display of class B")
class c(A):
	def display(self):
		print("i am the display of class c")
class D(B,C):
	def display(self):
		print("i an the display of class D")
o=D()
o.display()