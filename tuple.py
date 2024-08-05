#tuple in python
#immutable
#surronded by round brackets(1,1,5)
a=(1,2,5,True,"black")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("madhu")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))
for i in a:
    print(i)
if "black" in a:
    print("black is found")
else:
    print("not found")
    
print(len(a))
a=(1,2)
print(type(a))
a=(1,2,7,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(7))
a=(1,2,7,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x=('priya',)*10
print(x)
a=(1,2,7,4)
print(min(a))
print(max(a))