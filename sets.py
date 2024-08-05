names={'priya','madhu','meena'}
print(names)
print(type(names))
#access values using for loop
for name in names:
    print(name)
#adding new element
names.add('sara')
print(names)
#update another set of data
a={'anu','dhina','nisha'}
names.update(a)
print(names)
names.remove('sara')
print(names)
names.discard('anu')
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names

names={'priya','madhu','meena','anu','dhina','nisha','sara','priya'}
print(names)
a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)
