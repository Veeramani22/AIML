#open in python
try:
	file=open("sample\\test.py","r")
	print  (file.read())
except  FileNotFoundError:
	print("Error:File Not Found")
else:
	file.close()