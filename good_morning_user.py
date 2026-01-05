
input=int(input("Enter current hour (0-23) : "))
if(5<=input<12):
    print("Good morning user")
elif(12<=input<17):
    print("Good noon user")
elif(17<=input<20):
    print("Good evening user")
else:
    print("Good night user")
