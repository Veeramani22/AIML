x={"f","e","d","c","b","a"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)
x={"f","e","d","c","b"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.difference_update(y)
print(x)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.intersection(y)
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
result=x.intersection(y,z)
print(result)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.isdisjoint(y)
print(z)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.isdisjoint(y)
print(z)
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=x.union(y)
print(z)
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
result=x.union(y,z)
print(result)
print(z)

