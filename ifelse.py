# if else Statement in Python
#Write a program to check Vote eligibility by enter his/her name and age

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
	print(name, " age is ", age, " Eligibile for Vote.")
else:
	print(name, " age is ", age, " Not Eligible for Vote.")