#loop through the lines in python
try:
	file=open("new\\word.py","r")
	for line in file:
		print(line)
except  FileNotFoundError:
	print("Error:File Not Found")
else:
	file.close()