# Python program to convert decimal to binary without buit-in function
def decimalToBinary(num):

	return "{0:b}".format(int(num))
	
	
# Driver code

if __name__ == '__main__':

	print(decimalToBinary(10))
	
	print(decimalToBinary(64))
	
	print(decimalToBinary(84))
	
	print(decimalToBinary(36))