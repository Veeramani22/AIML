class user:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@property
	def msg(self):
		return self.name+"is"+str(self.age)+"years old"
	
o=user("madhumitha",21)
print(o.name)
print(o.age)
print(o.msg)
o.age=45
print(o.msg)