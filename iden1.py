#identity operator
#to compare object-same-true
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
#returns true because z is the same object as xrange
print(x is z)
#returns false because x is not the same object as y,even if they have the same content
print(x==y)
#to democonstrate the difference between "is" and "==":
#this comparision returns true because x is equal to yeild
x=["apple","bananaaa"]
y=["apple","banana"]
z=x
print(x is not z)
#returns false because z is the same object as xrange
print(x is not y)
#returns true because x is not the same object as y, even if they have the same content
print(x!=y)
#to demonstrate the difference between"is not" and "!=":this comparision returns false