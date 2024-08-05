# Python program on implementing the switch case
class Months: 
	def switchCase(self, month_number):
		default = "Oops! Wrong Input"
		return getattr(self, 'month_' + str(month_number), lambda: default)()
	def month_1(self):
		return "January" 
	def month_2(self):
		return "February"
	def month_3(self):
		return "March"
	def month_4(self):
		return "April"
		def month_5(self):
			return "June"
result = Months()
print(result.switchCase(3))
print(result.switchCase(5))
print(result.switchCase(9))