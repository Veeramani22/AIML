#string and string functions
s="Madhu Mitha"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.endswith("ed"))
print(s.find("d"))
print(s.find("a"))
print(s.replace("i",'7'))
a="Mitha12345"
print("Is Upper:",a.isupper())
print("Is Lower:",a.islower())
print("Is Alpha Numberic:",a.isalnum())
print("Is Alpha:",a.isalpha())
s="he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a="failure is not the opposite of sucess it is part of success"
print(a.split(" "))

s="  Mitha  "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s="04-02-2002"
print(s.partition('_'))