#class atribute
class student():
	name="madhu"
	age=20
#getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attribute found')) #gender not in class but using so error attr use in clear
#dot notation
print(student.name)
print(student.age)
#setattr new attr create
setattr(student,'name','priya')
print(student.name)
setattr(student,'gender','female')
print(student.gender)
student.city="trichy"
print(student.city)
print(student.__dict__)

delattr(student,"city")
print(student.__dict__)