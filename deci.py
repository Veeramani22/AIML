# Python program to convert decimal to binary
def DecimalToBinary(number):
	
	
	if number >= 1:
	
		DecimalToBinary(number // 2)
	
	print(number % 2, end = '')
	
	
# Driver Code

if __name__ == '__main__':


	# decimal value
	
	decimal_val = 17
	
	# Calling function
	
	DecimalToBinary(decimal_val)