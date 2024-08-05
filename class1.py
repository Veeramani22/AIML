#class methods
class Student:
	name="madhumitha"
	age=21
	def printall():
		print("Name:",Student.name)
		print("Age:",Student.age)
Student.printall()
print(Student.__dict__)
print(getattr(Student,"printall"))
getattr(Student,"printall")()
Student.__dict__['printall']()
