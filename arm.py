# Python program to find armstrong in an interval
lower = 100
upper = 2000

for numb in range(lower, upper + 1):

	# order of number
	ord = len(str(numb))
	
	# initialize sum
	sum = 0
	tem = numb
	
	while tem > 0:	#153>o:
	
		rem = tem % 10	#153%10=3  15.3%10
		sum += rem ** ord #27
		tem//= 10
	
	if numb == sum:
		print("The Armstrong numbers are: ",numb)
		