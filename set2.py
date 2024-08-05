#set in python
print("******************convert list***********************")
sampleSet={"yellow","orange","black"}
sampleList={"blue","red","black"}
sampleSet.update(sampleList)
print(sampleSet)
print("************************intersection*****************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1.intersection(set2))
print("**********************union*****************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1.union(set2))
print("*******************commom element*******************")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
if set1.isdisjoint(set2):
	print("two sets have no items in common")
else:
	print("two sets have items in common")
	print(set1.intersection(set2))