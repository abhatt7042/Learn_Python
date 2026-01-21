# reverse a string without using slicing
s=input("enter string to reverse")
l=len(s)
rev=""
# iterate through the string in reverse order
for i in range (l):
    rev=rev+s[l-i-1]
print(rev)



# reverse a string using slicing
a=input("enter string to reverse")
slice=a[::-1]
print(slice)
    