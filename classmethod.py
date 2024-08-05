#class method decorator is python
class student:
	count=0
	def _init_(self,name,age):
		self.name=name
		self.age=age
		student.count+=1
	def printDetail(self):
		print("Name:",self.name,"age:",self.age)
	@classmethod
	def total(cls):
		return cls.count
o=student("Ram",25)
o.printDetail()
print("Total Admission:",o.total())
a=student("Raja",29)
a.printDetail()
print("Total Admission:",student.total())
print("Total Admission:",o.total())