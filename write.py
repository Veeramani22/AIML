 #write to an exsiting file in python
try:
	file=open("new\\rohit.py","w")
	file.write("this is madhu from trichy")
	file.close()
	file=open("new\\rohit.py","r")
	for line in file:
		print (line)
except FileNotFoundError:
	print("Error:File Not Found")
else:
	file.close()