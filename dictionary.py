#dictionary
user={
    "name":"priya",
    "age":25,"ismarried":True
    }
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())
for x in user:
      print(x," ",user[x])
for x in user.values():
      print(x)
for x in user.keys():
      print(x)
for x,y in user.items():
      print(x,y)
if"gender" in user:
      print("present")
#changing values
user.update({"gender":"female"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
users={
"user1":{
    "name":"priya",
    "age":25,
    "ismarried":True
    },
"user2":{
    "name":"madhu",
    "age":35,
    "ismarried":False
}
}
print(users)
