# Python program on implementing switch case using the dictionary:
def vowel(num):
	switch={
	  1:'a',
	  2:'e',
	  3:'i',
	  4:'o',
	  5:'u'
	  }
	return switch.get(num,"Invalid input")

vowel(3)

vowel(0)