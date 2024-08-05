#if statement
#else
a=200
b=200
if b>a:
	print("b is greater than a")
elif a==b:
	print("a and b are equal")
#single line:short hand if
a=100
b=50
if a>b: 
	print("a is greater than b")
#short hand if............else
a=10
b=50
print("A") if a>b else print("B")
#multiple else statements on the same line:
a=20
b=30
print("A") if a>b else print("=") if a==b else print("B")
#and
a=100
b =50
c =500
if a > b and c > a:
	print("both conditions are True")
#or
a=100
b=30
c=200
if a>b or a>c:
	print("At least one of the conditions is True")
