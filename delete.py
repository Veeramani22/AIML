#delete a file in python
import os
if os.path.exists("new\\rohit.py"):
	os.remove("new\\rohit.py")
else:
	print("File Not Found")
	