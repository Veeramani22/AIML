#instance method
class Student:
	name="madhumitha"
	age=21
	def printall(self,gender):
		print("Name:",Student.name)
		print("Age:",Student.age)
		print("Gender:",gender)
o=Student()
o.printall("female")
Student.printall(o,"female")