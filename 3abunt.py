# Python math: find out, if the given number is abundant
def is_abundant(n):
	fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
	return fctr_sum > n #15> 16
print(is_abundant(16))
print(is_abundant(18)) #21>18