#read a file using readline in python
try:
	file=open("new\\word.py","r")
	#print (file.readline())
	print (file.readline(3))
	#print(file.readlines())
except FileNotFoundError:
	print("Error:File Not Found")
else:
	file.close()