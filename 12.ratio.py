# python math: convert a float into ratio
from fractions import Fraction
value= 4.2
print(Fraction (value).limit_denominator())