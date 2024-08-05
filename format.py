#format in python
print("****************************convert list*************")
sampleset={"yellow","orange","black"}
samplelist=["blue","green","red"]
sampleset.update(samplelist)
print(sampleset)
print("**************intersection**************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1.intersection(set2))
print("*************union****************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1.union(set2))
print("************common element***************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
if set1.isdisjoint(set2):
	print("two sets have no items in common")
else:
	print("two sets have items in common")
	print(set1.intersection(set2))
	