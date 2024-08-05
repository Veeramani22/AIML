print("-------------------float conversion------------")
price=55
txt="the price is {:.2f} dollars"
print(txt.format (price))
print("-----------same values-----------")
age=36
name="priya"
txt="his name is{1}.{1} is {0} years old"
print(txt.format(age,name))
print("-------------named index-------")
myorder="i have a {scooty},it isa {model}."
print(myorder.format(scooty="yamaha",model="ray z"))
