#recursive fun
#1*2*3*4*5=120
def factorial(x):
	if x==1:
		return 1
	else:
		return(x*factorial(x-1))
print("factorial:",factorial(5))























