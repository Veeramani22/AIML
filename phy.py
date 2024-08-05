#To solve the following equations using the python programs
def solve_equation(v=None, t=None, s=None):
	if v is not None and t is not None:
		return v * t   # s case
	elif s is not None and t:  # t not None and not 0
		return s / t   # v case
	else:
		raise ValueError   #"t should be defined or not zero"
		
		
print(solve_equation(v=10, t=2))
print(solve_equation(s=2, t=7))