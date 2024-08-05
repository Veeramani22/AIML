#FUNCTION OVERRIDING
class Employee:
	def WorkingHrs(self):
		self.hrs=50
	def printHrs(self):
		print("Total Working Hrs:",self.hrs)
class Trainee (Employee):
	def WorkingHrs(self):
		self.hrs=60
	def resetHrs(self):
		super().WorkingHrs()
employee=Employee()
employee.WorkingHrs()
employee.printHrs()#base class employee hrs 
trainee=Trainee()
trainee.WorkingHrs()
trainee.printHrs()#derived class employee hrs
trainee.resetHrs()
trainee.printHrs()#base class hrs insert..because super()inbulit function