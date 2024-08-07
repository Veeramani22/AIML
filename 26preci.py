# Python math: Get the local and default precision
import decimal
with decimal.localcontext() as context:
	context.prec = 2
	print('Local precision:', context.prec)
	print('22/7 =', (decimal.Decimal('22') / 7))
print()
print('Default precision: ', decimal.getcontext().prec)
print('22 /7 =', (decimal.Decimal('22') / 7))	
