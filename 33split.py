# Python math: Split fractional and integer parts of a floating point number
import math
print(' (F)  (I)')
for i in range(6):
	print('{}/2 = {} {}'.format(i, i/2, math.modf(i/2.0)))