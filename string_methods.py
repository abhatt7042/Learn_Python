'''lets learn strings methods'''

a="introduction to COding!!!!!"

print(a.upper())

print(a.lower())

print(a.rstrip("!"))

print(a.lstrip("!"))

print(a.replace("ing","e"))

print(a.split(" "))

print(a.capitalize())

print(a.center(50))

print(a.count("i"))

print(a.endswith("!*"))

b="Ankita Bhatt"
print(b.endswith("Bhatt",5,12))

b="Ankita is a good girl"
print(b.find("is"))

# print (b.index("iss"))

b="Wohoo Here we go "

print(b.isalnum())

print(b.isalpha())

print(b.islower())

print(b.isprintable())

print(b.isspace())

print(b.istitle())

print(b.isupper())

print(b.startswith("Wohoo"))

print(b.swapcase())

print(b.title())