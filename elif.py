#elif in python
mark=int(input("enter your mark:"))

if(mark<35 and mark>0):
		print("fail")
elif (mark>=35 and mark<60):
		print("grade c")
elif (mark>=60 and mark<80):
		print("grade b")
elif (mark>=80 and mark<=100):
		print("grade a")
		
		
else: 
		print("negative marks provided:please check")