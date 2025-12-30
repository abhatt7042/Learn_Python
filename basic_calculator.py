a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Welcome to the calculator \n Please select operation - A for Addition, \nS for Subtraction,\nM for Multiplication, \nD for Division, \nFD for Floor Division, \nMD for Modulus\n")
print(f"You have selected - {a},{b},{c}") 

if c.upper()=="A":
    print(f"Answer is : {a+b}")
elif c.upper()=="S":
    print(f"Answer is : {a-b}")
elif c.upper()=="M":
    print(f"Answer is : {a*b}")
elif c.upper()=="D":
    print(f"Answer is : {a/b}")
elif c.upper()=="FD":
    print(f"Answer is : {a//b}")
elif c.upper()=="MD":
    print(f"Answer is : {a%b}")

else:
    print("You did not select the right action, signing off bbye")