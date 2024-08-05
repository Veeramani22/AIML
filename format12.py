print("-----------format----------------")
age = 20
txt = "My name is sam, and I am {}"
print(txt.format(age))


print("-------multiple arguments----------")
quantity = 3
count = 5
price = 50.10
my_order = "I want {} pieces of item {} for {} dolors."
print(my_order.format(quantity, count, price))

print("------use index numbers {0}----------")
quantity = 5
count = 7
price = 20.00
myorder = "I want to pay {2} dollar for {0} pieces of items {1}."
print(myorder.format(quantity, count, price))



txt = "My name is rohit, I am "
print(txt)
