#append mode life in python
try:
	file=open("new\\rohit.py","a")
	file.write("computer education")
	file.close()
	file=open("new\\rohit.py","r")
	print (file.read())
except FileNotFoundError:
	print("Error:File Not Found")
else:
	file.close()