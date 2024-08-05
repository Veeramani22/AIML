#tryelse
try:
	a=10/5
except Exception as e:
	print(e)
else:
	print("A value:",a)
finally:
	print("thank you")