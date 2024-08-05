#for in python
course=["web design","php","python"]
for x in course:
	print(x)
for x in "python":
	print(x)
	print("----------------------")
	course=["web design","php","python"]
for x in course:
	print(x)
	if x=="php":
		break
course=["web design","php","python"]
for x in course:
	if x=="php":
	 continue
	print(x)
print("---------------for----------")
course=["web design","php","python"]
for x in course:
	if x=="php":
	 continue
	print(x)
for x in range(6):
	print(x)
print("---------------------")
for x in range(2,30,2):
	print(x)
#else
for  x in range(6):
	print(x)
else:
	print("finally finished")
	adj=["red","big","tasty"]
	fruits=["apple","banana","cherry"]
for x in adj:
	for y in fruits:
		print(x,y)