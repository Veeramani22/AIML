try:
	f=open("New Text Document.txt")
except FileNotFoundError as e:
	print("File Not Found")
else:
	print(f.read())