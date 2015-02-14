a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
oper=input("Enter operation: ")

if oper=="+":
    print("The result is: "+str(a+b))
elif oper=="-":
    print("The result is: "+str(a-b))
elif oper=="*":
    print("The result is: "+str(a*b))
elif oper=="/":
    print("The result is: "+str(a/b))
else:
    print("Enter suitable operator +,-,* or /")
