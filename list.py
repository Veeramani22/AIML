#list in python
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])
print("------------------------------")
a=[1,True,'ram',2.5,[1,2,3,4]]
print(a)
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][1])#meaning 4th index 1st element
print("-----------------------------")
a=[10,25,35,45]
print(a)
a.clear()
print(a)
a=[10,25,35,45]
b=a.copy()
print(b)
a=[10,25,35,45,25,4,25]
print(a.count(25))
print(a.index(25)) #25 what position 
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0) #remove element using index
print(a)
a=[10,25,35,45,25,4,25]
a.remove(25) # remove paricular first values only
print(a)
print("-------------------------------------")
names=["Black"]
print(names)
names.append("madhu")
names.append("ram")
names.append("priya")
print(names)
name2=["dhina","anu"]
names.extend(name2)
print(names)
names.insert(0,"suriya")
print(names)
print("--------------------------------------")
print(list(range(5)))
print(list("madhumitha"))
a=[10,50,100,25,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","zebra"]
a.sort(key=len)
print(a)
    


