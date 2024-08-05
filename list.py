#list in python
print("-----list must have square bracate----------")
thislist=["apple","banana","cherry"]
print("-------print list[i]-----")
print(thislist[1])
print("-------------print full list-------")
print(thislist)
this=["apple","banana","cherry"]
this[1]="blackcurrant"
print("-----------change banana to blackcurrant in list[i]---------")
print(this)
print("---------check the list using if--------")
thislist=["apple","banana","cherry"]
if ("mango" in thislist):
	print("yes,'mango' is in the fruits list")
else:
	print("no")
print("---------to find the len of-----")
print(len(thislist))
print("-------------add value to list----")
thislist=["apple","banana","cherry"]
print("---------add value to list before----")
print(thislist)
print("---------add value to list after----")
print(thislist)
print("------------insert(move)---------")
thislist.insert(1,"orange")
thislist.insert(5,"banana")
print(thislist)
thislist.reverse()
print(thislist)
print("-----pop the val---")
thislist.pop()
print(thislist)
