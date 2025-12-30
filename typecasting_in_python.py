#Explicit Type-casting - done manually by programmer
name='123'
name_cast=int(name)
print (name_cast)

#Implicit Type-casting - done automatically by python
a=7
b=2.5
c=a+b
print (type(c))
# datatype for c is changed to float by default via python to avoid data loss, this is implicit typecasting