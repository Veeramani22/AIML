#set in python
thisset={"black","red","blue"}
print(thisset)
thisset={"black","red","blue"}
for x in thisset:
	print (x)
print("---main diff-------")
thisset={"black","red","blue","blue"}
print("-it print unique values---")
print(thisset)
print("---true or false-")
thisset={"black","red","blue"}
print("red" in thisset)
print("------ad value---")
thisset={"black","red","blue"}
thisset.add("yellow")
print(thisset)
print("----remove----")
thisset={"black","red","blue"}
thisset.remove("blue")
print(thisset)
print("-clear-----")
thisset={"black","red","blue"}
thisset.clear()
print(thisset)
print("---copy to other var----")
colours={"black","red","blue"}
x=colours.copy()
print(x)
print("-find len----")
thisset={"black","red","blue"}
print(len(thisset))
x={"black","red","blue"}
y={"google","microsoft","apple"}
z=y.difference(x)
z1=x.difference(y)
print("---y difference----")
print(z)
print("------x difference-")
print(z1)
print("----------update-----")
x={"black","red","blue"}
y={"google","microsoft","apple"}
x.update(y)
print(x)