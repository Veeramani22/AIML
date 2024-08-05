#keyword in python
print("-------------break--------------")
for i in range(9):
	if i > 3:
	 break
	print(i)
print("-------------break--------------")
for i in range(9):
    if i==5:
      continue #go to next loop
    print(i)
i=0
while i<9:
    i +=1
    if i==7:
      continue
    print(i)
print("-------------def--------------")
def my_function():
	print("function assign")
my_function()
print("-----------del-----------------")
x="evening"
print(x)